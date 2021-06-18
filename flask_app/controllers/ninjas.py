from flask import render_template,redirect,session,request
from flask_app import app
from ..models.dojo import Dojo
from ..models.ninja import Ninja


@app.route('/ninja/add')
def add_ninja():
    results = Dojo.get_all()
    return render_template('addninja.html', dojos = results)


@app.route('/new-ninja/add', methods=['POST'])
def create_ninja():
    Ninja.add_ninja(request.form)
    return redirect('/')