# Test Exercici 3

# Aquest fitxer està sota una llicència Creative Commons Reconeixement-NoComercial 4.0 Internacional:
# https://creativecommons.org/licenses/by/3.0/es/legalcode.ca

# Testejarem les funcions de l'exercici 3

import unittest
import pandas as pd
import Moduls.Exercici3 as E3


class TestExercici3(unittest.TestCase):

    def setUp(self) -> None:
        """
        Crear la taula d'exemple
        :return:
        """
        # Dades Exemple
        dades = {
            'state': ["Alabama", "Alaska", "Arizona"],
            "permit": [31205, 34897, 5685],
            "handgun": [34897, 4657, 46377],
            "long_gun": [17850, 3819, 19346],
            "year": [2020, 2021, 2022]
        }
        self.df = pd.DataFrame(dades)

    def test_groupby_state_and_year(self):
        """
        Aquest test comprova que el DataFrame després d'aplicar la funció groupby_state_and_year només conté les columnes:
        "permit", "handgun" i "long_gun".
        :return:
        """
        df_agrupat = E3.groupby_state_and_year(self.df)

        # Comprovem les columnes
        columnes = ["permit", "handgun", "long_gun"]
        self.assertEqual(df_agrupat.columns.tolist(), columnes)


if __name__ == "__main__":
    unittest.main()
