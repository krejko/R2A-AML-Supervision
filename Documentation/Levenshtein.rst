Levenshtein
===========

OFAC
----

In order to run a list of names against the OFAC watchlist add the list of names to the ``nombres_pruebas.csv`` csv file inside the Levenshtein directory. After the ``nombres_pruebas.csv`` file is loaded with the names that will be compared against the watchlist navigate to the Levenshtein directory and run the file ``listas.py`` this will download the OFAC lists and compare the names in the csv file against the watchlist. 

When the program is finished, the user will be able to see the result if the names match up to a 80% and the user will see the letter ``a`` if the names in the csv file don't match a name in the watchlist

UN
--
In order to run a list of names against the UN watchlist add the list of names to the ``nombres_pruebas.csv`` csv file inside the Levenshtein directory. After the ``nombres_pruebas.csv`` file is loaded with the names that will be compared against the watchlist navigate to the Levenshtein directory and open python, then type the following commands: ::

    from listas import *
    run the file ``listas.py`` this will download the OFAC lists and compare the names in the csv file against the watchlist. 
    lec_lista_onu('https://scsanctions.un.org/resources/xml/en/consolidated.xml')
    
When the program is finished, the user will be able to see the result if the names match up to a 80% and the user will see the letter ``a`` if the names in the csv file don't match a name in the watchlist
