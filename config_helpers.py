

import os

def get_base_url():

    env = os.environ.get('ENV', 'prod')

    if env.lower() == 'dev':
        return 'https://yph-com.allbugs.info'
        # return 'http://localhost:8888/localdemostore/'
    elif env.lower() == 'prod':
        return 'http://hyalual.com'
    else:
        raise Exception(f"Unknown environment: {env}")

def get_database_credentials():

    env = os.environ.get('ENV', 'dev')

    db_user = os.environ.get("yph")
    db_password = os.environ.get("3YSmqTdm")
    if not db_user or not db_password:
        raise Exception("Environment variables 'DB_USER' and 'DB_PASSWORD' must be set.")

    if env == 'dev':
        db_host = '127.0.0.1'
        db_port = 8889
    elif env == 'prod':
        db_host = 'demostore.supersqa.com'
        db_port = 3306
    else:
        raise Exception(f"Unknown environment: {env}")

    db_info = {"db_host": db_host, "db_port": db_port,
               "db_user": db_user, "db_password": db_password}

    return db_info