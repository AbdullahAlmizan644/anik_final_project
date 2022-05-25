from flask import Flask,Blueprint
from flask_mysqldb import MySQL
from flask_ckeditor import CKEditor
from flask_mail import Mail,Message

ckeditor = CKEditor()
db=MySQL()
mail=Mail()

def create_app():
    UPLOAD_FOLDER = 'C:\\Users\\abdul\\OneDrive\\Desktop\\agro_system\\website\\static\\image'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    app=Flask(__name__)
    app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
    app.config['SECRET_KEY']='Anik'
    app.config['MYSQL_HOST']='127.0.0.1'
    app.config['MYSQL_USER']='root'
    app.config['MYSQL_PASSWORD']=''
    app.config['MYSQL_DB']='agro_system'


    app.config["MAIL_SERVER"]='smtp.gmail.com' 
    app.config["MAIL_PORT"] = 465
    app.config['MAIL_USE_TLS'] = False  
    app.config['MAIL_USE_SSL'] = True  
    app.config["MAIL_USERNAME"] = 'dekbovideo@gmail.com'  
    app.config['MAIL_PASSWORD'] = '5255452554'  

    def format_datetime(value, format="%d %b %Y %I:%M %p"):
        if value is None:
            return ""
        return value.strftime(format)

    # Register the template filter with the Jinja Environment
    app.jinja_env.filters['formatdatetime'] = format_datetime

    db.init_app(app)
    ckeditor.init_app(app)
    mail.init_app(app)



    from .view import view
    from .review import review
    from .shop import shop
    from .admin import admin
    from .auth import auth
    from .expert import expert



    app.register_blueprint(view, url_prefix="/")
    app.register_blueprint(review, url_prefix="/")
    app.register_blueprint(shop, url_prefix="/")
    app.register_blueprint(admin, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(expert, url_prefix="/")


    return app