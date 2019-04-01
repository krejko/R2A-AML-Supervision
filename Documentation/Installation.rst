Installation
============

After the Ubuntu 16.04 LTS opertating system is installed in the host machine please follow these steps:

1. Install Git with the following command in: ``sudo apt-get install git``
2. Install Python 3.6.0
3. Install the necessary external python libraries detailed `here <Requirements.rst#python>`_.
4. Install PostgreSQL 9.6, plese follow these `instructions <https://www.postgresql.org/download/linux/ubuntu/>`_.
5. Install MongoDB, please follow these `instructions <https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/>`_.
6. Clone the delivered Github repository with the following command: ``git clone [PATH]`` where path is the http link of the Github repository.


After following these steps the platform will be ready to run

Before Turning the Platform On for the first time
-------------------------------------------------

1. Read the `Security <Security.rst>`_ section of the documentation and make the necessary changes with regards to user authentication and token management.
2. Read the `dashboards considerations <Dashboards.rst#considerations>`_ section of the documentation and make the necessary changes with regards to the server IP address.

To Turn-on the Platform
-----------------------

1. Navigate to the APIs directory and turn-on the APIs with the following command: ``python api.py``
2. Navigate to the Dashboards directory and turn-on the web server (see `Dashboards
<Dashboards.rst>`_ for more information)

After following these steps the platform will be ready to receive information from the financial institutions and to display that information in the Dashboards.

To use the machine learning models please check the `Machine Learning
<MachineLearning.rst>`_ section of the documentation.

To use the Levenshtein algorithm and sweep the OFAC and UN watchlists please check the `Levenshtein
<Levenshtein.rst>`_ section of the documentation.
