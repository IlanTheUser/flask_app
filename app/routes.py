from flask import render_template, request, redirect, url_for
from app import app
from app.models import save_user

# Define route for the home page
@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

# Define route for handling form submission
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        # Extract form data
        full_name = request.form['full_name']
        age = request.form['age']
        email = request.form['email']
        city = request.form['city']

        # Attempt to save user data
        success = save_user(full_name, age, email, city)
        if success:
            # If save is successful, render success page
            return render_template('success.html')
        else:
            # If save fails, return an error message
            return "Registration failed. Please try again."