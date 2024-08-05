from flask import render_template, request, redirect, url_for, flash
from app import app
from app.models import save_user, get_all_users, get_user, update_user, delete_user

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
            flash('Registration successful', 'success')
            return render_template('success.html')
        else:
            # If save fails, return an error message
            flash('Registration failed. Please try again.', 'error')
            return redirect(url_for('index'))

@app.route('/members')
def members():
    users = get_all_users()
    return render_template('members.html', users=users)

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_member(user_id):
    user = get_user(user_id)
    if user is None:
        flash('User not found', 'error')
        return redirect(url_for('members'))
    
    if request.method == 'POST':
        full_name = request.form['full_name']
        age = request.form['age']
        email = request.form['email']
        city = request.form['city']
        if update_user(user_id, full_name, age, email, city):
            flash('User updated successfully', 'success')
            return redirect(url_for('members'))
        else:
            flash('Failed to update user', 'error')
    return render_template('edit_member.html', user=user)

@app.route('/delete/<int:user_id>')
def delete_member(user_id):
    if delete_user(user_id):
        flash('User deleted successfully', 'success')
    else:
        flash('Failed to delete user', 'error')
    return redirect(url_for('members'))