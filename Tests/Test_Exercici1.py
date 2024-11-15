# Test Exercici 1

# Aquest fitxer està sota una llicència Creative Commons Reconeixement-NoComercial 4.0 Internacional:
# https://creativecommons.org/licenses/by/3.0/es/legalcode.ca

# Testejarem les funcions de l'exercici 1

import unittest
import os
import pandas as pd
import Moduls.Exercici1 as E1


class TestExercici1(unittest.TestCase):

    def setUp(self) -> None:
        """
        Crear la taula d'exemple
        :return:
        """
        # Dades Exemple
        data = {
            "month": ["2020-01", "2021-02", "2022-03"],
            'state': ["CA", "TX", "KC"],
            "permit": [123, 456, 789],
            "handgun": [31, 21, 87],
            "longgun": [98, 33, 55],
            "long_gun": [98, 33, 55],
            "extra": ["patates", "i", "dracs"]
        }
        self.df = pd.DataFrame(data)

    def test_read_csv(self):
        """
        Aquest test verifica si el nombre de columnes al DataFrame és superior o igual a 5.
        :return:
        """
        ncol = self.df.shape[1]
        self.assertTrue(ncol >= 5)

    def test_clean_csv(self):
        """
        Aquest test neteja el DataFrame amb la funció clean_csv. A continuació, imprimeix el DataFrame.
        El test comprova que les columnes del DataFrame resultant són exactament
        ['month', 'state', 'permit', 'handgun', 'long_gun']
        :return:
        """
        resultat = E1.clean_csv(self.df)
        print(resultat)
        columnes = ['month', 'state', 'permit', 'handgun', 'long_gun']
        self.assertEqual(resultat.columns.tolist(), columnes)

    def test_rename_col(self):
        """
        Aquest test canvia el nom de la columna "longgun" a "long_gun" amb la funció rename_col.
        Comprova que la columna "longgun" ja no està present i que la columna reanomenada "long_gun" existeix.
        :return:
        """
        # Executem la funció
        resultat = E1.rename_col(self.df)

        # Comprovem que es fa el canvi i que no tenim longgun
        self.assertNotIn("longgun", resultat.columns.tolist())
        self.assertIn("long_gun", resultat.columns.tolist())

    def test_exercici1(self):
        """
        Aquest test verifica si el fitxer de dades d'entrada esperat
        :return:
        """
        self.assertTrue(os.path.isfile("/home/datasci/prog_datasci_2/activities/activity_4/Data/"
                                       "nics-firearm-background-checks.csv"))


if __name__ == "__main__":
    unittest.main()
