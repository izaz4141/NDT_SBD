from dotenv import load_dotenv, find_dotenv
import os
# import redis
load_dotenv(find_dotenv())
class Flask_Config:
    SECRET_KEY = os.environ.get("FLASK_SECRET")

    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{os.environ.get("USER_NAME")}:{os.environ.get("USER_PASSWORD")}@localhost/ndt_sbd'

    # SESSION_TYPE = 'redis'
    # SESSION_PERMANENT = False
    # SESSION_USE_SIGNER = True
    # SESSION_REDIS = redis.from_url('redis://localhost:6379')
