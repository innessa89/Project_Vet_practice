import pdb
from models.owner import Owner
from models.animal import Animal
from models.vet import Vet
from models.treatment import Treatment

import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository
import repositories.treatment_repository as treatment_repository

vet1=Vet("Ilker Jons")
owner1=Owner("Deniz Sezer",vet1,"+445050973570")
animal1=Animal("Gumus","Cat","01.01.2015",owner1, vet1)
treatment1=Treatment("07.11.2021","10.11.2021",animal1,"Fractured leg")


vet2=Vet("Stiv Black")
owner2=Owner("Joanna McArthur",vet2,"+446580876545")
animal2=Animal("Sparkl","Dog","01.11.2021",owner2,vet2)
treatment2=Treatment("01.10.2021","01.10.2021",animal2,"Scheduled vaccinations")


saved_animal=animal_repository.save(animal1,)
print(saved_animal.id)
saved_animal=animal_repository.save(animal2,)
print(saved_animal.id)

saved_owners=owner_repository.save(owner1)
print(saved_owners.id)
saved_owners=owner_repository.save(owner2)
print(saved_owners.id)

saved_vets=vet_repository.save(vet1)
print(saved_vets.id)
saved_vets=vet_repository.save(vet2)
print(saved_vets.id)

saved_treatments=treatment_repository.save(treatment1)
print(treatment1.id)
saved_treatments=treatment_repository.save(treatment2)
print(treatment1.id)



