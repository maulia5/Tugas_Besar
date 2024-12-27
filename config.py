class Config(object):
    HOST = "localhost"
    PORT = 3306
    USER = "root"
    PASSWORD = ""
    DB = "sewa_mobil"
    SECRET_KEY = "admin1234#"
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True