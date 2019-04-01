import psycopg2
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from scipy.stats import norm
from scipy.optimize import minimize, approx_fprime
from sklearn import datasets, linear_model
import random


def eig(eig_vals_corr, eig_vecs_corr):
    eig_pairs = [(np.abs(eig_vals_corr[i]), eig_vecs_corr[:,i]) for i in range(len(eig_vals_corr))]
    eig_pairs.sort()
    eig_pairs.reverse()
    #print('Eigenvalues in descending order:')
    #for i in eig_pairs:
    #    print(i[0])
    tot = sum(eig_vals_corr)
    var_exp = [(i / tot)*100 for i in sorted(eig_vals_corr, reverse=True)]
    var_exp
    cum_var_exp = np.cumsum(var_exp)
    cum_var_exp
    return(var_exp,cum_var_exp, eig_pairs)

    
def pca(eig_pairs, df, top):
    matrix_w = np.hstack((eig_pairs[0][1].reshape(len(eig_pairs),1), 
                      eig_pairs[1][1].reshape(len(eig_pairs),1)))
    matrix_w=pd.DataFrame(matrix_w)
    matrix_w.insert(0, 'Vars', df.columns.T)
    matrix_w.columns=['Vars','PC1','PC2']
    matrix_w['PC1'] = matrix_w['PC1'].abs()
    matrix_w['PC2'] = matrix_w['PC2'].abs()
    print(matrix_w)
    pc1 = matrix_w.sort_values("PC1", ascending = 0)[['Vars','PC1']]
    pc1 = pc1.head(n=top)
    pc2 = matrix_w.sort_values("PC2", ascending = 0)[['Vars','PC2']]
    pc2 = pc2.head(n=top)
    pc1=pc1.merge(pc2, left_on='Vars', right_on='Vars', how='outer')
    return(pc1)

def filtro_K(arg,x,P,med,varr,reales,dia):
    
    a = np.array(arg[dia][0:5])
    A = np.array([arg[dia][5:7], arg[dia][7:9]])
    H = np.array([arg[dia][9:11], arg[dia][11:13], arg[dia][13:15], arg[dia][15:17], arg[dia][17:19]])
    h = np.array(arg[dia][19:25])
    
    print(dia)
    
    x_apr = np.dot(A,x[(dia-1)%7]) + med[dia]
    P_apr = np.dot(A, np.dot(P[(dia-1)%7], np.transpose(A))) + np.diag(varr[dia])
    K_1 = np.dot(P_apr, np.transpose(H))
    K_2 = np.dot(H, K_1) 
    #Hacemos a la matriz K_2 positiva definida
    for i in range(5):
        if K_2[i][i] > h[i]:
            h[i] = K_2[i][i]*1.1
    K_3 = K_2 + np.diag(h)

    inv = np.linalg.cholesky(K_3)
    inv = np.linalg.solve(inv, np.diag([1,1,1,1,1]))
    K = np.dot(K_1, np.dot(inv, np.transpose(inv)))
    x_post = x_apr + np.dot(K, (reales[dia] - a - np.dot(H, x_apr)))
    P_post = np.dot((np.diag([1,1]) - np.dot(K, H)), P_apr)
    P_post[0][0] = np.abs(P_post[0][0])
    P_post[1][1] = np.abs(P_post[1][1])
    
    bnds=[(-100, 100),]*19
    [bnds.append((0.001,5)) for i in range(5)]

    try:    
        res = minimize(logver, arg[dia]
                       ,args=(x, P, med, varr, reales)
                       ,method='L-BFGS-B'
                       ,bounds =bnds
                       ,options={'disp':False, 'maxiter':150, 'gtol':1e-4})
    except IOError:    
        res = minimize(logver, arg[dia]
                       ,args=(x, P, med, varr, reales)
                       ,method='Nelder-Mead'
                       ,options={'disp':False, 'maxiter':1000, 'fatol':1})
    
    return x_post, P_post, res

def logdist(opt,x,P,med,varr, z):
    
    a = opt[0]
    A = opt[1]
    H = opt[2]
    h = opt[3]
    
    P_apr = np.dot(A, np.dot(P, np.transpose(A))) + np.diag(varr)
    
    #Hacemos a la matriz P_val positiva definida
    for i in range(5):
        if np.dot(H, np.dot(P_apr, np.transpose(H)))[i][i] > h[i]:
            h[i] = np.dot(H, np.dot(P_apr, np.transpose(H)))[i][i]*1.1
            
    P_val = np.dot(H, np.dot(P_apr, np.transpose(H))) + np.diag(h)
    inv = np.linalg.cholesky(P_val)
    inv = np.linalg.solve(inv, np.diag([1, 1, 1, 1, 1]))
    P_inv = np.dot(inv, np.transpose(inv))
    
    return -np.linalg.det(P_val) - np.dot(np.transpose((z - a - np.dot(H,np.dot(A,x) - med))), np.dot(P_inv, (z - a - np.dot(H,np.dot(A,x) - med))))

