from db.run_sql import run_sql
from models.animal import Animal
from models.owner import Owner
from models.vet import Vet
from models.treatment import Treatment
import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository
import repositories.treatment_repository as treatment_repository


def save(vet):
    sql = "INSERT INTO vets (name) VALUES (%s) RETURNING *"
    values = [vet.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet


def select_all():
    vets = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for row in results:
        vet = Vet(row['name'],row['id'])
        vets.append(vet)
    return vets



def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if len(results)==0:
        return None
    result=results[0]
    if result is not None:
        vet = Vet(result['name'],result['id'])
    return vet


def delete_all():
    sql = "DELETE FROM vets "
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(vet):
    sql = "UPDATE vets SET (name) = (%s) WHERE id = %s"
    values = [vet.name]
    run_sql(sql, values)