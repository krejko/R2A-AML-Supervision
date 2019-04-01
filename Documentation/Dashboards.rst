Dashboards
==========

The dashboards are tools that enable the user to visualize data in several ways. The platform has 4 Dashboards which are the following 

+-----------------------------------------------------------------------------------------------------------------------------+-------------------------+
|Dashboard                                                                                                                    |HTML file                |
+=============================================================================================================================+=========================+
|Reporte de Entrada                                                                                                           |riesgos                  |
+-----------------------------------------------------------------------------------------------------------------------------+-------------------------+
|Número de operaciones y monto para personas físicas menores de edad, mayores a 80 años y personas morales con menos de 3 años|riesgosUno               |
+-----------------------------------------------------------------------------------------------------------------------------+-------------------------+
|Operaciones hacia países de baja imposición fiscal                                                                           |riesgosDieciseis         |
+-----------------------------------------------------------------------------------------------------------------------------+-------------------------+
|Conciliacion de elemento de cuestionario vs información operativa por producto y moneda                                      |expedienteConciliacionUno|
+-----------------------------------------------------------------------------------------------------------------------------+-------------------------+

In order to be able to view the dashboards the user needs to setup a web server, such as NginX, Apache, Node.js etc. The prototype used the python 3.6.0 built in webserver which is great for development and testing purposes, which is the case for the prototype; however, another web server must be used if the number of users starts to increase.

In the case of the prototype the user needs to first fun the `api.py` file located in the APIs directory, this will turn on the `outgoing information APIs
<APIs.rst#outgoing-information-apis>`_ that provide the JSON to fill the plots, graphs, maps, etc. Once the APIs are up and running, navigate towards the Dashboards directory where the `index.html` file is located and run the following command in the terminal(for windows users see `requirements
<Requirements.rst#windows-users>`_): ::

    python -m http.server

Once the server is running the user will be able to visualize the dashboards.

Considerations
--------------

1. Since the APIs ran on a server that is no longer working, the user needs to change the IP address and port number in all of the dashboard files, so that they will request the JSON to the correct server. The current IP address is `169.57.27.134`, once the prototype is installed in a new server please change the IP address to the IP address of the new server.

2. Because the web server used for the platform is designed for development and testing purposes in doesn't allow Crossed-Origin-Resource-Sharing, which basically means that the dashboards will not accept the information coming from the APIs, in order to solve this, the user can either use a different web server allowing Crossed-Origin-Resource-Sharing or install an extension in his/her browser allowing Crossed-Origin-Resource-Sharing (for example "Allow-Control-Allow-Origin: \*") to be able to use the built-in python server.