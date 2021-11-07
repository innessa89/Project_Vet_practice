from db.run_sql import run_sql
from models.animal import Animal
from models.owner import Owner
from models.vet import Vet
from models.treatment import Treatment
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository
import repositories.treatment_repository as treatment_repository

def save(owner):
    sql = "INSERT INTO owners (name,vet_id,contact_info) VALUES (%s, %s, %s) RETURNING *"
    values = [owner.name,owner.vet.id,owner.contact_info]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id
    return owner


def select_all():
    owners = []

    sql = "SELECT * FROM owners"
    results = run_sql(sql)

    for row in results:
        vet=vet_repository.select(row['vet_id'])
        owner = Owner(row['name'], vet,row['contact_info'], row['id'] )
        owners.append(owner)
    return owners



def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if len(results)==0:
        return None
    result=results[0]
    if result is not None:
        vet=vet_repository.select(result['vet_id'])
        owner = Owner(result['name'], vet, result['contact_info'], result['id'] )
    return owner


def delete_all():
    sql = "DELETE FROM animals "
    run_sql(sql)


def delete(id):
    animal_repository.delete_by_owner_id(id)
    sql = "DELETE FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_by_vet_id(vet_id):
    sql = "SELECT id FROM owners where vet_id = %s"
    values = [vet_id]
    results = run_sql(sql)

    for row in results:
        owner_id = row['id']
        animal_repository.delete_by_owner_id(owner_id)

    sql = "DELETE FROM owners WHERE vet_id = %s"
    values = [vet_id]
    run_sql(sql, values)    


def update(owner):
    sql = "UPDATE owners SET (name,vet_id,contact_info) = (%s, %s, %s) WHERE id = %s"
    values = [owner.name,owner.vet.id,owner.contact_info,owner.id]
    run_sql(sql, values)
