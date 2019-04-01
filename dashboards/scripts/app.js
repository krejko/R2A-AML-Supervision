var app = angular.module("cnbvAPP", ["ngRoute"]);
app.config(function($routeProvider) {
    $routeProvider
        .when("/", {
            templateUrl: "partials/home.html"
        })
        .when("/intro", {
            templateUrl: "partials/intro.html",
            controller: "intro"
        })
        .when("/inicio", {
            templateUrl: "partials/inicio.html",
            controller: "inicio"
        })
        .when("/riesgos", {
            templateUrl: "partials/riesgos.html",
            controller: "riesgos"
        })
        .when("/riesgosUno", {
            templateUrl: "partials/riesgosUno.html",
            controller: "riesgosuno"
        })
        .when("/riesgosDos", {
            templateUrl: "partials/riesgosDos.html",
            controller: "riesgosdos"
        })
        .when("/riesgosTres", {
            templateUrl: "partials/riesgosTres.html",
            controller: "riesgos"
        })
        .when("/riesgosCuatro", {
            templateUrl: "partials/riesgosCuatro.html",
            controller: "riesgos"
        })
        .when("/riesgosCinco", {
            templateUrl: "partials/riesgosCinco.html",
            controller: "riesgos"
        })
        .when("/riesgosSeis", {
            templateUrl: "partials/riesgosSeis.html",
            controller: "riesgos"
        })
        .when("/riesgosSiete", {
            templateUrl: "partials/riesgosSiete.html",
            controller: "riesgos"
        })
        .when("/riesgosOcho", {
            templateUrl: "partials/riesgosOcho.html",
            controller: "riesgos"
        })
        .when("/riesgosNueve", {
            templateUrl: "partials/riesgosNueve.html",
            controller: "riesgos"
        })
        .when("/riesgosDiez", {
            templateUrl: "partials/riesgosDiez.html",
            controller: "riesgos"
        })
        .when("/riesgosOnce", {
            templateUrl: "partials/riesgosOnce.html",
            controller: "riesgos"
        })
        .when("/riesgosDoce", {
            templateUrl: "partials/riesgosDoce.html",
            controller: "riesgos"
        })
        .when("/riesgosTrece", {
            templateUrl: "partials/riesgosTrece.html",
            controller: "riesgosTrece"
        })
        .when("/riesgosCatorce", {
            templateUrl: "partials/riesgosCatorce.html",
            controller: "riesgos"
        })
        .when("/riesgosQuince", {
            templateUrl: "partials/riesgosQuince.html",
            controller: "riesgos"
        })
        .when("/riesgosDieciseis", {
            templateUrl: "partials/riesgosDieciseis.html",
            controller: "riesgosDieciseis"
        })
        .when("/riesgosDiecisiete", {
            templateUrl: "partials/riesgosDiecisiete.html",
            controller: "riesgos"
        })
        .when("/riesgosDieciocho", {
            templateUrl: "partials/riesgosDieciocho.html",
            controller: "riesgos"
        })
        .when("/riesgosDiecinueve", {
            templateUrl: "partials/riesgosDiecinueve.html",
            controller: "riesgos"
        })
        .when("/riesgosVeinte", {
            templateUrl: "partials/riesgosVeinte.html",
            controller: "riesgos"
        })
        .when("/riesgosVeintiuno", {
            templateUrl: "partials/riesgosVeintiuno.html",
            controller: "riesgos"
        })
        .when("/riesgosVeintidos", {
            templateUrl: "partials/riesgosVeintidos.html",
            controller: "riesgos"
        })
        .when("/riesgosVeintitres", {
            templateUrl: "partials/riesgosVeintitres.html",
            controller: "riesgos"
        })
        .when("/riesgosVeinticuatro", {
            templateUrl: "partials/riesgosVeinticuatro.html",
            controller: "riesgos"
        })
        .when("/riesgosVeinticinco", {
            templateUrl: "partials/riesgosVeinticinco.html",
            controller: "riesgos"
        })
        .when("/riesgosVeintiseis", {
            templateUrl: "partials/riesgosVeintiseis.html",
            controller: "riesgos"
        })
        .when("/riesgosVeintisiete", {
            templateUrl: "partials/riesgosVeintisiete.html",
            controller: "riesgos"
        })
        .when("/riesgosVeintiocho", {
            templateUrl: "partials/riesgosVeintiocho.html",
            controller: "riesgos"
        })
        .when("/riesgosVeintinueve", {
            templateUrl: "partials/riesgosVeintinueve.html",
            controller: "riesgos"
        })
        .when("/riesgosTreinta", {
            templateUrl: "partials/riesgosTreinta.html",
            controller: "riesgos"
        })
        .when("/expedienteInstitucionFinanciera", {
            templateUrl: "partials/expedienteInstitucionFinanciera.html",
            controller: "expedienteInstitucionFinanciera"
        })
        .when("/expedienteInstitucionFinancieraDos", {
            templateUrl: "partials/expedienteInstitucionFinancieraDos.html"
        })
        .when("/expedienteInstitucionFinancieraTres", {
            templateUrl: "partials/expedienteInstitucionFinancieraTres.html"
        })
        .when("/expedienteInstitucionFinancieraCuatro", {
            templateUrl: "partials/expedienteInstitucionFinancieraCuatro.html"
        })
        .when("/expedienteInstitucionFinancieraCinco", {
            templateUrl: "partials/expedienteInstitucionFinancieraCinco.html"
        })
        .when("/expedienteInstitucionFinancieraSeis", {
            templateUrl: "partials/expedienteInstitucionFinancieraSeis.html"
        })
        .when("/expedienteInstitucionFinancieraSiete", {
            templateUrl: "partials/expedienteInstitucionFinancieraSiete.html"
        })
        .when("/expedienteInstitucionFinancieraOcho", {
            templateUrl: "partials/expedienteInstitucionFinancieraOcho.html"
        })
        .when("/expedienteInstitucionFinancieraNueve", {
            templateUrl: "partials/expedienteInstitucionFinancieraNueve.html",
            controller: "expedienteInstitucionFinancieraNueve",
            css: "css/prueba_.css"
        })
        .when("/expedienteInstitucionFinancieraDiez", {
            templateUrl: "partials/expedienteInstitucionFinancieraDiez.html"
        })
        .when("/expedienteInstitucionFinancieraOnce", {
            templateUrl: "partials/expedienteInstitucionFinancieraOnce.html"
        })
        .when("/expedienteConciliacion", {
            templateUrl: "partials/expedienteConciliacion.html",
            controller: "expedienteConciliacion"
        })
        .when("/expedienteConciliacionUno", {
            templateUrl: "partials/expedienteConciliacionUno.html",
            controller: "expedienteConciliacionUno"
        })
        .when("/expedienteEstadistica", {
            templateUrl: "partials/expedienteEstadistica.html"
        })
        .when("/expedienteEstadisticaUno", {
            templateUrl: "partials/expedienteEstadisticaUno.html"
        })
        .when("/expedienteEstadisticaDos", {
            templateUrl: "partials/expedienteEstadisticaDos.html"
        })
        .when("/expedienteAlertas", {
            templateUrl: "partials/expedienteAlertas.html"
        })
        .when("/expedienteAlertasUno", {
            templateUrl: "partials/expedienteAlertasUno.html"
        })
        .when("/entradapublica", {
            templateUrl: "partials/entradapublica.html"
        })
        .when("/dragdrop", {
            templateUrl: "partials/dragdrop.html"
        });
});

