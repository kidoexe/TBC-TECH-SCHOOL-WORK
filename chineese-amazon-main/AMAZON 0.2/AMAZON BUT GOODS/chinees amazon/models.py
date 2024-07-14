from exstantions import db, app
from flask_login import LoginManager
from exstantions import db, app, login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

login_manager = LoginManager(app)



class Product(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)

    price = db.Column(db.Float)

    text = db.Column(db.String)

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key = True)

    email = db.Column(db.String)

    password = db.Column(db.String)

    username = db.Column(db.String)

    role = db.Column(db.String)

    def __init__(self, email, password, username,role="user"):
            self.email = email
            self.password = generate_password_hash(password)
            self.username = username
            self.role = role


    def check_password(self, password):
        return check_password_hash(self.password, password)



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("db was done")
        admin = User(email = "sabaking389@gmail.com", 
                     password = "ADMIN1",
                     username = "SuperAdmin",
                     role = "admin")
        db.session.add(admin)
        db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)