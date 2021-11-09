from flask import Flask, render_template,request,redirect
from flask import Blueprint
from repositories import animal_repository
from repositories import owner_repository
from repositories import vet_repository
from repositories import treatment_repository
from models.treatment import Treatment
from datetime import date

treatments_blueprint=Blueprint('treatments',__name__)


@treatments_blueprint.route("/treatments")
def treatments():
    treatments=treatment_repository.select_all()
    return render_template("treatments/index.html",all_treatments=treatments)

# # NEW
# # GET '/treatments/new'
@treatments_blueprint.route("/treatments/new", methods=['GET'])
def new_treatment():
    animals=animal_repository.select_all()
    return render_template("/treatments/new.html",all_animals=animals)


# # CREATE
# # POST '/treatments'
@treatments_blueprint.route("/treatments", methods=['POST'])
def create_treatment():
    check_in_date=request.form['check_in_date']
    check_out_date=request.form['check_out_date']
    animal_id=request.form['animal_id']
    treatment_notes=request.form['treatment_notes']
    animal=animal_repository.select(animal_id)
    treatment=Treatment(check_in_date,check_out_date,animal,treatment_notes)
    treatment_repository.save(treatment)
    return redirect('/treatments')


# SHOW
# GET '/treatments/<id>'
@treatments_blueprint.route("/treatments/<id>", methods=['GET'])
def show_treatment(id):
    treatment=treatment_repository.select(id)
    return render_template('/treatments/index.html',treatment=treatment)


@treatments_blueprint.route("/treatments/show", methods=['GET'])
def show_treatment_by_date():
    treatments=treatment_repository.select_by_date()
    return render_template('/treatments/show.html',all_treatments=treatments)    


# EDIT
# GET '/treatments/<id>/edit'
@treatments_blueprint.route("/treatments/<id>/edit", methods=['GET'])
def edit_treatment(id):
    treatment=treatment_repository.select(id)
    animals=animal_repository.select_all()
    return render_template("/treatments/edit.html",treatment=treatment, all_animals=animals)


# UPDATE
# PUT '/treatments/<id>'
@treatments_blueprint.route("/treatments/<id>", methods=['POST'])
def update_treatment(id):
    check_in_date=request.form['check_in_date']
    check_out_date=request.form['check_out_date']
    treatment_notes=request.form['treatment_notes']
    animal_id=request.form['animal_id']
    animal=animal_repository.select(animal_id)
    treatment=Treatment(check_in_date,check_out_date,animal,treatment_notes,id)
    treatment_repository.update(treatment)
    return redirect('/treatments')


# # DELETE
# # DELETE '/treatments/<id>'  
@treatments_blueprint.route("/treatments/<id>/delete", methods=['POST'])
def delete_treatment(id):
    treatment_repository.delete(id)
    return redirect('/treatments')
   