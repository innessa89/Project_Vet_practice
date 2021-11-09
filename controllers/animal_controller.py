from flask import Flask, render_template,request,redirect
from flask import Blueprint
from repositories import animal_repository
from repositories import owner_repository
from repositories import vet_repository
from models.animal import Animal

animals_blueprint=Blueprint('animals',__name__)


@animals_blueprint.route("/animals")
def animals():
    animals=animal_repository.select_all()
    return render_template("animals/index.html",all_animals=animals)

# # NEW
# # GET '/animals/new'
@animals_blueprint.route("/animals/new", methods=['GET'])
def new_animal():
    vets=vet_repository.select_all()
    owners=owner_repository.select_all()
    return render_template("/animals/new.html",all_owners=owners,all_vets=vets)


# # CREATE
# # POST '/animals'

@animals_blueprint.route("/animals", methods=['POST'])
def create_animal():
    name=request.form['name']
    animal_type=request.form['animal_type']
    birth_date=request.form['birth_date']
    owner_id=request.form['owner_id']
    owner=owner_repository.select(owner_id)
    animal=Animal(name,animal_type,birth_date,owner,owner.vet,id)
    animal_repository.save(animal)
    return redirect('/animals')


# SHOW
# GET '/animals/<id>'
@animals_blueprint.route("/animals/<id>", methods=['GET'])
def show_animal(id):
    animal=animal_repository.select(id)
    return render_template('/animals/index.html',animal=animal)


# EDIT
# GET '/animals/<id>/edit'
@animals_blueprint.route("/animals/<id>/edit", methods=['GET'])
def edit_animal(id):
    animal=animal_repository.select(id)
    owners=owner_repository.select_all()
    return render_template("/animals/edit.html",animal=animal, all_owners=owners)


# UPDATE
# PUT '/animals/<id>'
@animals_blueprint.route("/animals/<id>", methods=['POST'])
def update_animal(id):
    name=request.form['name']
    animal_type=request.form['animal_type']
    birth_date=request.form['birth_date']
    owner_id=request.form['owner_id']
    owner=owner_repository.select(owner_id)
    animal=Animal(name,animal_type,birth_date,owner,owner.vet,id)
    animal_repository.update(animal)
    return redirect('/animals')


# # DELETE
# # DELETE '/animals/<id>'  
@animals_blueprint.route("/animals/<id>/delete", methods=['POST'])
def delete_animal(id):
    animal_repository.delete(id)
    return redirect('/animals')
   