
# Projecte Final

Aquesta és la pràctica final de l'assignatura de programació per a la
ciència de dades de la Universitat Oberta de Catalunya.

Les instruccions d'aquest projecte es troben a la carpeta Enunciat/ on
podem trobar el pdf en Català i en Castellà.

## Taula de continguts

 - [Directori](#Directori)
 - [Requeriments](#Requeriments)
 - [Executar](#Executar)
 - [Exercicis](#Exercicis)
 - [Main](#Main)
 - [Tests](#Tests)
 - [Llicencia](#Llicencia)
 - [Contacte](#Contacte)

## Directori

+ activity_4
|_ + Data
   |_ Comentari-del-grafic.pdf
   |_ nics-firearm-background-checks.csv
   |_ us-state-populations.csv
|_ + Enunciat
   |_ + pdf
      |_ CAT-PEC4-enun.pdf
      |_ ES-PEC4-enun.pdf
   |_ CAT-PEC4-enun.ipynb
   |_ ES-PEC4-enun.ipynb
|_ + Moduls
   |_ Exercici1.py
   |_ Exercici2.py
   |_ Exercici3.py
   |_ Exercici4.py
   |_ Exercici5.py
   |_ Exercici6.py
|_ + Output
   |_ mapa_llargues.html
   |_ mapa_llicencies.html
   |_ mapa_pistoles.html
|_ + Tests
   |_ Test_Exercici1.py
   |_ Test_Exercici2.py
   |_ Test_Exercici3.py
   |_ Test_Exercici4.py
   |_ Test_Exercici5.py
   |_ Test_Exercici6.py
|_ __init__.py
|_ main.py
|_ README.txt
|_ requeriments.txt
|_ LICENSE.txt

## Requeriments

### Requeriments dels exercicis:

 - pandas
 - matplotlib.pyplot
 - webbrowser
 - folium

### Requeriments dels tests:

 - unittest
 - os
 - pandas
 - matplotlib.pyplot
 - requests
 - from unittest.mock import patch

## Executar

Per a fer anar el codi s'ha d'executar l'arxiu main amb l'script:

python3 main.py

Aquest executarà tota la pràctica seguida, com s'indica a l'enunciat.
Ara bé, una vegada executada tota la pràctica tindrem un menú esperant una resposta:

 * Si es vol executar la pràctica una altra vegada tota sencera, llavors haurem de pitjar 0.
A aquesta opció li direm opció per defecte.
 * Si es vol executar la pràctica apartat per apartat, pitjarem l'1. Si anem pitjant Enter la
pràctica avançarà. Sempre la pràctica s'aturarà en un print on dirà què passarà quan es
pitgi l'Enter.
 * Si es vol sortir de la pràctica haurem de pitjar qualsevol botó.

Veurem que la pràctica obrirà un plot, un pdf i tres mapes.

Pel que fa als tests:
Si els volem executar s'haurà de fer d'un en un. Tenim un test per exercici.
Per exemple, si volem fer els tests per a l'exercici 1, hem d'executar l'script següent:

python3 Test_Exercici1.py

En referència a la cobertura:

Des del directori del projecte hem d'executar la instrucció:

coverage run --omit="/usr/*" -m unittest discover -s Tests -p "Test_*.py"

A la terminal. Seguit de:

coverage report -m

per a fer un informe i llegir-lo podem executar:

coverage html

Que ens generarà un informe en html per a visualitzar-lo amb claredat.
Se'ns generarà la carpeta htmlcov i per llegir-lo només caldrà la instrucció:

open htmlcov/index.html

En el nostre cas podem veure que tenim una cobertura de tot el projecte del 72%.
Idealment, voldríem que la cobertura fos la més alta possible.
Cal destacar que encara podem millorar els tests sobretot per a l'Exercici3 i l'Exercici5 que tenen cobertures de menys del 50%.
Malgrat tot, per motius personals no m'ha estat possible invertir més temps en la pràctica i espero que hagi aconseguit demostrar
els coneixements obtinguts en aquesta assignatura.

Aprofito aquest espai per agrair el vostre temps i la vostra dedicació i, aprofitant l'avinentesa, desitjar-vos un bon estiu.

## Exercicis

Explicarem els exercicis un a un.

### Exercici 1

Aquest exercici demostra com llegir un conjunt de dades CSV i modificar el nom d'una columna

Objectius:

 * Llegir un fitxer CSV des d'una URL.
 * Mostrar les primeres 5 columnes i la seva estructura.
 * Seleccionar les columnes rellevants per a l'anàlisi.
 * Canviar el nom d'una columna.

Funcions:

 * read_csv(url: str) -> pd.DataFrame: Llegeix un fitxer CSV des d'una URL i retorna un data frame.
 * clean_csv(joc_dades: pd.DataFrame) -> pd.DataFrame: Selecciona les columnes desitjades i retorna un data frame net.
 * rename_col(columnes_df: pd.DataFrame) -> pd.DataFrame: Canvia el nom de la columna "longgun" a "long_gun".
 * continuar(auto: bool = True) -> None: Atura la pràctica fins que es pitgi enter si auto és False.
 * exercici1(auto: bool = True) -> pd.DataFrame: Executa l'exercici 1 i retorna un data frame amb el resultat. Si
 auto es True no s'atura si és False si.

Input:

 * nics-firearm-background-checks.csv

### Exercici 2

Separa la columna month i es queda amb l'any.

Objectius:

 * Descompondre la columna "month" en columnes separades per a l'any i el mes.
 * Eliminar la columna "month".

Funcions:

 * breakdown_date(df: pd.DataFrame) -> pd.DataFrame: Descompon la columna "month" i retorna un data frame amb columnes "year" i "month".
 * erase_month(df_mes: pd.DataFrame) -> pd.DataFrame: Elimina la columna "month" i retorna un data frame.
 * exercici2(df: pd.DataFrame, auto: bool = True) -> pd.DataFrame: Executa l'exercici 2 i retorna un data frame amb el resultat. Si
 auto es True no s'atura si és False si.

### Exercici 3

Fa un groupby de les dades i mostra l'any i estat amb més nombre d'armes curtes i llargues.

Objectius:

 * Agrupar les dades per any i estat.
 * Sumar les columnes "permit", "handgun" i "long_gun".
 * Identificar l'any i l'estat amb el nombre més gran d'armes curtes.
 * Identificar l'any i l'estat amb el nombre més gran d'armes llargues.

Funcions:

 * groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame: Agrupa les dades per any i estat i retorna un data frame amb les sumes de "permit", "handgun" i "long_gun".
 * print_biggest_handguns(df: pd.DataFrame) -> None: Imprimeix la informació sobre l'any i l'estat amb el nombre més gran d'armes curtes ("handgun").
 * print_biggest_longguns(df: pd.DataFrame) -> None: Imprimeix la informació sobre l'any i l'estat amb el nombre més gran d'armes llargues ("long_gun").
 * exercici3(df: pd.DataFrame, auto: bool = True) -> pd.DataFrame: Executa l'exercici 3 i retorna un data frame amb el resultat. Si
 auto es True no s'atura si és False si.

### Exercici 4

Crea una gràfica del group by i obre el comentari en pdf.

Objectius:

 * Crear una gràfica que mostri el nombre de permisos, armes curtes ("handgun") i armes llargues ("long_gun") per any.
 * Obrir un comentari en format PDF amb explicacions addicionals sobre la gràfica.

Funcions:

 * time_evolution(df: pd.DataFrame) -> None: Crea una gràfica de l'evolució temporal dels permisos i registres d'armes.
 * obrir_comentari(url: str) -> None: Obre una nova pestanya del navegador amb la URL especificada.
 * exercici4(df: pd.DataFrame, auto: bool = True) -> None: Executa l'exercici 4 i mostra la gràfica i el comentari. Si
 auto es True no s'atura si és False si.

Input:

 * Comentari-del-grafic.pdf

### Exercici 5

Fer un groupby per estats i eliminar outliers substituint-los per valors més adients.

Objectius:

 * Agrupar les dades per estat.
 * Eliminar certs estats.
 * Agrupar les dades amb un conjunt de dades de població per estat.
 * Calcular valors percentuals relatius de permisos i registres d'armes per població.

Funcions:

 * groupby_state(df: pd.DataFrame) -> pd.DataFrame: Agrupa les dades per estat i suma les columnes "permit", "handgun" i "long_gun".
 * clean_states(df: pd.DataFrame) -> pd.DataFrame: Elimina certs estats especificats del DataFrame.
 * merge_datasets(df_exercici: pd.DataFrame, df_nou: pd.DataFrame) -> pd.DataFrame: Fusiona dos DataFrames basats en la columna "state".
 * calculate_relative_values(df: pd.DataFrame) -> pd.DataFrame: Calcula valors percentuals relatius respecte a la població.
 * exercici5(df: pd.DataFrame, auto: bool = True) -> pd.DataFrame: Executa l'exercici 5 i retorna el DataFrame amb els resultats. Si
 auto és True no s'atura si és False si.

Input:

 * us-state-populations.csv

### Exercici 6

Crear tres mapes per a les tres mètriques que volem.

Objectius:

 * Crear un mapa per a cada tipus de registre d'armes: permisos, armes llargues i armes curtes.
 * Representar la proporció de registres d'armes o llicències per població en cada estat.
 * Utilitzar colors i llegendes per a una visualització clara i útil.

Funcions:

choromap_geojson(df: pd.DataFrame,
                 columnes: list,
                 nom_llegenda: str,
                 url_json: str,
                 color: str = "YlOrRd",
                 nom_mapa: str = "Mapa") -> None: Crea un mapa coroplètic amb dades geogràfiques i valors associats.

Input:

 * https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/us-states.json

Output:

 * /home/datasci/prog_datasci_2/activities/activity_4/Output/mapa_llargues.html
 * /home/datasci/prog_datasci_2/activities/activity_4/Output/mapa_llicencies.html
 * /home/datasci/prog_datasci_2/activities/activity_4/Output/mapa_pistoles.html

## Main

Aquest script permet executar la pràctica completa.

Funcions:

 * practica_sencera(auto: bool = True) -> None: Executa tots els exercicis de la pràctica de manera seqüencial.
 * main() -> None: Mostra a l'usuari per seleccionar si vol executar la pràctica completa o els apartats de manera individual.

## Tests

Tenim un test per exercici:

### Test_Exercici1

 * test_read_csv: Aquest test verifica si el nombre de columnes al DataFrame és superior o igual a 5.

 * test_clean_csv: Aquest test neteja el DataFrame amb la funció clean_csv. A continuació, imprimeix el DataFrame.
 El test comprova que les columnes del DataFrame resultant són exactament ['month', 'state', 'permit', 'handgun', 'long_gun'].

 * test_rename_col:
 Aquest test canvia el nom de la columna "longgun" a "long_gun" amb la funció rename_col. Comprova que la columna "longgun" ja no està present
 i que la columna reanomenada "long_gun" existeix al DataFrame.

 * test_exercici1: Aquest test verifica si el fitxer de dades d'entrada esperat:
  "/home/datasci/prog_datasci_2/activities/activity_4/Data/nics-firearm-background-checks.csv" existeix.

### Test_Exercici2

 * test_breakdown_date: Aquest test verifica la funció E2.breakdown_date, que extreu informació de l'any i el mes de la columna "month".
 Comprova si es creen noves columnes anomenades "year" i "month" al DataFrame i  confirma que els tipus de dades d'aquestes noves columnes són enters.

 * test_erase_month: Aquest test comprova que la columna "month" ja no està present després d'aplicar la funció erase_month.

### Test_Exercici3

 * test_groupby_state_and_year: Aquest test comprova que el DataFrame després d'aplicar la funció groupby_state_and_year només conté les columnes "permit", "handgun" i "long_gun".

### Test_Exercici4

 * test_time_evolution: Aquest test comprova el plot de la funció time_evolution. Verifica que es crea la figura, que es creen tres plots, i es comproven títols i llegenda.

### Test_Exercici5

 * test_groupby_state: Comprova si la funció groupby_state agrupa correctament el DataFrame per estat i suma les columnes "permit", "handgun" i "long_gun".
 Compara el resultat amb un DataFrame esperat.

 * test_clean_states: Verifica que la funció clean_states elimina les files amb l'estat "Guam" del DataFrame. Assegura que els altres estats continuen presents.

 * test_merge_datasets: Unifica el DataFrame original amb un DataFrame de població basat en l'estat. Compara el resultat amb un DataFrame esperat que conté les dades i la població de 2014.

 * test_calculate_relative_values: Afegeix els valors relatius de les tres mesures. Comprova si les noves columnes s'han afegit i si els valors calculats són correctes.

### Test_Exercici6

 * test_choromap_geojson: Comprova que existeix el directori Output.

 * test_exercici6: Comprova que la url de l'arxiu json està vigent.

## Llicencia

Copyright (c) 2024 [El teu nom]
Aquesta obra està sota una llicència Creative Commons Reconeixement-NoComercial 4.0 Internacional. https://creativecommons.org/licenses/by/3.0/es/legalcode.ca

## Contacte

Si se'm vol contactar, no ho dubteu a través de:

 - LinkedIn: https://www.linkedin.com/in/victormarmolromero/
 - email: vmarmolr@gmail.com
