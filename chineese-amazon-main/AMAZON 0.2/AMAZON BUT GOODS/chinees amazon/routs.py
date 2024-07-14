from flask import render_template, redirect
from forms import RegisterUser, AddProduct, LoginUser
from exstantions import app, db
from models import Product, User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
import os
from forms import AddProduct





@app.route('/dashboard', methods =['GET','POST' ])
def dashboard():
    return(render_template('dashboard.html'))




@app.route("/")
def home_page():
        return render_template("base.html",)



@app.route("/reg", methods=["POST", "GET"])
def register():
    form = RegisterUser()
    if form.validate_on_submit():
        new_user = User(email=form.email.data,password=form.password.data, username=form.username.data, role="User")

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect("/dashboard")
    return render_template("registration.html", form=form)

@app.route("/log", methods=["POST", "GET"])
def log():
    form = LoginUser()
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
    return render_template("login.html", form=form, )
    
@app.route("/logout", methods=["POST", "GET"])

def logout():
    logout_user()
    return redirect("/")
    

@app.route("/add_product", methods=["POST", "GET"])
@login_required
def add_product():
    if current_user.role != "admin":
        return redirect("/")
    form = AddProduct()
    if form.validate_on_submit():
        new_product = Product (name=form.name.data,
                               mage_url=form.image_url.data, 
                               price=form.price.data, 
                               text=form.text.data)
        db.session.add(new_product)
        db.session.commit()
        return redirect("/")
    
    return render_template("amazonproducts.html", form=form)

@app.route("/edit_product/<int:id>", methods=["POST", "GET"])
@login_required
def edit_product(id):
    product = Product.query.get(id)

    form = AddProduct(name=product_name, text=product_text, price=product_price,)

    if form.validate_on_submit():
        product_name = form.name.data
        product_text = form.text.data
        product_price = form.price.data
    
        db.session.commit()
        return redirect("/")
    