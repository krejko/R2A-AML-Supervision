Database Considerations
=======================

PostgreSQL
----------

After installing the PostgreSQL database management system (DBMS) it is highly recommended to create user roles. This will enable the user to manage access permissions, helping to restrict access to the appropiate level, to read more about database roles and how to set them up please click `here <https://www.postgresql.org/docs/9.6/static/user-manag.html>`_

It is highly recommended to create a specific role for the APIs, with the necessary permission them to be able to create and alter tables.

After a deciding which role is goint to be used by the APIs to add and retrieve information to the database it is necessary to edit the ``APIs/SQLhelpers.py`` and the ``APIs/Dashboards/SQLhelpers.py`` files to let the APIs know which role to use. 

Specifically the user needs to change the following part: ::

    PG_HOST = os.environ['PG_HOST']
    PG_USR = os.environ['PG_USR']
    PG_PASS = os.environ['PG_PASS']
    PG_DB = os.environ['PG_DB']
    PG_PORT = os.environ['PG_PORT']

Where the user needs to change ``PG_HOST`` with the address of the machine hosting the database,in the prototype the database is in the same server as the APIs so the value is ``localhost``. ``PG_USR`` is where the username of the new role goes, and ``PG_Pass`` is where the user's passwords go. ``PG_DB`` is where the name of the database goes. Finally ``PG_PORT`` is the port used by PostgreSQL, normally it is ``5342``.

The user can change the values of the aforementioned variables in two ways. The values can be hardcoded, which is not recommended, because anyone looking at the code will be able see the user password and will therefore gain access to the database.

An example of how a hardcoded code looks like is as follows: ::
    
    PG_HOST = 'localhost'
    PG_USR = 'gestell'
    PG_PASS = '123456'
    PG_DB = 'CNBV_db'
    PG_PORT = '5432'

The recommended alternative is to use environment variables, which is what was done in the prototype. The setup of an environmet variable depends on the operating system and the environment used, to find out more about environment variables click `here <https://en.wikipedia.org/wiki/Environment_variable>`_.

MongoDB
-------

The MongoDB Database Management System (DBMS) will be used by the platform when the machine learning models require automatic continuous training. Since this was not the case for the prototype (it was only trained one time) the MongoDB DBMS was not used. It is advisable to use the MongoDB DBMS in the future when the prototype goes into production  to automate the training process 
