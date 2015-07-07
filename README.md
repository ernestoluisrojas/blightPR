# blightPR

## Synopsis:

"San Juan - Abandoned Lots App" tries to recompile, consolidate, and publicly share data concerning San Juan’s list of abandoned lots under one straightforward and visually intuitive application.

## Packages:

disqus-python==0.4.2

Django==1.7.1

django-bootstrap-toolkit==2.15.0

django-disqus==0.5

mock==1.0.1

Pillow==2.8.1

pyshp==1.2.1

simplejson==3.6.5

South==1.0.2

## Installation:

% download setuptools:

	$ cd setuptools-1.1.6
	$ sudo python ez_setup.py
	$ sudo easy_install pip
	$ pip install virtualenv
	$ pip install virtualenvwrapper

% create a virtual environment:

	For Linux:
	$ source virtualenvwrapper
	$ mkvirtualenv blight_env
	$ workon blight_env

	For Windows:
	
	> virtualenv blight_env
	> cd blight_env
	> .\Script\activate

% install required packages:

	$ pip install -r requirements.txt

% clone Git directory:

	$ git clone https://github.com/ernestoluisrojas/blightPR.git

% setup database:

	~/blight_project $ python manage.py makemigrations
	
	~/blight_project $ python manage.py migrate
	
	~/blight_project $ python populate_blight.py
	
	~/blight_project $ python manage.py createsuperuser	

% update Disqus API key:

	Modify blight_project>local_settings.py

	DISQUS_API_KEY = '<YOUR DISQUS API KEY>'

## Contributors


## License

