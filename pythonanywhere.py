# PythonAnywhere WSGI configuration file
import sys
import os

# Add your project directory to the Python path
project_home = '/home/yourusername/mysite'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Import your Flask app
from app import app as application

# Make sure app runs in production mode
application.debug = False
