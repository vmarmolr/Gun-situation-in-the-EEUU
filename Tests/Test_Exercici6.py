# Test Exercici 6

# Aquest fitxer està sota una llicència Creative Commons Reconeixement-NoComercial 4.0 Internacional:
# https://creativecommons.org/licenses/by/3.0/es/legalcode.ca

# Testejarem les funcions de l'exercici 6

import unittest
import requests
import os


class TestExercici6(unittest.TestCase):

    def test_choromap_geojson(self):
        """
        Comprova que existeix el directori Output
        :return:
        """
        # Comprovar que existeix el directori de guardat
        self.assertTrue(os.path.exists("/home/datasci/prog_datasci_2/activities/activity_4/Output"))

    def test_exercici6(self):
        """
        Comprova que la url de l'arxiu json no està buida
        :return:
        """
        # Comprovar que existeix el json
        state_geo = "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/us-states.json"
        url = requests.get(state_geo)
        self.assertEqual(url.status_code, 200)

if __name__ == "__main__":
    unittest.main()