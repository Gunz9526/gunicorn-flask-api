import os

JWT_SECRET_KEY = {
    'SECRET_KEY' : 'rehabilitation'
}
base_dir = os.path.abspath(os.path.dirname(__file__))
db_file = os.path.join(base_dir, 'database.db')