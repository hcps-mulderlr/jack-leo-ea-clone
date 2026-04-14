import os
#fix for vulnerability #2: making the secret key random
SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
DB_CONFIG = {
    "host": "localhost",
    "database": "clone_lab",
    "user": "postgres",
    "password": "postgres"
}

SECRET_KEY = os.environ.get("SECRET_KEY", "dev_secret_key")
