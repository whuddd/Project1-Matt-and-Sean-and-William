import unittest
from project1code import (
    calc_avg_body_mass_by_species, 
    calc_male_percentage_by_island,
    calc_avg_flipper_length_by_species,
    calc_avg_bill_length_by_sex
)
class TestPenguinAnalysis(unittest.TestCase):

    # William's Test cases

    def test_avg_body_mass_typical(self):
        # Usual case: calculates average for species with valid data.
        data = [
            {'species': 'Adelie', 'body_mass_g': '3700', 'island': 'Torgersen', 'sex': 'male'},
            {'species': 'Adelie', 'body_mass_g': '3800', 'island': 'Torgersen', 'sex': 'female'},
            {'species': 'Chinstrap', 'body_mass_g': '3200', 'island': 'Dream', 'sex': 'male'}
        ]
        self.assertEqual(calc_avg_body_mass_by_species(data), {'Adelie': 3750.0, 'Chinstrap': 3200.0})

    def test_avg_body_mass_multiple_species(self):
        # Usual case: calculates for more than one species.
        data = [
            {'species': 'Gentoo', 'body_mass_g': '5000', 'island': 'Biscoe', 'sex': 'female'},
            {'species': 'Gentoo', 'body_mass_g': '5100', 'island': 'Biscoe', 'sex': 'male'},
            {'species': 'Adelie', 'body_mass_g': '3600', 'island': 'Torgersen', 'sex': 'male'}
        ]
        self.assertEqual(calc_avg_body_mass_by_species(data), {'Gentoo': 5050.0, 'Adelie': 3600.0})

    def test_avg_body_mass_missing_values(self):
        # Edge case: handles missing or 'NA' body mass values.
        data = [
            {'species': 'Adelie', 'body_mass_g': '3700', 'island': 'Torgersen', 'sex': 'male'},
            {'species': 'Adelie', 'body_mass_g': 'NA', 'island': 'Torgersen', 'sex': 'female'},
            {'species': 'Chinstrap', 'body_mass_g': 'NA', 'island': 'Dream', 'sex': 'male'}
        ]
        self.assertEqual(calc_avg_body_mass_by_species(data), {'Adelie': 3700.0})

    def test_avg_body_mass_no_valid_entries(self):
        # Edge case: all input rows lack valid mass (should return empty dict).
        data = [
            {'species': 'Adelie', 'body_mass_g': 'NA', 'island': 'Torgersen', 'sex': 'male'},
            {'species': 'Adelie', 'body_mass_g': '', 'island': 'Torgersen', 'sex': 'female'}
        ]
        self.assertEqual(calc_avg_body_mass_by_species(data), {})

    # Test cases for calc_male_percentage_by_island

    def test_male_percentage_typical(self):
        # Usual case: computes percent male for island with mix.
        data = [
            {'island': 'Dream', 'sex': 'male'},
            {'island': 'Dream', 'sex': 'female'},
            {'island': 'Dream', 'sex': 'male'}
        ]
        result = calc_male_percentage_by_island(data)
        self.assertAlmostEqual(result['Dream'], 66.66666666666666, places=4)

    def test_male_percentage_multiple_islands(self):
        # Usual case: computes percent male for multiple islands.
        data = [
            {'island': 'Biscoe', 'sex': 'male'},
            {'island': 'Biscoe', 'sex': 'male'},
            {'island': 'Torgersen', 'sex': 'female'},
            {'island': 'Torgersen', 'sex': 'male'}
        ]
        out = calc_male_percentage_by_island(data)
        self.assertAlmostEqual(out['Biscoe'], 100.0, places=2)
        self.assertAlmostEqual(out['Torgersen'], 50.0, places=2)

    def test_male_percentage_na_sex(self):
        # Edge case: handles 'NA' in sex column, excludes from percent calculation.
        data = [
            {'island': 'Biscoe', 'sex': 'male'},
            {'island': 'Biscoe', 'sex': 'NA'},
            {'island': 'Biscoe', 'sex': 'female'}
        ]
        result = calc_male_percentage_by_island(data)
        self.assertAlmostEqual(result['Biscoe'], 50.0, places=2)

    def test_male_percentage_all_female(self):
        # Edge case: island with only females (should yield 0%).
        data = [
            {'island': 'Torgersen', 'sex': 'female'},
            {'island': 'Torgersen', 'sex': 'female'}
        ]
        result = calc_male_percentage_by_island(data)
        self.assertAlmostEqual(result['Torgersen'], 0.0, places=2)



    # Sean's Test Cases
    def test_avg_flipper_length_typical(self):
        # Usual case: calculates average flipper length across multiple species.
        data = [
            {'species': 'Adelie', 'flipper_length_mm': '189', 'sex': 'male'},
            {'species': 'Adelie', 'flipper_length_mm': '191', 'sex': 'female'},
            {'species': 'Gentoo', 'flipper_length_mm': '220', 'sex': 'male'}
        ]
        self.assertEqual(calc_avg_flipper_length_by_species(data), {'Adelie': 190.0, 'Gentoo': 220.0})

    def test_avg_flipper_length_single_species(self):
        # Usual case: calculates average flipper length for a single species.
        data = [
            {'species': 'Chinstrap', 'flipper_length_mm': '200', 'sex': 'male'},
            {'species': 'Chinstrap', 'flipper_length_mm': '202', 'sex': 'female'},
        ]
        self.assertEqual(calc_avg_flipper_length_by_species(data), {'Chinstrap': 201.0})

    def test_avg_flipper_length_missing_values(self):
        # Edge case: handles missing or empty flipper length values, excluding them.
        data = [
            {'species': 'Adelie', 'flipper_length_mm': '195', 'sex': 'male'},
            {'species': 'Adelie', 'flipper_length_mm': 'NA', 'sex': 'female'},
            {'species': 'Gentoo', 'flipper_length_mm': '', 'sex': 'male'}
        ]
        self.assertEqual(calc_avg_flipper_length_by_species(data), {'Adelie': 195.0})

    def test_avg_flipper_length_no_valid_entries(self):
        # Edge case: returns an empty dictionary if no entries have valid flipper lengths.
        data = [
            {'species': 'Adelie', 'flipper_length_mm': 'NA', 'sex': 'male'},
            {'species': 'Adelie', 'flipper_length_mm': '', 'sex': 'female'}
        ]
        self.assertEqual(calc_avg_flipper_length_by_species(data), {})
    def test_avg_bill_length_typical(self):
        # Usual case: calculates average bill length for both male and female penguins.
        data = [
            {'sex': 'male', 'bill_length_mm': '40.9', 'species': 'Adelie'},
            {'sex': 'female', 'bill_length_mm': '37.8', 'species': 'Adelie'},
            {'sex': 'male', 'bill_length_mm': '41.1', 'species': 'Adelie'}
        ]
        result = calc_avg_bill_length_by_sex(data)
        self.assertAlmostEqual(result['male'], 41.0)
        self.assertAlmostEqual(result['female'], 37.8)

    def test_avg_bill_length_one_sex(self):
        # Usual case: correctly calculates average when only one sex is present.
        data = [
            {'sex': 'female', 'bill_length_mm': '38.1', 'species': 'Adelie'},
            {'sex': 'female', 'bill_length_mm': '38.3', 'species': 'Adelie'}
        ]
        self.assertEqual(calc_avg_bill_length_by_sex(data), {'female': 38.2})

    def test_avg_bill_length_missing_value(self):
        # Edge case: ignores entries with 'NA' for bill length.
        data = [
            {'sex': 'male', 'bill_length_mm': '42.0', 'species': 'Adelie'},
            {'sex': 'male', 'bill_length_mm': 'NA', 'species': 'Adelie'},
            {'sex': 'female', 'bill_length_mm': '36.0', 'species': 'Adelie'}
        ]
        self.assertEqual(calc_avg_bill_length_by_sex(data), {'male': 42.0, 'female': 36.0})

    def test_avg_bill_length_invalid_sex(self):
        # Edge case: ignores entries where sex is not 'male' or 'female'
        data = [
            {'sex': 'male', 'bill_length_mm': '45.0', 'species': 'Adelie'},
            {'sex': 'NA', 'bill_length_mm': '50.0', 'species': 'Gentoo'},
            {'sex': '.', 'bill_length_mm': '51.0', 'species': 'Chinstrap'},
            {'sex': 'female', 'bill_length_mm': '35.0', 'species': 'Adelie'}
        ]
        self.assertEqual(calc_avg_bill_length_by_sex(data), {'male': 45.0, 'female': 35.0})
if __name__ == '__main__':
    unittest.main(verbosity=2)
