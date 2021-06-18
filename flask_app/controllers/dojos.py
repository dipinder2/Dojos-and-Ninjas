from flask import render_template,redirect,session,request
from flask_app import app
from ..models.dojo import Dojo

@app.route('/')
@app.route('/dojos')
def index():
    results = Dojo.get_all()
    
    return render_template("index.html", results = results)


@app.route('/dojo/create', methods=['POST'])
def create_dojo():

    print(Dojo.add_dojo(request.form))
    
    return redirect('/')


@app.route('/dojo/<int:id>/<name>')
def dojo_info(id,name):
    Dojo.get_one({'id':id})
    return render_template('dojoshow.html',ninjas = Dojo.get_one({'id':id}),name=name)