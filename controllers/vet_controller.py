from flask import Flask, render_template,request,redirect
from flask import Blueprint
from repositories import animal_repository
from repositories import owner_repository
from repositories import vet_repository
from models.vet import Vet

vets_blueprint=Blueprint('vets',__name__)


@vets_blueprint.route("/vets")
def vets():
    vets=vet_repository.select_all()
    return render_template("vets/index.html",all_vets=vets)

# # NEW
# # GET '/vets/new'
@vets_blueprint.route("/vets/new", methods=['GET'])
def new_vet():
    return render_template("/vets/new.html")


# # CREATE
# # POST '/vets'
@vets_blueprint.route("/vets", methods=['POST'])
def create_vet():
    name=request.form['name']
    vet=Vet(name,id)
    vet_repository.save(vet)
    return redirect('/vets')


# SHOW
# GET '/vets/<id>'
@vets_blueprint.route("/vets/<id>", methods=['GET'])
def show_vet(id):
    vet=vet_repository.select(id)
    return render_template('/vets/index.html',vet=vet)


# EDIT
# GET '/vets/<id>/edit'
@vets_blueprint.route("/vets/<id>/edit", methods=['GET'])
def edit_vet(id):
    vet=vet_repository.select(id)
    return render_template("/vets/edit.html",vet=vet)


# UPDATE
# PUT '/vets/<id>'
@vets_blueprint.route("/vets/<id>", methods=['POST'])
def update_vet(id):
    name=request.form['name']
    vet=Vet(name,id)
    vet_repository.update(vet)
    return redirect('/vets')


# # DELETE
# # DELETE '/vets/<id>'  
@vets_blueprint.route("/vets/<id>/delete", methods=['POST'])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect('/vets')
   