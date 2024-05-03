from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/about')
def about():
    return render_template('public/about.html')

@app.route('/admin/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')

@app.route('/admin/settings')
def settings():
    return render_template('admin/settings.html')
