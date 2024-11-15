# Exercici 6

# Aquest fitxer està sota una llicència Creative Commons Reconeixement-NoComercial 4.0 Internacional:
# https://creativecommons.org/licenses/by/3.0/es/legalcode.ca

# Crearem les funcions de l'exercici 6

import folium
import pandas as pd
import Moduls.Exercici4 as E4
import Moduls.Exercici1 as E1


def choromap_geojson(df: pd.DataFrame,
                     columnes: list,
                     nom_llegenda: str,
                     url_json: str,
                     color: str = "YlOrRd",
                     nom_mapa: str = "Mapa") -> None:
    """
    Funció per crear un mapa coroplètic interactiu amb dades geogràfiques i valors associats.

    :param:
        df (pd.DataFrame): DataFrame amb les dades a visualitzar en el mapa.
        columnes (list): Llista de les columnes del DataFrame a utilitzar per a la visualització.
        nom_llegenda (str): Nom de la llegenda del mapa.
        url_json (str): URL o ruta del fitxer GeoJSON que conté les dades geogràfiques per fer la visualització.
        color (str, opcional): Paleta de colors per omplir les àrees del mapa (per defecte és "YlOrRd").
        nom_mapa (str, opcional): Nom del fitxer HTML de sortida del mapa (per defecte és "Mapa").

    :return:
        None
    """
    m = folium.Map(location=[40, -95], zoom_start=4)
    folium.Choropleth(
        geo_data=url_json,
        data=df,
        columns=columnes,
        key_on="feature.id",
        fill_color=color,
        legend_name=nom_llegenda
    ).add_to(m)

    folium.LayerControl().add_to(m)

    m.save(f"/home/datasci/prog_datasci_2/activities/activity_4/Output/{nom_mapa}.html")


def exercici6(df: pd.DataFrame, auto: bool = True) -> None:
    """
    Executa l'exercici 6
    :param:
        df (pd.DataFrame): dataframe de l'exercici 5
        auto (bool): True si volem que la PAC vagi automàtica i False si volem esperar al lector.
    :return:
    pd.DataFrame: resultat de l'exercici 6
    """
    # Extraiem l'url on es troba el fitxer json.
    state_geo = "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/us-states.json"

    # Posem els noms dels fitxers on es guardaran els mapes
    nom_m1 = "mapa_llicencies"
    nom_m2 = "mapa_llargues"
    nom_m3 = "mapa_pistoles"

    # Crearem els tres mapes
    choromap_geojson(df,
                     ["code", "permit_perc"],
                     "permisos",
                     state_geo,
                     color="Oranges",
                     nom_mapa=nom_m1)
    choromap_geojson(df,
                     ["code", "longgun_perc"],
                     "Armes llargues",
                     state_geo,
                     color="PuRd",
                     nom_mapa=nom_m2)
    choromap_geojson(df,
                     ["code", "handgun_perc"],
                     "Armes curtes",
                     state_geo,
                     nom_mapa=nom_m3)

    # Visualitzem els mapes:
    print("Veiem el primer mapa:")
    E1.continuar(auto)
    E4.obrir_comentari(f"/home/datasci/prog_datasci_2/activities/activity_4/Output/{nom_m1}.html")
    print("Veiem el segon:")
    E1.continuar(auto)
    E4.obrir_comentari(f"/home/datasci/prog_datasci_2/activities/activity_4/Output/{nom_m2}.html")
    print("Veiem el tercer:")
    E1.continuar(auto)
    E4.obrir_comentari(f"/home/datasci/prog_datasci_2/activities/activity_4/Output/{nom_m3}.html")
