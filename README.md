# Base Flask Project for Azure App Service
This base project includes configuration that allows Flask Microframework to be used with Azure App Service

Setup
-----

### Installation
Run the following commands:

    $ git clone git@github.com:oespirilla/azure-flask-sample.git

    $ cd azure-flask-sample

    $ [sudo] pip install virtualenv

    $ virtualenv ENV

    # Activate enviroment (POSIX)
    $ source <ENV_NAME>/bin/activate

    # Activate enviroment (Windows)
    > \path\to\env\Scripts\activate

    # Installing dependencies
    (ENV)$ pip install -r requirements.txt

	  # Running a local instance
    (ENV)$ python runserver.py

The site will now be accessible at [http://localhost:8000/](http://localhost:8000/)
