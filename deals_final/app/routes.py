from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
import requests
import os
import pandas as pd



@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

######################################################################################
#API CODE GOES HERE
######################################################################################

        print('deal requested for member {}'.format(
            form.member.data))
        return redirect(url_for('thankyou'))
    return render_template('login.html',  title='Sign In', form=form)




@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        if request.files:

            image = request.files["image"]
            image.save(image.filename)

            print("Image saved")
            customer_data_file = image.filename
            customers = pd.read_excel(customer_data_file,
            
            header=0,
            index_col=False,
            keep_default_na=True
            )
            print(customers.head())

            return redirect((url_for('thankyou')))


    return render_template("upload.html")



@app.route('/thankyou')
def thankyou():
    
    return render_template('thankyou.html', title='Thankyou', )