# blightPR

## Synopsis:

"San Juan - Abandoned Lots" app tries to recompile, consolidate, and publicly share data concerning San Juan’s list of abandoned lots under one straightforward and visually intuitive application.

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

% clone Git directory:

	$ git clone https://github.com/ernestoluisrojas/blightPR.git
	
% install required packages:

	$ pip install -r requirements.txt
	
% update Disqus API key:

	Modify ~/blightPR/blight_project/local_settings.py

	DISQUS_API_KEY = '<YOUR DISQUS API KEY>'

% setup database:

	~/blightPR $ python manage.py migrate
	
	~/blightPR $ python populate_blight.py
	
	~/blightPR $ python manage.py createsuperuser	

## Contributors

#Code4PR 
Sasha Mendez
Roger Reichard
Ernesto L Rojas

## License