def logver(opt, x, P, med, varr, z):
    opt = [opt[0:5], opt[5:7], opt[7:9], opt[9:11], opt[11:13], opt[13:15], opt[15:17], opt[17:19], opt[19:25]]
    opt = (np.array(opt[0]), np.array([opt[1], opt[2]]), np.array([opt[3], opt[4],
            opt[5], opt[6], opt[7]]), np.array(opt[8]))
    func = 0
    for i in range(7):
        func = func - logdist(opt,x[(i-1)%7],P[(i-1)%7],med[i],varr[i],z[i])
    return func

if __name__ == '__main__':
    pca = PCA(n_components=2)
    pca.fit(est_base.drop('fecha', axis=1))
    proyeccion = pd.DataFrame(pca.transform(est_base.drop('fecha', axis=1)))
    componentes = pd.DataFrame(pca.components_)
    componentes = componentes.transpose()
    componentes.columns = [['PC1', 'PC2']]
    proyeccion.columns = [['PC1', 'PC2']]
    proyeccion['PC1_LAG'] = proyeccion.PC1.shift(1)
    proyeccion['PC2_LAG'] = proyeccion.PC2.shift(1)
    proyeccion['PC1_Diff1']=proyeccion.PC1_LAG-proyeccion.PC1
    proyeccion['PC2_Diff1']=proyeccion.PC2_LAG-proyeccion.PC2
    proyeccion['PC1_Diff1_rollVar5'] = proyeccion.PC1_Diff1.rolling(5,5).var()
    proyeccion['PC2_Diff1_rollVar5'] = proyeccion.PC2_Diff1.rolling(5,5).var()
    proyeccion = proyeccion.loc[(-pd.isnull(proyeccion.PC1_Diff1_rollVar5)) & (-pd.isnull(proyeccion.PC2_Diff1_rollVar5))]\
    .reset_index(drop=True)
    base = base.reset_index()
    datos['weekday'] = datos['fecha'].apply(lambda x: x.weekday())
    est_base['weekday'] = est_base['fecha'].apply(lambda x: x.weekday())
    base['weekday'] = base['fecha'].apply(lambda x: x.weekday())
    weekdays = pd.DataFrame({'weekday':[0,1,2,3,4,5,6], 'day':['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']})
    proyeccion = pd.concat([proyeccion, est_base.weekday[5:].reset_index(drop=True)], axis=1)
    xxx, xxy, res = filtro_K(args, x, P, medias, varianzas, reales, 1)
    for n in range(len(est_base)):
        fecha = est_base.fecha.loc[n]
        datos = est_base.loc[est_base.fecha == fecha]
        dia = datos.weekday.tolist()[0]
        z[dia] = np.squeeze(datos.reset_index(drop=True)[['1','2','3','4','5','6']]\
        .as_matrix())
        med = []
        varr = []
        for i in range(7):
            proy_dia = comp_1m.loc[comp_1m.weekday == i].reset_index(drop=True)
            med.append(np.array([proy_dia.PC1.mean(), proy_dia.PC2.mean()]))
            varr.append(np.array([proy_dia.PC1.var(), proy_dia.PC2.var()]))
        del proy_dia

        x[dia], P[dia], res = filtro_K(args, x, P, med, varr, z, dia)
        args[dia] = res.x
        comp_1m = comp_1m.append(pd.DataFrame([[x[dia][0], x[dia][1], dia]],
                                            columns=['PC1', 'PC2', 'weekday'], index=[91]))
        comp_1m = comp_1m.drop(0).reset_index(drop=True)
        print(n)
    fun = lambda x: (x[0] - 1)**2 + (x[1] - 2.5)**2
    cons = ({'type': 'ineq', 'fun': lambda x:  x[0] - 2 * x[1] + 2},
            {'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 6},
            {'type': 'ineq', 'fun': lambda x: -x[0] + 2 * x[1] + 2})
    bnds = ((0, None), (0, None))
    res = minimize(fun, (2, 0), method='SLSQP', bounds=bnds,
                   constraints=cons)