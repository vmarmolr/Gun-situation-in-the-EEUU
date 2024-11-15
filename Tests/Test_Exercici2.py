# Test Exercici 2

# Aquest fitxer està sota una llicència Creative Commons Reconeixement-NoComercial 4.0 Internacional:
# https://creativecommons.org/licenses/by/3.0/es/legalcode.ca

# Testejarem les funcions de l'exercici 2

import unittest
import pandas as pd
import Moduls.Exercici2 as E2


class TestExercici2(unittest.TestCase):

    def setUp(self) -> None:
        """
        Crear la taula d'exemple
        :return:
        """
        # Dades Exemple
        dades = {
            "month": ["2020-01", "2021-02", "2022-03"],
            'state': ["Alabama", "Alaska", "Arizona"],
            "permit": [31205, 34897, 5685],
            "handgun": [34897, 4657, 46377],
            "long_gun": [17850, 3819, 19346],
        }
        self.df = pd.DataFrame(dades)

    def test_breakdown_date(self):
        """
        Aquest test verifica la funció E2.breakdown_date, que extreu informació de l'any i el mes de la columna "month".
        Comprova si es creen noves columnes anomenades "year" i "month" al DataFrame.
        Confirma que els tipus de dades d'aquestes noves columnes són enters.
        :return:
        """
        df_mes = E2.breakdown_date(self.df)

        # Comprovem que s'han creat les columnes correctament
        self.assertIn("year", df_mes.columns)
        self.assertIn("month", df_mes.columns)

        # Comprovem el tipus de dada
        self.assertEqual(df_mes["year"].dtype, int)
        self.assertEqual(df_mes["month"].dtype, int)

    def test_erase_month(self):
        """
        Aquest test comprova que la columna "month" ja no està present després d'aplicar la funció erase_month.
        :return:
        """
        df_mes = E2.erase_month(self.df)

        # Comprovem que s'elimina el mes
        self.assertNotIn("month", df_mes.columns)


if __name__ == "__main__":
    unittest.main()
