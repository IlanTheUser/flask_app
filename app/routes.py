from flask import render_template, request, redirect, url_for, flash
from app import app
from app.models import save_user, get_all_users, get_user, update_user, delete_user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        # Extract form data
        full_name = request.form['full_name']
        age = request.form['age']
        skill_level = request.form['skill_level']
        country = request.form['country']
        motorcycle = request.form['motorcycle']

        # Attempt to save rider data
        success = save_user(full_name, age, skill_level, country, motorcycle)
        if success:
            flash('Registration successful for Yehuda Rally 2024', 'success')
            return render_template('success.html')
        else:
            flash('Registration failed. Please try again.', 'error')
            return redirect(url_for('index'))

@app.route('/members')
def members():
    riders = get_all_users()
    return render_template('members.html', riders=riders)

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_member(user_id):
    rider = get_user(user_id)
    if rider is None:
        flash('Rider not found', 'error')
        return redirect(url_for('members'))
    
    if request.method == 'POST':
        full_name = request.form['full_name']
        age = request.form['age']
        skill_level = request.form['skill_level']
        country = request.form['country']
        motorcycle = request.form['motorcycle']
        if update_user(user_id, full_name, age, skill_level, country, motorcycle):
            flash('Rider information updated successfully', 'success')
            return redirect(url_for('members'))
        else:
            flash('Failed to update rider information', 'error')
    return render_template('edit_member.html', rider=rider)

@app.route('/delete/<int:user_id>')
def delete_member(user_id):
    if delete_user(user_id):
        flash('Rider removed from registration successfully', 'success')
    else:
        flash('Failed to remove rider from registration', 'error')
    return redirect(url_for('members'))