# Exercici 5

# Aquest fitxer està sota una llicència Creative Commons Reconeixement-NoComercial 4.0 Internacional:
# https://creativecommons.org/licenses/by/3.0/es/legalcode.ca

# Crearem les funcions de l'exercici 5

import pandas as pd
import Moduls.Exercici1 as E1


def groupby_state(df: pd.DataFrame) -> pd.DataFrame:
    """
    Funció per agrupar les dades per estat i sumar les columnes 'permit', 'handgun' i 'long_gun'.

    :param:
        df (pd.DataFrame): DataFrame amb les dades a analitzar.
    :return:
        pd.DataFrame: DataFrame amb les dades agrupades per estat amb les sumes de 'permit', 'handgun' i 'long_gun'.
    """
    df_estat = df.groupby(["state"])[["permit", "handgun", "long_gun"]].sum().reset_index()
    print(df_estat.head(5))
    return df_estat


def clean_states(df: pd.DataFrame) -> pd.DataFrame:
    """
    Funció per netejar el DataFrame eliminant certos estats especificats.

    :param: df (pd.DataFrame): DataFrame original amb la columna 'state'. :return: pd.DataFrame: DataFrame depurat
    sense els estats especificats ('Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands').
    """
    print("Nombre de valors abans d'eliminar els estats:", len(df["state"]))
    estats_no = ["Guam", "Mariana Islands", "Puerto Rico", "Virgin Islands"]
    llista_estats_no = [(estat, estat in df.values) for estat in estats_no]
    estats_eliminar = [tupla[0] for tupla in llista_estats_no if tupla[1] is True]
    df_depurat = df[~df["state"].isin(estats_eliminar)]
    print("Nombre de valors despres d'eliminar els estats:", len(df_depurat["state"]))
    return df_depurat


def merge_datasets(df_exercici: pd.DataFrame, df_nou: pd.DataFrame) -> pd.DataFrame:
    """
    Funció per fusionar dos DataFrames basats en la columna 'state'.

    :param:
        df_exercici (pd.DataFrame): Primer DataFrame a fusionar.
        df_nou (pd.DataFrame): Segon DataFrame a fusionar.
    :return:
        pd.DataFrame: DataFrame resultat de la fusió basada en la columna 'state'.
    """
    df_agrupat = pd.merge(df_exercici, df_nou, on="state")
    print(df_agrupat.head())
    return df_agrupat


def calculate_relative_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Funció per calcular valors percentuals relatius respecte a una població específica.

    :param: df (pd.DataFrame): DataFrame amb les dades que inclouen les columnes 'permit', 'handgun', 'long_gun' i
    'pop_2014'. :return: pd.DataFrame: DataFrame amb les noves columnes 'permit_perc', 'handgun_perc' i
    'longgun_perc' que representen els valors percentuals relatius respecte a 'pop_2014'.
    """
    df["permit_perc"] = (100 * df["permit"])/df["pop_2014"]
    df["longgun_perc"] = (100 * df["long_gun"]) / df["pop_2014"]
    df["handgun_perc"] = (100 * df["handgun"]) / df["pop_2014"]
    return df


def exercici5(df: pd.DataFrame, auto: bool = True) -> pd.DataFrame:
    """
    Executa l'exercici 5
    :param:
        df (pd.DataFrame): dataframe de l'exercici 3
        auto (bool): True si volem que la PAC vagi automàtica i False si volem esperar al lector.
    :return:
    pd.DataFrame: resultat de l'exercici 5
    """
    print("L'Exercici 5 comença agrupant les dades per estat:")
    E1.continuar(auto)
    # Fem el groupby
    firearm_checks = groupby_state(df)
    print("Traiem els estats dels que no tenim dades:")
    E1.continuar(auto)
    firearm_checks = clean_states(firearm_checks)
    print("Ara agruparem els dos jocs de dades: ")
    E1.continuar(auto)
    # Llegim el fitxer .csv
    populations = E1.read_csv("/home/datasci/prog_datasci_2/activities/activity_4/Data/us-state-populations.csv")
    # Agrupem les dades
    dades_agrupades = merge_datasets(firearm_checks, populations)
    # Calculem els valors relatius
    dades_agrupades = calculate_relative_values(dades_agrupades)

    print("Calcularem la mitjana:")
    E1.continuar(auto)
    # Calculem la mitjana
    mitjana_permisos = dades_agrupades["permit_perc"].mean()
    print("mitjana de permisos:", mitjana_permisos.round(2))

    # Mostrem totes les columnes de l'estat de Kentucky
    print("Mostrarem la informació de Kentucky")
    E1.continuar(auto)
    pd.set_option('display.max_columns', None)
    print("Informació de Kentucky:\n", dades_agrupades[dades_agrupades["state"] == "Kentucky"])
    print("Assignarem a l'estat de Kentucky la mitjana calculada")
    E1.continuar(auto)
    # Assignem a l'estat de Kentucky la mitjana calculada anteriorment
    dades_agrupades.loc[dades_agrupades["state"] == "Kentucky", "permit_perc"] = mitjana_permisos
    # Tornem a calcular la mitjana
    print("Calculem la nova mitjana")
    E1.continuar(auto)
    nova_mitjana_permisos = dades_agrupades["permit_perc"].mean()
    print("mitjana de permisos:", nova_mitjana_permisos.round(2), "\n")
    # Fem el comentari del resultat
    print("Veiem el comentari")
    E1.continuar(auto)
    print("El valor ha canviat molt, entenc el procès de treure valors atipics.\nConsidero que amb aquest procès "
          "obtenim un valor més alt que el de la mitjana, però\nno tant disparatat com per a que les nostres anàlisis "
          "siguin erronees.\n")
    # retornem el dataframe dades_agrupades
    return dades_agrupades
