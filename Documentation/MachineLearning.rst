Machine Learning
================

The platform uses 4 different machine learning models to analyze the financial institutions data and provide new ingisghts regarding high risk behaviours. 

The models, and their associated files, used by the platform are:

+----------------------+---------------+------------------+
|Machine learning model|Python file(s) |Trained model file|
+======================+===============+==================+
|Logistic regression   |gnosis_cl      |log_res           |
+----------------------+---------------+------------------+
|Clustering            |gnosis_cl      |clusters          |
+----------------------+---------------+------------------+
|Neural networks       |classify & eval|neural_network    |
+----------------------+---------------+------------------+
|Random forests        |gnosis_rf      |mod_RF            |
+----------------------+---------------+------------------+

Training the models
-------------------

In order to train the files the platform uses an extra file to help train the model, this file is called pipeline.sh.

Every time a user wants to train one of the models, lines 1, 4 and 10 of the pipline.sh file must be edited: ::

    1   $tablas = ()
    
    4   	cat psql -U postgres -d database_name -c 'SELECT *  FROM $ ;'  |

    10  sed *.py |


In line `1` the user must add the name of the tables where the information that is going to be used to train the model is stored. In line `4` the user must replace `database_name` with the name of the database where the information is stored, and (if needed) `postgres` with the username. In line 10 the user needs to replace the `*` with the name of the python file that contains the model the user wants to train (see table above).

Once the script is ready the user needs to open a terminal window (for windows users see `requirements
<Requirements.rst#windows-users>`_) and run the script. To run the script please navigate towards the folder containing the pipline.sh file, write the filename in the terminal and press enter. After the process is finished a trained model file will have been created.

Using Trained model files
-------------------------

To use the machine learning models one first needs to load the model, in order to do this execute the following commands in python: ::

    from sklearn.externals import joblib

    lodaded_model = joblib.load(filename)

Where file name is the name of the file containing the trained machine learning model. Once the model is loaded it can now be used to produce instights base some data, to do this execute the following commands in python (after the model was loaded): ::

    loaded_model.predict(data)

Where data is a pandas dataframe containing the data that is going to be analyzed.
