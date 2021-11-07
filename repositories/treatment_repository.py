from db.run_sql import run_sql
from models.animal import Animal
from models.owner import Owner
from models.vet import Vet
from models.treatment import Treatment
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository


def save(treatment):
    sql = "INSERT INTO treatments (check_in_date, check_out_date, animal_id,treatment_notes) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [treatment.check_in_date,treatment.check_out_date,treatment.animal.id,treatment.treatment_notes]
    results = run_sql(sql, values)
    id = results[0]['id']
    treatment.id = id
    return treatment


def select_all():
    treatments = []

    sql = "SELECT * FROM treatments"
    results = run_sql(sql)

    for row in results:
        animal=animal_repository.select(row['animal_id'])
        treatment = Treatment(row['check_in_date'],row['check_out_date'], animal, row['treatments_notes'],row['id'])
        treatments.append(treatment)
    return treatments



def select(id):
    owner = None
    sql = "SELECT * FROM treatments WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        animal=animal_repository.select(result['animal_id'])
        treatment = Treatment(result['check_in_date'],result['check_out_date'], animal, result['treatments_notes'],result['id'])
    return treatment


def delete_all():
    sql = "DELETE FROM treatments "
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM treatments WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_by_animal_id(animal_id):
    sql = "DELETE FROM treatments WHERE animal_id = %s"
    values = [animal_id]
    run_sql(sql, values)


def update(treatment):
    sql = "UPDATE treatments SET (check_in_date, check_out_date, animal_id, treatment_notes) = (%s, %s, %s, %s) WHERE id = %s"
    values = [treatment.check_in_date,treatment.check_out_date,treatment.animal.id,treatment.treatment_notes]
    run_sql(sql, values)
