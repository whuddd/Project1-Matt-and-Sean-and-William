import csv

def read_penguin_data(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def calc_avg_body_mass_by_species(data):
    species_mass = {}
    species_count = {}
    for penguin in data:
        species = penguin['species']
        mass = penguin.get('body_mass_g', '').strip()
        if mass.lower() not in ('', 'na'):
            mass = float(mass)
            species_mass[species] = species_mass.get(species, 0) + mass
            species_count[species] = species_count.get(species, 0) + 1
    avg_mass = {}
    for species in species_mass:
        avg_mass[species] = species_mass[species] / species_count[species]
    return avg_mass

def calc_male_percentage_by_island(data):
    males = {}
    total = {}
    for penguin in data:
        island = penguin['island']
        sex = penguin.get('sex', '').strip().lower()
        if sex in ('male', 'female'):
            total[island] = total.get(island, 0) + 1
            if sex == 'male':
                males[island] = males.get(island, 0) + 1
    percent_male = {}
    for island in total:
        percent_male[island] = (males.get(island, 0) / total[island]) * 100
    return percent_male