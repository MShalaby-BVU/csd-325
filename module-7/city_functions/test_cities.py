from city_functions import citystring
import unittest


class TestCityString(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(citystring("Madrid" , "Spain") , "Madrid, Spain")


if __name__ == "__main__":
    unittest.main()
