import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY = os.getenv('SECRET_KEY') or 'notsosecretkey'
    CURRENT_VERSION = os.getenv('CURRENT_VERSION') or 'development'
    SERVICE_NAME = os.getenv('SERVICE_NAME') or 'Sample Application'
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    # SQLITE database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_POOL_SIZE = None    


config_by_name = dict(
    development=DevelopmentConfig
)  
      