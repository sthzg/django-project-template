In any working environment this directory needs to contain a file named 
.env. This file holds sensitive environment variables that must not be 
distributed in GIT.

Remember to chmod this file to something very restrictive. It needs to be 
readable by the user under which the WSGI server runs. In case of webfaction 
this user is the system user, which makes 400 appropriate.

    $ chmod 400 ./.env
    
**Example**

You can copy this code, rename the attributes and save it to ./.env. 

    #!/bin/bash
    DJ_##PROJECT##_CURRENT_ENV=""
    
    DJ_##PROJECT##_DEV_SECRET_KEY=""
    DJ_##PROJECT##_DEV_DB_NAME=""
    DJ_##PROJECT##_DEV_DB_USER=""
    DJ_##PROJECT##_DEV_DB_HOST=""
    DJ_##PROJECT##_DEV_DB_PASS=""
    
    DJ_##PROJECT##_DEV_CELERY_USER=""
    DJ_##PROJECT##_DEV_CELERY_PASS=""
    DJ_##PROJECT##_DEV_CELERY_HOST=""
    DJ_##PROJECT##_DEV_CELERY_PORT=""
    
    DJ_##PROJECT##_DEV_SERVER_EMAIL=""
    DJ_##PROJECT##_DEV_EMAIL_BACKEND=""
    DJ_##PROJECT##_DEV_EMAIL_HOST=""
    DJ_##PROJECT##_DEV_EMAIL_PORT=""
    DJ_##PROJECT##_DEV_EMAIL_HOST_USER=""
    DJ_##PROJECT##_DEV_EMAIL_HOST_PASSWORD=""
    DJ_##PROJECT##_DEV_EMAIL_USE_TLS=""