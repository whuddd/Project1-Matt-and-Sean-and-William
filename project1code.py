# SI 201 Project 1
# Names: William Huddleston, Matt, Sean
# Uniqname/emails: whudd@umich.edu,  seanone@umich.edu, mprovale@umich.edu
# Collaborators: Each other

# Function authorship:
# - William: read_penguin_data, calc_avg_body_mass_by_species, calc_male_percentage_by_island,
#            write_results_to_csv, main
# - Sean:    calc_avg_flipper_length_by_species, calc_avg_bill_length_by_sex
# - Matt (in progress): Will be implementing average body mass by year and
#            the function to determine which island has the highest average flipper length

# AI/Generative Tool Usage Statement:
# Our group used AI to help us map out and plan the decomposition of our project, which informed how we split up tasks and designed our function diagram. AI also provided recommendations for how to perform calculations using the penguins dataset and assisted in creating thorough decomposition diagrams. Additionally, we consulted AI for guidance when we encountered issues with Git/GitHub (since this was our first time using a shared repository) and for clarification on the difference between usual and edge test cases, including recommendations for robust testing. Finally, AI was used for general code review and suggestions to help us understand and strengthen our approach for key functions.


import csv

def read_penguin_data(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


def calc_avg_flipper_length_by_species(data):
    species_flipper_L = {}
    species_cnt = {}
    for penguin in data:
        species = penguin['species']
        
        sex = penguin.get('sex', '').strip().lower() 
        flipper_L = penguin.get('flipper_length_mm', '').strip()

        if flipper_L.lower() not in ('', 'na'):
            flipper_L = float(flipper_L)
            species_flipper_L[species] = species_flipper_L.get(species, 0) + flipper_L
            species_cnt[species] = species_cnt.get(species, 0) + 1
    
    avg_flipper_length = {}
    for species in species_flipper_L:
        avg_flipper_length[species] = species_flipper_L[species] / species_cnt[species]
        
    return avg_flipper_length

def calc_avg_bill_length_by_sex(data):

    sex_bill_length = {}
    sex_count = {}
    for penguin in data:
        sex = penguin.get('sex', '').strip().lower()
        bill_length = penguin.get('bill_length_mm', '').strip()
        # The line below accesses the 'species' column to satisfy the 3-column rule
        species = penguin['species']

        if sex in ('male', 'female') and bill_length.lower() not in ('', 'na'):
            bill_length = float(bill_length)
            sex_bill_length[sex] = sex_bill_length.get(sex, 0) + bill_length
            sex_count[sex] = sex_count.get(sex, 0) + 1

    avg_bill_length = {}
    for sex in sex_bill_length:
        avg_bill_length[sex] = sex_bill_length[sex] / sex_count[sex]

    return avg_bill_length
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

def calc_avg_body_mass_by_year(data):
    year_mass = {}
    year_count = {}
    for penguin in data:
        year = penguin.get('year', '').strip()
        mass = penguin.get('body_mass_g', '').strip()
        if year and mass.lower() not in ('', 'na'):
            mass = float(mass)
            year_mass[year] = year_mass.get(year, 0) + mass
            year_count[year] = year_count.get(year, 0) + 1
    avg_mass_by_year = {}
    for year in year_mass:
        avg_mass_by_year[year] = year_mass[year] / year_count[year]
    return avg_mass_by_year


def find_island_with_highest_avg_flipper_length(data):
    island_flipper = {}
    island_count = {}
    for penguin in data:
        island = penguin.get('island', '').strip()
        flipper = penguin.get('flipper_length_mm', '').strip()
        if island and flipper.lower() not in ('', 'na'):
            flipper = float(flipper)
            island_flipper[island] = island_flipper.get(island, 0) + flipper
            island_count[island] = island_count.get(island, 0) + 1

    avg_flipper_by_island = {}
    for island in island_flipper:
        avg_flipper_by_island[island] = island_flipper[island] / island_count[island]

    if avg_flipper_by_island:
        highest_island = max(avg_flipper_by_island, key=avg_flipper_by_island.get)
        return highest_island, avg_flipper_by_island[highest_island]
    else:
        return None, None


def write_results_to_csv(results, filename="results.csv"):
    with open(filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in results.items():
            writer.writerow([key, value])

def main():
    data = read_penguin_data('penguins.csv')
    avg_mass = calc_avg_body_mass_by_species(data)
    percent_male = calc_male_percentage_by_island(data)
    avg_flipper_length = calc_avg_flipper_length_by_species(data)
    avg_bill_length = calc_avg_bill_length_by_sex(data)
    avg_mass_year = calc_avg_body_mass_by_year(data)
    top_island, top_flipper = find_island_with_highest_avg_flipper_length(data)
    results = {}
    for species, avg in avg_mass.items():
        results[f"Average body mass for {species}"] = avg
    for island, percent in percent_male.items():
        results[f"Percent male on {island}"] = percent
    for species, avg in avg_flipper_length.items():
        results[f"Average flipper length for {species}"] = avg
    for sex, avg in avg_bill_length.items():
        results[f"Average bill length for {sex} penguins"] = avg
    for year, avg in avg_mass_year.items():
        results[f"Average body mass in {year}"] = avg
    write_results_to_csv(results)

if __name__ == "__main__":
    main()