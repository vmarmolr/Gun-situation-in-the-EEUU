# Exercici 1

# Aquest fitxer està sota una llicència Creative Commons Reconeixement-NoComercial 4.0 Internacional:
# https://creativecommons.org/licenses/by/3.0/es/legalcode.ca

# Primer crearem les funcions de l'exercici 1

import pandas as pd


def read_csv(url: str) -> pd.DataFrame:
    """
    Funció que llegeix un fitxer .csv des d'una URL en un data frame i mostra les 5 primeres columnes i la seva
    estructura.

    :param:
        url (str): URL del fitxer .csv.
    :return:
        pd.DataFrame: Data frame amb les dades del fitxer .csv.
    """
    # Llegim el fitxer en un data frame
    dades = pd.read_csv(url)
    # Imprimim les primeres 5 columnes
    print(dades.iloc[:, : 5])
    # Imprimim l'estructura
    print(dades.info())
    # Retornem el data frame
    return dades


def clean_csv(joc_dades: pd.DataFrame) -> pd.DataFrame:
    """
    Funció que selecciona les columnes month, state, permit, handgun i long_gun

    :param:
        joc_dades (pd.DataFrame): DataFrame amb les dades
    :return:
        pd.DataFrame: Data frame net amb les columnes que voliem
    """
    # Dades amb les columnes seleccionades
    dades_columnes = joc_dades[['month', 'state', 'permit', 'handgun', 'long_gun']]
    # Imprimir les columnes en llista
    print(dades_columnes.columns.tolist())
    # Retornem el dataframe.
    return dades_columnes


def rename_col(columnes_df: pd.DataFrame) -> pd.DataFrame:
    """
    Funció per a canviar el nom de la columna longgun a long_gun

    :param:
        columnes_df (pd.DataFrame): dataframe amb les dades.
    :return:
        pd.dataframe: Dataframe amb el nom de la columna canviat.
    :raise:
        AssertionError: Si la columna "longgun no existeix al DataFrame.
    """
    assert "longgun" in columnes_df.columns.tolist(), "No existeix la columna longgun!"
    columnes_df = columnes_df.rename(columns={"longgun": "long_gun"})
    print(columnes_df.columns.tolist())
    return columnes_df


def continuar(auto: bool = True) -> None:
    if not auto:
        input("Pitja Enter per continuar")


def exercici1(auto: bool = True) -> pd.DataFrame:
    """
    Executa l'exercici 1.
    :param:
        auto (bool): True si volem que la PAC vagi automàtica i False si volem esperar al lector.
    :return:
        pd.dataframe: Dataframe amb el resultat.
    """
    print("L'Exercici 1 primer llegeix el fitxer:")
    continuar(auto)

    firearm_checks = read_csv("/home/datasci/prog_datasci_2/activities/activity_4/Data/"
                              "nics-firearm-background-checks.csv")
    print("I el neteja")
    continuar(auto)

    firearm_checks = clean_csv(firearm_checks)

    return firearm_checks
