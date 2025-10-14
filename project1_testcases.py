import unittest
from project1code import calc_avg_body_mass_by_species, calc_male_percentage_by_island

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

if __name__ == '__main__':
    unittest.main(verbosity=2)
