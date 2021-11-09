from db.run_sql import run_sql
from models.animal import Animal
from models.owner import Owner
from models.vet import Vet
from models.treatment import Treatment
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.treatment_repository as treatment_repository



def save(animal):
    sql = "INSERT INTO animals (name, animal_type, birth_date, owner_id,vet_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name,animal.animal_type,animal.birth_date,animal.owner.id,animal.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal


def select_all():
    animals = []

    sql = "SELECT * FROM animals"
    results = run_sql(sql)
    

    for row in results:
        owner = owner_repository.select(row['owner_id'])
        vet=vet_repository.select(row['vet_id'])
        animal = Animal(row['name'], row['animal_type'], row['birth_date'],owner,vet, row['id'] )
        animals.append(animal)
    return animals


def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if len(results)==0:
        return None
    result=results[0]
    if result is not None:
        owner = owner_repository.select(result['owner_id'])
        vet=vet_repository.select(result['vet_id'])
        animal = Animal(result['name'], result['animal_type'], result['birth_date'], owner, vet, result['id'] )
    return animal



def delete_all():
    sql = "DELETE FROM animals "
    run_sql(sql)


def delete(id):
    treatment_repository.delete_by_animal_id(id)
    sql = "DELETE FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_by_vet_id(vet_id):
    sql = "SELECT id FROM animals where vet_id = %s"
    values = [vet_id]
    results = run_sql(sql)

    for row in results:
        animal_id = row['id']
        treatment_repository.delete_by_animal_id(animal_id)

    sql = "DELETE FROM animals WHERE vet_id = %s"
    values = [vet_id]
    
    run_sql(sql, values)    


def delete_by_owner_id(owner_id):
    sql = "SELECT id FROM animals where owner_id = %s"
    values = [owner_id]
    results = run_sql(sql)

    for row in results:
        animal_id = row['id']
        treatment_repository.delete_by_animal_id(animal_id)

    sql = "DELETE FROM animals WHERE owner_id = %s"
    values = [owner_id]
    
    run_sql(sql, values)  


def update(animal):
    sql = "UPDATE animals SET (name, animal_type, birth_date, owner_id,vet_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.name,animal.animal_type,animal.birth_date,animal.owner.id,animal.vet.id,animal.id]
    run_sql(sql, values)



    