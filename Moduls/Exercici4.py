# Exercici 4

# Aquest fitxer està sota una llicència Creative Commons Reconeixement-NoComercial 4.0 Internacional:
# https://creativecommons.org/licenses/by/3.0/es/legalcode.ca

# Crearem les funcions de l'exercici 4

import pandas as pd
import matplotlib.pyplot as plt
import webbrowser as wb
import Moduls.Exercici1 as E1


def time_evolution(df: pd.DataFrame) -> None:
    """
    Funció per representar gràficament l'evolució temporal dels permisos i registres d'armes.

    :param: df (pd.DataFrame): DataFrame amb les dades a analitzar, que inclou la columna 'year' i les columnes
    'permit', 'handgun' i 'long_gun'. :return: None
    """
    df_total = df.groupby(["year"])[["permit", "handgun", "long_gun"]].sum()

    plt.figure(figsize=(12, 6))

    plt.plot(df_total["permit"], label="Permís")
    plt.plot(df_total["handgun"], label="Arma Curta")
    plt.plot(df_total["long_gun"], label="Arma llarga")

    plt.xticks(df_total.index, rotation=45)

    plt.title("Evolució temporal")
    plt.xlabel("anys")
    plt.legend()

    plt.show()


def obrir_comentari(url: str) -> None:
    """
    Funció per obrir una nova pestanya del navegador amb la URL donada.

    :param:
        url (str): URL que es vol obrir en una nova pestanya del navegador.
    :return:
        None
    """
    wb.open_new(url)


def exercici4(df: pd.DataFrame, auto: bool = True) -> None:
    """
    Executa l'exercici 4
    :param:
        df (pd.DataFrame): dataframe de l'exercici 3
        auto (bool): True si volem que la PAC vagi automàtica i False si volem esperar al lector.
    """
    print("A l'Exercici 4 representem l'evolució temporal:")
    E1.continuar(auto)
    # Representar l'evolució temporal
    time_evolution(df)
    print("I obrirem el comentari:")
    E1.continuar(auto)
    # Obrir el comentari
    obrir_comentari("/home/datasci/prog_datasci_2/activities/activity_4/Data/"
                    "Comentari-del-grafic.pdf")
