import os
import urllib

#db_pw = urllib.parse.quote_plus("!ppmysql!@")
#db = {
#     'user' : 'user',
#     'password' : 'pw',
#     'host' : '3.34.133.41',
#     'port' : '3306',
#     'database' : 'gunicorn'
# }
JWT_SECRET_KEY = {
    'SECRET_KEY' : 'rehabilitation'
}
base_dir = os.path.abspath(os.path.dirname(__file__))
db_file = os.path.join(base_dir, 'database.db')

# DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"