from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

# Dummy users for demonstration purposes
users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # Authentication successful, redirect to the main page
        return redirect(url_for('index'))
    else:
        # Authentication failed, redirect back to the login page
        return redirect(url_for('login'))

@app.route('/my-link/')
def my_link():
    print("hello")
    subprocess.call('python ff.py', shell=True)
    return redirect(url_for('display_stress_level'))

@app.route('/display-stress-level')
def display_stress_level():
    try:
        with open("average_stress_level.txt", "r") as file:
            average_stress_level = file.read()
    except FileNotFoundError:
        average_stress_level = "File not found."

    return render_template('display_stress_level.html', average_stress_level=average_stress_level)

if __name__ == '__main__':
    app.run(debug=True)
