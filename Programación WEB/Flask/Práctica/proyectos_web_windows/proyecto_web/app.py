from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/settings/profile')
def settings_profile():
    return render_template('settings_profile.html')

@app.route('/settings/account')
def settings_account():
    return render_template('settings_account.html')

if __name__ == '__main__':
    app.run(debug=True)

