from flask import Flask, render_template,request,redirect
from flask import Blueprint
from repositories import animal_repository
from repositories import owner_repository
from repositories import vet_repository
from models.owner import Owner

owners_blueprint=Blueprint('owners',__name__)


@owners_blueprint.route("/owners")
def owners():
    owners=owner_repository.select_all()
    return render_template("owners/index.html",all_owners=owners)

# # NEW
# # GET '/owners/new'
@owners_blueprint.route("/owners/new", methods=['GET'])
def new_owner():
    vets=vet_repository.select_all()
    return render_template("/owners/new.html",all_vets=vets)


# # CREATE
# # POST '/owners'
@owners_blueprint.route("/owners", methods=['POST'])
def create_owner():
    name=request.form['name']
    contact_info=request.form['contact_info']
    vet_id=request.form['vet_id']
    vet=vet_repository.select(vet_id)
    owner=Owner(name,contact_info,vet,id)
    owner_repository.save(owner)
    return redirect('/owners')


# SHOW
# GET '/owners/<id>'
@owners_blueprint.route("/owners/<id>", methods=['GET'])
def show_owner(id):
    owner=owner_repository.select(id)
    return render_template('/owners/index.html',owner=owner)


# EDIT
# GET '/owners/<id>/edit'
@owners_blueprint.route("/owners/<id>/edit", methods=['GET'])
def edit_owner(id):
    owner=owner_repository.select(id)
    vets=vet_repository.select_all()
    return render_template("/owners/edit.html",owner=owner, all_vets=vets)


# UPDATE
# PUT '/owners/<id>'
@owners_blueprint.route("/owners/<id>", methods=['POST'])
def update_owner(id):
    name=request.form['name']
    contact_info=request.form['contact_info']
    vet_id=request.form['vet_id']
    vet=vet_repository.select(vet_id)
    owner=Owner(name,vet,contact_info,id)
    owner_repository.update(owner)
    return redirect('/owners')


# # DELETE
# # DELETE '/owners/<id>'  
@owners_blueprint.route("/owners/<id>/delete", methods=['POST'])
def delete_owner(id):
    owner_repository.delete(id)
    return redirect('/owners')
   