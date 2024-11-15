# Exercici 2

# Aquest fitxer està sota una llicència Creative Commons Reconeixement-NoComercial 4.0 Internacional:
# https://creativecommons.org/licenses/by/3.0/es/legalcode.ca

# Crearem les funcions de l'exercici 2

import pandas as pd
import Moduls.Exercici1 as E1


def breakdown_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Funció per a descompondre la columna month en any i mes.

    :param:
        df (pd.DataFrame): DataFrame amb la columna month
    :return:
        pd.DataFrame: DataFrame amb les columnes "state", "permit", "handgun", "long_gun", "month", "year"
    :raise:
        AssertionError: No existeix la columna month.
        AssertionError: Month no es str.
    """
    assert "month" in df.columns.tolist(), "No existeix la columna month!"
    assert isinstance(df["month"].str, object), "La columna month no és un str."
    df[["year", "month"]] = df["month"].str.split("-", expand=True)
    df["year"] = df["year"].astype(int)
    df["month"] = df["month"].astype(int)
    df = df[["state", "permit", "handgun", "long_gun", "month", "year"]]
    print(df.head(5))
    return df


def erase_month(df_mes: pd.DataFrame) -> pd.DataFrame:
    """
    Funcio per eliminar el mes del dataframe

    :param:
        df_mes (pd.DataFrame): Dataframe amb les dades.
    :return:
        pd.DataFrame: DataFrame sense la columna month.
    """
    # Eliminar la columna
    df_sense_mes = df_mes.drop(columns=["month"])
    # Imprimir les primeres 5 files
    print(df_sense_mes.head(5))
    # Imprimir la llista de columnes
    print(df_sense_mes.columns.tolist())
    # Retornar el data frame
    return df_sense_mes


def exercici2(df: pd.DataFrame, auto: bool = True) -> pd.DataFrame:
    """
    Executa l'exercici 2
    :param:
        df (pd.DataFrame): dataframe de l'exercici 1
        auto (bool): True si volem que la PAC vagi automàtica i False si volem esperar al lector.
    :return:
    pd.DataFrame: resultat de l'exercici 2
    """
    print("L'Exercici 2 primer trenca la data:")
    E1.continuar(auto)

    firearm_checks = breakdown_date(df)
    print("I esborra el mes:")
    E1.continuar(auto)

    firearm_checks = erase_month(firearm_checks)

    return firearm_checks
