from flask import render_template, session

def home():
    return render_template('home_page.html')


