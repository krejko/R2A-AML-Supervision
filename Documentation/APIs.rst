Application Programming Interfaces (APIs)
=========================================

The platform has two kinds of application programming interfaces (APIs). The first kind of APIs handle incoming information, i.e. information coming from financial instituions at the request of CNBV.

The second kind of APIs handle outgoing information, i.e. information already stored inside CNBV's databases that is going to be used to create graphs, plots, maps, etc. in the dashboards.

Despite the fact that there are just over 30 APIs, the user only needs to manage one, which is the master API, this API will turn-on and off all of the APIs described in this section, as well as managing the incoming requests and outgoing replies. The python file for the master API is called `api.py` and is located in the APIs directory.

Incoming information APIs
-------------------------

There are 28 different APIs that handle incoming information for the platform to validate and consolidate. Out of these, 22 are used to validate operational information stored in the financial institusions' databases. The platform uses exactly 22 different APIs for this purpose because CNBV has 22 different layouts, detailing how the financial institution should format the information stored in its databases.

In order for a financial institution to be able to upload information to CNBV's databases, the financial institution requires a token. This token has two main purposes. The first one is for security purposes, the platform will only accept information incoming from specific sources, avoiding injection attacks if it were to allow access to anyone with the URL. The second reason for the token is to be used as an identifier, so that the platform will lable incoming information with the financinal institution's name.

Each layout has an API associated with it, in order for the financial institution to upload data following 

As of right now the platform requires the cURL software library to transfer data (available for Linux, OSX, and Windows, see requirements). The cURL command needed to upload files to CNBV is the following: ::

    curl -F "datafile=@[PATH]" -X POST "http://xxx.xx.xx.xxx:xxxx/api/[API ROUTE]?pw=[password]" 

Where ``[PATH]`` is where the file is located, ``xxx.xx.xx.xxx`` should be replaced with the public IP address of the server where the APIs are running, ``:xxxx`` is the specific port (inside the server) in which the APIs are runnning, ``[API ROUTE]`` is the specific API (out of the 22) which is going to be used to read the file, and finally ``[password]`` is the financial institution's token.

The following table specifies the API route for each of the 22 different layouts: 

**DISCLAIMER** *This table was removed by CNBV's request* **DISCLAIMER**

Example: Let's imagine that a senior Banorte employee wants to upload the file ``client_info.txt`` located in ``/home/Documents`` of her computer following the FBD-Clientes-usuarios format with the token ``Banorte123456``. She already knows that the IP address of CNBV's server is ``123.45.67.890`` and that the APIs are running on port ``3001``, then she will use the following cURL command: ::

    curl -F "datafile=@/home/Documents/client_info.txt" -X POST "http://123.45.67.890:3001/api/clientes_usuarios?pw=Banorte123456"


The files containing the financial institution's operational information have to follow CNBVs guidelines, otherwise the API will reject the file and display an error messagine indicating that the file did not follow the specified format. In order for the API to accept the file it has to be a csv file in text format (with the ``.txt`` file extension), separated by pipes ``|``, with exactly the number of columns specified by CNBV, without empty compulsory columns, and the specified date format (``YYYYMMDD``). 

Of the remaining 6 APIs, 2 are used by the institution tu upload the "Reporte de Operaciones Inusuales" (unusual operations report) and the "Reporte de Operaciones Relevantes" (relevant operations report) which are required by the "Unidad de Inteligencia Financiera" (UIF, financial intelligence unit). These two APIs also take csv files in text format, separated by semicolons ``;``. These APIs are special in the sense that they will not reject the file if there are imperfections in it, as required by CNBV. The only ocassion in which the API will reject the report is if the financial institution tries to use the "Reporte de Operaciones Inusuales" API to upload a relevant operations report, or viceversa.

To upload the UIF reports the financial institution uses the same cURL command used to upload its operational information, with the following API routes:

**DISCLAIMER** *This table was removed by CNBV's request* **DISCLAIMER**

The final 4 APIs were developed with CNBV in mind, the actual user of these APIs will be a CNBV employee so that the platform will be able to use the "R24" reports and the "Cuestionario de Operatividad" (operational questionaire) to compare the financial institution's operational information with what was reported by the institution.

To upload the reports the user uses the same cURL command used by the other APIs, with the following API routes:

**DISCLAIMER** *This table was removed by CNBV's request* **DISCLAIMER**

Everything that is read with the APIs will be saved in a PostgreSQL database in the system, the names of the tables inside the databases and the names of the columns can be found inside the python files for each API.

Outgoing information APIs
-------------------------

Each Dashboard requires javascript object notation (JSON) text to fill the plots, graphs, maps, etc. with the financial institution's data. In order to get the necessary JSON the platform has several APIs that will generate the JSON needed for each element in each dashboard. These APIs are also activated via a cURL command, which follows this pattern: ::

    curl -X GET "http://xxx.xx.xx.xxx:xxxx/api/[API ROUTE]"

Where ``xxx.xx.xx.xxx`` represents the public IP address of the server where the APIs are running, ``:xxxx`` is the specific port (inside the server) in which the APIs are runnning, and ``[API ROUTE]`` is the specific API which will generate the necessary JSON to send data to the dashboards.

The following table specifies the necessary API route for each element of each dashboard.

**DISCLAIMER** *This table was removed by CNBV's request* **DISCLAIMER**
