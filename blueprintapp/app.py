from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db=SQLAlchemy()

def create_app():
    app = Flask(__name__,template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///./blueprints.db'

    db.init_app(app)


    #import and register all blue prints
    from blueprintapp.blueprints.todos.routes import todos # we are importing the blueprint , if you remember we gave the blueprint to the variable todos check routes file u will see that
    from blueprintapp.blueprints.people.routes import people
    from blueprintapp.blueprints.core.routes import core

    app.register_blueprint(todos,url_prefix='/todos')
    app.register_blueprint(people,url_prefix='/people')
    app.register_blueprint(core,url_prefix="/")#No url prefix because this our home page


    migrate=Migrate(app,db)

    return app