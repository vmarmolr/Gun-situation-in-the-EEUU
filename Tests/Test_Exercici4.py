# Test Exercici 4

# Aquest fitxer està sota una llicència Creative Commons Reconeixement-NoComercial 4.0 Internacional:
# https://creativecommons.org/licenses/by/3.0/es/legalcode.ca

# Testejarem les funcions de l'exercici 4

import unittest
from unittest.mock import patch
import pandas as pd
import Moduls.Exercici4 as E4


class TestExercici4(unittest.TestCase):

    def setUp(self) -> None:
        """
        Crear la taula d'exemple
        :return:
        """
        # Dades Exemple
        dades = {
            "state": ["Alabama", "Alaska", "Arizona"],
            "permit": [31205, 34897, 5685],
            "handgun": [34897, 4657, 46377],
            "long_gun": [17850, 3819, 19346],
            "year": [2020, 2021, 2022]
        }
        self.df = pd.DataFrame(dades)

    @patch("matplotlib.pyplot.figure")
    @patch("matplotlib.pyplot.plot")
    @patch("matplotlib.pyplot.xticks")
    @patch("matplotlib.pyplot.title")
    @patch("matplotlib.pyplot.xlabel")
    @patch("matplotlib.pyplot.legend")
    @patch("matplotlib.pyplot.show")
    def test_time_evolution(self,
                            mock_show,
                            mock_legend,
                            mock_xlabel,
                            mock_title,
                            mock_xticks,
                            mock_plot,
                            mock_figure):
        """
        Aquest test comprova el plot de la funció time_evolution.
        Verifica que es crea la figura, que es creen tres plots, i es comproven títols i llegenda.
        :param mock_show:
        :param mock_legend:
        :param mock_xlabel:
        :param mock_title:
        :param mock_xticks:
        :param mock_plot:
        :param mock_figure:
        :return:
        """
        # Executem la funció
        E4.time_evolution(self.df)

        # Crearem la figura
        mock_figure.assert_called_once_with(figsize=(12, 6))

        # Ens assegurem que es criden els 3 plots
        self.assertTrue(mock_plot.call_count, 3)

        # Comprovem els titols i la llegenda
        mock_title.assert_called_once_with("Evolució temporal")
        mock_xlabel.assert_called_once_with("anys")
        mock_legend.assert_called_once()


if __name__ == '__main__':
    unittest.main()
