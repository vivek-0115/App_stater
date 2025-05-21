class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LocalDevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///appDB.sqlite3"
    
    # Flask-Security / Flask-Security-Too settings
    SECURITY_PASSWORD_SALT = "salty"
    SECURITY_PASSWORD_HASH = "bcrypt"
    SECRET_KEY = "SecretApp" 
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authorization"
    
    # For disabling CSRF in WTF forms (note the typo fix)
    WTF_CSRF_ENABLED = False    