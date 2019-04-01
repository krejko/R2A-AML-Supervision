Security
========

Tokens
------

A token is a user authentication method. Tokens are used in the platform to identify the user identity and to know if a request being made to the platform will be carried out or rejected. The tokens have 325 bits of entropy, which is higher than the recommended 256 bits.

In order for the APIs to know which tokens are valid and which ones are not, the user needs to add the tokens to the system either by hardcoding the tokens in the code or by setting the tokens as environment variables.

The following tokens can be used by CNBV for additional institutions:

**DISCLAIMER** *This information was removed by CNBV's request* **DISCLAIMER**

Hardcoding
``````````
The user can hardcode the token in each of the API files, adding it to the tokens list. Likewise if the user wishes to remove a token, then he/she will need to remove the token manually from each of the API files. However, it is not recommended to do so, since it might be desirable to show the code to someone else and it might be easy to forget to delete the tokens.

As of right now the tokens are hardcoded in the API files in order for the APIs to be able to function "out of the box" without having to first configure environmnet variables.

Setting up an Environment Variable
``````````````````````````````````

Alternatively, the user can create an environment variable in the server and then tell python to load the environment variables. This is the recommended way to add a token, since the tokens will only be accesible by the people who has access to the server (a superuser).

It is recommended that the environment variable is set up in the following manner: ::

    TOKENS="token1 token2 token3"

Where each token is separated by a single space. Since there are different ways to add an environment variable, depending on the operating system and the environmet, it is left to the user to find the proper documentation for his/her operating system and environmet. For more information on environment variables please click `here
<https://en.wikipedia.org/wiki/Environment_variable>`_

After the environment variable is set up, Python needs to load the variables. In order to do this, the following lines must be included in each of the python files: ::

    import os
    TOKENS = os.environ['TOKENS'].split(" ")



Users
-----

To test the prototype's ability to handle user authentication some tests were performed using the Google Firebase Authentication platform.

Firebase Authentication is an open SDK(Software Developer Kit) distributed by Google which helps develop the infraestructure required to support user authentication in mobile or web applications.

The SDK allows the developer to choose the method of authentication such as email and password or through third party providers like Google, Facebook, etc.

When a user authenticates, a unique id is generated which can be used to grant access to certain components of the platform.

The implementation consists of two parts:

1. The id management is done through the Firebase Console, where the user basic data and login method is setup.

2. The SDK implementation is done by connecting the front end application to the Firebase Console. This enables the application to log in the users previously generated in the Console.

https://firebase.google.com/docs/reference/admin

Since CNBV will install the platform in its own servers, the implementation of the authentication service must be left to them.