app.controller('MainCtrl', function($scope, $routeParams, $route, $location) {
    $scope.$watch(function() {
            return ($route.current && $route.current.css) ? $route.current.css : 'css/style.css';
        },
        function(value) {
            $scope.css = value;
        });
});

app.controller("intro", function($scope) {});

app.controller("inicio", function($scope) {});

app.controller("riesgos", function($scope, $http) {
    $http.get('/CNBV_NUEVO/data/instrumentomonetario.json')
        .then(function(res) {
            $scope.instrumentos = res.data['0'];
        });
        
    $http.get('/CNBV_NUEVO/data/perfilInstitucion.json')
        .then(function(res) {
            $scope.perfiles = res.data;
            console.log(res);
        });
        
    $http.get('http://169.57.27.134:3001/api/R24_tabla_alert')
        .then(function(res) {
            $scope.alertamientos = res.data;
        });
        
    $http.get('http://169.57.27.134:3001/api/CuestOper_tabla_alert')
        .then(function(res) {
            $scope.alertamientosfondika = res.data;
        });
});

app.controller("riesgosuno", function($scope, $http) {
    $http.get('http://169.57.27.134:3001/api/s1r1')
        .then(function(res) {
            $scope.mppfs = res.data.table;
    console.log(res.data);
        });
});

app.controller("riesgosdos", function($scope, $http) {
    $http.get('/CNBV_NUEVO/data/riesgosdos.json')
        .then(function(res) {
            $scope.riesgos = res.data;
        });
});

app.controller("riesgosTrece", function($scope, $http) {
});

app.controller("riesgosDieciseis", function($scope, $http) {
    $http.get('http://169.57.27.134:3001/api/s5r4_tifr_mapageo_lines')
        .then(function(res) {
            $scope.lineas = res.data;
            //console.log(res);
        });
        
        
    $http.get('http://169.57.27.134:3001/api/s5r4_tifr_tabla1')
        .then(function(res) {
            $scope.tabalaunos = res.data;
            //console.log(res);
        });
        
    $http.get('http://169.57.27.134:3001/api/s5r4_tifr_tabla2')
        .then(function(res) {
            $scope.tabaladoss = res.data;
            //console.log(res);
        });
});

app.controller("expedienteInstitucionFinanciera", function($scope, $location) {
    $scope.go = function(path) {
        $location.path(path);
    };
});

app.controller("expedienteConciliacion", function($scope, $http) {
    $http.get('http://169.57.27.134:3001/api/rs2r2_tablaMonto')
        .then(function(res) {
            $scope.tablaconc = res.data;
            //console.log(res);
        });
});

app.controller("expedienteConciliacionUno", function($scope, $http) {
    $http.get('http://169.57.27.134:3001/api/rs2r2_tablaMonto')
        .then(function(res) {
            $scope.tablaconc = res.data;
            //console.log(res);
        });
        
    $http.get('http://169.57.27.134:3001/api/rs2r2_tablaMontoF')
        .then(function(res) {
            $scope.tablaconcFondika = res.data;
            //console.log(res);
        });
});


app.controller("expedienteInstitucionFinancieraNueve", function($scope, $route, $routeParams, $location) {});
