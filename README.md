# Autonomous_dev

I wanted to put together a <a href="https://www.autonomousdev.net/">portfolio site</a> built completely from scratch so I made this. 

The project is build on django and mostly uses the django template system and bootstrap5 for frontend. The production database is PostgresSQL. Both the App and the data base are hosted on heroku. For file hosting the app is connected to AWS S3.

* To install this project you need the packages listes in requirements.txt
* The database hosting will default back to sqlite if no os variables point it else where. 
* Create a .env file in the project root filling the '' with the correct config value. Include the following values, 
# .env
EMAIL_USER = ''

EMAIL_PASS = ''

SECRET_KEY = ''

DEBUG_MODE = ''

AWS_ACCESS_KEY_ID = ''

AWS_SECRET_ACCESS_KEY = ''

AWS_STORAGE_BUCKET_NAME = ''
