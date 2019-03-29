import os


def check_database(app, db):
    # db_path = format_database_url(app.config['DATABASE_PATH'])
    # db_uri = 'sqlite:///{}'.format(db_path)
    # app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    #
    # print(app.config['SQLALCHEMY_DATABASE_URI'])

    # db.init_app(app)

    # db_is_new = not os.path.exists(app.config['DATABASE_PATH'])

    db.create_all()

    # if db_is_new:
    #     print("CREATE A NEW DATABASE")
    # else:
    #     print("DATABASE ALREADY CREATED")



def get_database_url(app):
    db_path = format_database_url(app.config['DATABASE_PATH'])
    return 'sqlite:///{}'.format(db_path)


def format_database_url(path):
    dirname = os.path.dirname(__file__)[:-len(__package__)]
    dirname = dirname.replace("\\", "/")
    return os.path.join(dirname, path)

