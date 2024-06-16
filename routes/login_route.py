from flask import render_template, request

def login():
    if request.method == 'POST':
        # Process login form submission
        # Example: authenticate user
        return 'Logged in successfully!'
    return render_template('login.html')

