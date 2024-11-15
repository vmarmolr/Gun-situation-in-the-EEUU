# Test Exercici 5

# Aquest fitxer està sota una llicència Creative Commons Reconeixement-NoComercial 4.0 Internacional:
# https://creativecommons.org/licenses/by/3.0/es/legalcode.ca

# Testejarem les funcions de l'exercici 5

import unittest
import pandas as pd
import Moduls.Exercici5 as E5


class TestExercici5(unittest.TestCase):

    def setUp(self) -> None:
        """
        Crear les taules d'exemple
        :return:
        """
        # Dades Exemple
        dades = {
            "state": ["Alabama", "Alabama", "California", "Guam"],
            "permit": [100, 200, 150, 400],
            "handgun": [200, 200, 125, 700],
            "long_gun": [300, 200, 100, 200],
            "year": [2020, 2021, 2022, 2022]
        }
        self.df1 = pd.DataFrame(dades)

        dades = {
            "state": ["Alabama", "Alaska", "California"],
            "permit": [100, 200, 150],
            "handgun": [200, 200, 125],
            "long_gun": [300, 200, 100],
            "year": [2020, 2021, 2022],
            "pop_2014": [120000, 120000, 32000]
        }
        self.df2 = pd.DataFrame(dades)

    def test_groupby_state(self):
        """
        Comprova si la funció groupby_state agrupa correctament el DataFrame per estat i suma les columnes
        "permit", "handgun" i "long_gun".
        Compara el resultat amb un DataFrame esperat.
        :return:
        """
        # Apliquem la funció
        df_estat = E5.groupby_state(self.df1)

        # Crearem el dataframe amb el resultat
        resultat = {
            "state": ["Alabama", "California", "Guam"],
            "permit": [300, 150, 400],
            "handgun": [400, 125, 700],
            "long_gun": [500, 100, 200]
        }
        df_resultat = pd.DataFrame(resultat)
        # Comprovem si son iguals
        self.assertTrue(df_resultat.equals(df_estat))

    def test_clean_states(self):
        """
        Verifica que la funció clean_states elimina les files amb l'estat "Guam" del DataFrame.
         Assegura que els altres estats continuen presents.
        :return:
        """
        df_depurat = E5.clean_states(self.df1)

        # Comprovar que els valors eliminats no estan i que els no eliminats si
        self.assertNotIn("Guam", df_depurat["state"].to_list())
        self.assertIn("Alabama", df_depurat["state"].to_list())

    def test_merge_datasets(self):
        """
        Unifica el DataFrame original amb un DataFrame de població basat en l'estat.
        Compara el resultat amb un DataFrame esperat que conté les dades i la població de 2014.
        :return:
        """
        # Taula de població per agrupar
        poblacio = {
            "state": ["Alabama", "California"],
            "pop_2014": [120000, 32000]
        }
        poblacio = pd.DataFrame(poblacio)

        # Executem la funcio
        df_agrupat = E5.merge_datasets(self.df1, poblacio)

        # Taula que hauria de ser el resultat
        df_resultat = {
            "state": ["Alabama", "Alabama", "California"],
            "permit": [100, 200, 150],
            "handgun": [200, 200, 125],
            "long_gun": [300, 200, 100],
            "year": [2020, 2021, 2022],
            "pop_2014": [120000, 120000, 32000]
        }
        df_resultat = pd.DataFrame(df_resultat)

        # Comprovem que son iguals
        self.assertTrue(df_agrupat.equals(df_resultat))

    def test_calculate_relative_values(self):
        """
        Afegeix els valors relatius de les tres mesures.
        Comprova si les noves columnes s'han afegit i si els valors calculats són correctes.
        :return:
        """
        # Creem la funcio
        df_relatius = E5.calculate_relative_values(self.df2)
        print(df_relatius)
        # Comprovem que es correcte
        self.assertTrue(df_relatius.equals(self.df2))
        self.assertIn("permit_perc", df_relatius.columns)
        self.assertIn("longgun_perc", df_relatius.columns)
        self.assertIn("handgun_perc", df_relatius.columns)
        self.assertEqual(100 * 100 / 120000, df_relatius.iloc[0]["permit_perc"])
        self.assertEqual(100 * 200 / 120000, df_relatius.iloc[0]["handgun_perc"])
        self.assertEqual(100 * 300 / 120000, df_relatius.iloc[0]["longgun_perc"])


if __name__ == "__main__":
    unittest.main()
