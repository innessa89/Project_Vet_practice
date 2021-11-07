DROP TABLE IF EXISTS treatments;
DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS vets; 

CREATE TABLE vets(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact_info VARCHAR(255),
    vet_id INT REFERENCES vets(id)
);

CREATE TABLE animals(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    animal_type VARCHAR(255),
    birth_date VARCHAR(255),
    owner_id INT REFERENCES owners(id),
    vet_id INT REFERENCES vets(id)
);

CREATE TABLE treatments(
    id SERIAl PRIMARY KEY,
    check_in_date VARCHAR(255),
    check_out_date VARCHAR(255),
    treatment_notes VARCHAR(255),
    animal_id INT REFERENCES animals(id)
);
