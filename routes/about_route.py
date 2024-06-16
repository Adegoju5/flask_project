from flask import render_template, request

def about():
    return render_template('about.html')