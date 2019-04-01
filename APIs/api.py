from Dashboards.AudSec5Rep4 import apiS5R4
from Dashboards.AudSec1Rep1 import apiS1R1
from Dashboards.RepEnt import apiRepEnt
from Layouts.tipo_cambio_api import api_tipo_cambio
from Layouts.TIFR_api import apiTIFR
from Layouts.TIFE_api import apiTIFE
from Reportes_UIF.rips_relevantes_api import apiRIPSrel
from Reportes_UIF.rips_inusuales_api import apiRIPSin
from Layouts.peps_api import apiPEPS
from Layouts.inusuales_CCC_api import apiCCC
from Layouts.exigibilidad_inmediata_api import apiExIn
from R24_CO.excell_api import apiCuestOper
from Layouts.cvfi_api import apiCVFI
from Layouts.clientes_usuarios_api import apiCU
from Layouts.clientes_cuentasN1_api import apiN1
from Layouts.clientes_cuentas_api import apiCCuentas
from Layouts.clientes_ar_api import apiAR
from Layouts.alertas_api import apiAlert
from Dashboards.RiSec2Rep2 import apiRS2R2
from Dashboards.AudSec1Rep1f import apiS1R1f
from Layouts.remesas_api import apiRemesas
from Layouts.md_api import apiMD
from Layouts.mc_api import apiMC
from Layouts.fideicomiso_api import apiFideicomiso
from Layouts.fi_api import apiFI
from Layouts.ex_in_ope_api import apiExInOpe
from Layouts.clientesBP_api import apiClientesBP
from Layouts.creditos_api import apiCreditos
from Layouts.dep_plazo_api import apiDepPlazo
from Layouts.divisas_api import apiDivisas
from R24_CO.R24E50_api import r24e50
from R24_CO.R24E51_api import r24e51
from R24_CO.R24E52_api import r24e52

if __name__ == '__main__':
    apiRepEnt.merge(apiS5R4)
    apiRepEnt.merge(apiS1R1)
    apiRepEnt.merge(api_tipo_cambio)
    apiRepEnt.merge(apiTIFR)
    apiRepEnt.merge(apiTIFE)
    apiRepEnt.merge(apiRIPSrel)
    apiRepEnt.merge(apiRIPSin)
    apiRepEnt.merge(apiPEPS)
    apiRepEnt.merge(apiCCC)
    apiRepEnt.merge(apiExIn)
    apiRepEnt.merge(apiCuestOper)
    apiRepEnt.merge(apiCVFI)
    apiRepEnt.merge(apiCU)
    apiRepEnt.merge(apiN1)
    apiRepEnt.merge(apiCCuentas)
    apiRepEnt.merge(apiAR)
    apiRepEnt.merge(apiAlert)
    apiRepEnt.merge(apiRS2R2)
    apiRepEnt.merge(apiS1R1f)
    apiRepEnt.merge(apiRemesas)
    apiRepEnt.merge(apiMD)
    apiRepEnt.merge(apiMC)
    apiRepEnt.merge(apiFideicomiso)
    apiRepEnt.merge(apiFI)
    apiRepEnt.merge(apiCuestOper)
    apiRepEnt.merge(apiExInOpe)
    apiRepEnt.merge(apiClientesBP)
    apiRepEnt.merge(apiCreditos)
    apiRepEnt.merge(apiDepPlazo)
    apiRepEnt.merge(apiDivisas)
    apiRepEnt.run(host='0.0.0.0', port=3001, reloader=False)
