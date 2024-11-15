# Exercici 3

# Aquest fitxer està sota una llicència Creative Commons Reconeixement-NoComercial 4.0 Internacional:
# https://creativecommons.org/licenses/by/3.0/es/legalcode.ca

# Crearem les funcions de l'exercici 2

import pandas as pd
import Moduls.Exercici1 as E1


def groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Funcio per agrupar les dades per any i estat i sumar les columnes 'permit', 'handgun' i 'long_gun'.

    :param: df (pd.DataFrame): DataFrame amb les dades a agrupar. :return: pd.DataFrame: DataFrame amb les dades
    agrupades per any i estat amb les sumes de 'permit', 'handgun' i 'long_gun'.
    """
    df_agrupat = df.groupby(["year", "state"])[["permit", "handgun", "long_gun"]].sum()
    print(df_agrupat.head(), "\n")
    return df_agrupat


def print_biggest_handguns(df: pd.DataFrame) -> None:
    """
    Funcio per imprimir la informacio sobre l'any i estat amb el nombre mes gran d'armes curtes ('handgun').

    :param:
        df (pd.DataFrame): DataFrame amb les dades a analitzar.
    :return:
        None
    """
    max_pistoles = df["handgun"].idxmax()
    print("L'any",
          max_pistoles[0],
          "a l'estat",
          max_pistoles[1],
          "es va registrar el nombre més gran d'armes curtes:",
          df["handgun"].max())


def print_biggest_longguns(df: pd.DataFrame) -> None:
    """
    Funcio per imprimir la informacio sobre l'any i estat amb el nombre mes gran d'armes llargues ('long_gun').

    :param:
        df (pd.DataFrame): DataFrame amb les dades a analitzar.
    :return:
        None
    """
    max_llargues = df["long_gun"].idxmax()
    print("L'any",
          max_llargues[0],
          "a l'estat",
          max_llargues[1],
          "es va registrar el nombre més gran d'armes llargues:",
          df["long_gun"].max())


def exercici3(df: pd.DataFrame, auto: bool = True) -> pd.DataFrame:
    """
    Executa l'exercici 3
    :param:
        df (pd.DataFrame): dataframe de l'exercici 2
        auto (bool): True si volem que la PAC vagi automàtica i False si volem esperar al lector.
    :return:
    pd.DataFrame: resultat de l'exercici 3
    """
    print("L'Exercici 3 primer fa el groupby:")
    E1.continuar(auto)
    # Fer el groupby de les dades
    firearm_checks = groupby_state_and_year(df)
    # Imprimir les armes curtes més altes
    print("Ara imprimirem el major nombre d'armes curtes:")
    E1.continuar(auto)

    print_biggest_handguns(firearm_checks)
    # Imprimir les armes llargues més altes
    print("I el nombre més gran d'armes llargues:")
    E1.continuar(auto)
    print_biggest_longguns(firearm_checks)
    return firearm_checks
