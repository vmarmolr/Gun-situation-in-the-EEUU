# Projecte Final
 
This is the final practice of the programming course for data science at the Open University of Catalonia.
 
The instructions for this project are found in the Enunciat/ folder where we can find the pdf in Catalan and Spanish.
 
## Table of contents
 
 - [Directory](#Directory)
 - [Requirements](#Requirements)
 - [Run](#Run)
 - [Exercises](#Exercises)
 - [Main](#Main)
 - [Tests](#Tests)
 - [License](#License)
 - [Contact](#Contact)
## Directory
 
```text
.
├── Data/
│   ├── nics-firearm-background-checks.csv
│   ├── us-state-populations.csv
│   └── Comentari-del-grafic.pdf
│
├── Enunciat/
├── Moduls/
│   ├── Exercici1.py
│   ├── Exercici2.py
│   ├── Exercici3.py
│   ├── Exercici4.py
│   ├── Exercici5.py
│   └── Exercici6.py
│
├── Output/
│   ├── mapa_llargues.html
│   ├── mapa_llicencies.html
│   └── mapa_pistoles.html
│
├── Tests/
├── main.py
├── requirements.txt
└── README.md
└── README_extended.md
└── README_extended_catalan.md
```
 
## Requirements
 
### Requirements for exercises:
 
 - pandas
 - matplotlib.pyplot
 - webbrowser
 - folium
### Requirements for tests:
 
 - unittest
 - os
 - pandas
 - matplotlib.pyplot
 - requests
 - from unittest.mock import patch
## Run
 
To run the code you must execute the main file with the script:
 
```bash
python3 main.py
```
 
This will execute the entire practice in sequence, as indicated in the assignment. However, once the entire practice has been executed we will have a menu waiting for a response:
 
 * If you want to execute the practice again in its entirety, then you will have to press 0. We call this option the default option.
 * If you want to execute the practice section by section, press 1. If you keep pressing Enter the practice will advance. The practice will always stop at a print statement that says what will happen when you press Enter.
 * If you want to exit the practice you will have to press any button.
We will see that the practice will open a plot, a pdf and three maps.
 
Regarding tests:
If we want to run them we will have to do them one by one. We have one test per exercise. For example, if we want to do the tests for exercise 1, we must execute the following script:
 
```bash
python3 Test_Exercici1.py
```
 
Regarding coverage:
 
From the project directory we must run the instruction:
```bash
coverage run --omit="/usr/*" -m unittest discover -s Tests -p "Test_*.py"
```
 
In the terminal. Followed by:
```bash
coverage report -m
```
 
to make a report and read it we can execute:
```bash
coverage html
```
 
Which will generate an html report to view it clearly. The htmlcov folder will be generated and to read it we only need the instruction:
```bash
open htmlcov/index.html
```
 
In our case we can see that we have a coverage of the entire project of 72%. Ideally, we would want the coverage to be as high as possible. It should be noted that we can still improve the tests especially for Exercise3 and Exercise5 which have coverage of less than 50%. Despite this, for personal reasons I have not been able to invest more time in the practice and I hope that I have been able to demonstrate the knowledge obtained in this course.
 
I take this opportunity to thank you for your time and dedication and, taking this opportunity, wish you a good summer.
 
## Exercises
 
We will explain the exercises one by one.
 
### Exercise 1
 
This exercise demonstrates how to read a CSV dataset and modify the name of a column
 
Objectives:
 
 * Read a CSV file from a URL.
 * Display the first 5 columns and their structure.
 * Select the relevant columns for analysis.
 * Change the name of a column.
Functions:
 
 * read_csv(url: str) -> pd.DataFrame: Reads a CSV file from a URL and returns a data frame.
 * clean_csv(joc_dades: pd.DataFrame) -> pd.DataFrame: Selects the desired columns and returns a clean data frame.
 * rename_col(columnes_df: pd.DataFrame) -> pd.DataFrame: Changes the name of the "longgun" column to "long_gun".
 * continuar(auto: bool = True) -> None: Stops the practice until enter is pressed if auto is False.
 * exercici1(auto: bool = True) -> pd.DataFrame: Executes exercise 1 and returns a data frame with the result. If auto is True it does not stop if it is False it does.
Input:
 
 * nics-firearm-background-checks.csv
### Exercise 2
 
Separates the month column and keeps the year.
 
Objectives:
 
 * Decompose the "month" column into separate columns for year and month.
 * Remove the "month" column.
Functions:
 
 * breakdown_date(df: pd.DataFrame) -> pd.DataFrame: Decomposes the "month" column and returns a data frame with "year" and "month" columns.
 * erase_month(df_mes: pd.DataFrame) -> pd.DataFrame: Removes the "month" column and returns a data frame.
 * exercici2(df: pd.DataFrame, auto: bool = True) -> pd.DataFrame: Executes exercise 2 and returns a data frame with the result. If auto is True it does not stop if it is False it does.
### Exercise 3
 
Performs a groupby of the data and displays the year and state with the highest number of handguns and long guns.
 
Objectives:
 
 * Group the data by year and state.
 * Sum the "permit", "handgun" and "long_gun" columns.
 * Identify the year and state with the largest number of handguns.
 * Identify the year and state with the largest number of long guns.
Functions:
 
 * groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame: Groups the data by year and state and returns a data frame with the sums of "permit", "handgun" and "long_gun".
 * print_biggest_handguns(df: pd.DataFrame) -> None: Prints information about the year and state with the highest number of handguns.
 * print_biggest_longguns(df: pd.DataFrame) -> None: Prints information about the year and state with the highest number of long guns.
 * exercici3(df: pd.DataFrame, auto: bool = True) -> pd.DataFrame: Executes exercise 3 and returns a data frame with the result. If auto is True it does not stop if it is False it does.
### Exercise 4
 
Creates a graph of the group by and opens the comment in pdf.
 
Objectives:
 
 * Create a graph showing the number of permits, handguns and long guns per year.
 * Open a comment in PDF format with additional explanations about the graph.
Functions:
 
 * time_evolution(df: pd.DataFrame) -> None: Creates a graph of the temporal evolution of permits and firearms records.
 * obrir_comentari(url: str) -> None: Opens a new browser tab with the specified URL.
 * exercici4(df: pd.DataFrame, auto: bool = True) -> None: Executes exercise 4 and displays the graph and comment. If auto is True it does not stop if it is False it does.
Input:
 
 * Comentari-del-grafic.pdf
### Exercise 5
 
Performs a groupby by states and removes outliers by replacing them with more appropriate values.
 
Objectives:
 
 * Group the data by state.
 * Remove certain states.
 * Group the data with a population dataset by state.
 * Calculate relative percentage values of permits and firearms records per population.
Functions:
 
 * groupby_state(df: pd.DataFrame) -> pd.DataFrame: Groups the data by state and sums the "permit", "handgun" and "long_gun" columns.
 * clean_states(df: pd.DataFrame) -> pd.DataFrame: Removes certain specified states from the DataFrame.
 * merge_datasets(df_exercici: pd.DataFrame, df_nou: pd.DataFrame) -> pd.DataFrame: Merges two DataFrames based on the "state" column.
 * calculate_relative_values(df: pd.DataFrame) -> pd.DataFrame: Calculates relative percentage values with respect to population.
 * exercici5(df: pd.DataFrame, auto: bool = True) -> pd.DataFrame: Executes exercise 5 and returns the DataFrame with the results. If auto is True it does not stop if it is False it does.
Input:
 
 * us-state-populations.csv
### Exercise 6
 
Create three maps for the three metrics we want.
 
Objectives:
 
 * Create a map for each type of firearms record: permits, long guns and handguns.
 * Represent the proportion of firearms records or licenses per population in each state.
 * Use colors and legends for clear and useful visualization.
Functions:
 
choromap_geojson(df: pd.DataFrame,
                 columnes: list,
                 nom_llegenda: str,
                 url_json: str,
                 color: str = "YlOrRd",
                 nom_mapa: str = "Mapa") -> None: Creates a choropleth map with geographic data and associated values.
 
Input:
 
 * https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/us-states.json
Output:
 
 * /home/datasci/prog_datasci_2/activities/activity_4/Output/mapa_llargues.html
 * /home/datasci/prog_datasci_2/activities/activity_4/Output/mapa_llicencies.html
 * /home/datasci/prog_datasci_2/activities/activity_4/Output/mapa_pistoles.html
## Main
 
This script allows you to run the entire practice.
 
Functions:
 
 * practica_sencera(auto: bool = True) -> None: Executes all exercises in the practice sequentially.
 * main() -> None: Shows the user to select whether to run the complete practice or the sections individually.
## Tests
 
We have one test per exercise:
 
### Test_Exercici1
 
 * test_read_csv: This test verifies if the number of columns in the DataFrame is greater than or equal to 5.
 * test_clean_csv: This test cleans the DataFrame with the clean_csv function. Then it prints the DataFrame. The test checks that the columns of the resulting DataFrame are exactly ['month', 'state', 'permit', 'handgun', 'long_gun'].
 * test_rename_col: This test changes the name of the "longgun" column to "long_gun" with the rename_col function. It checks that the "longgun" column is no longer present and that the renamed "long_gun" column exists in the DataFrame.
 * test_exercici1: This test verifies if the expected input data file: "/home/datasci/prog_datasci_2/activities/activity_4/Data/nics-firearm-background-checks.csv" exists.
### Test_Exercici2
 
 * test_breakdown_date: This test verifies the E2.breakdown_date function, which extracts year and month information from the "month" column. It checks if new columns named "year" and "month" are created in the DataFrame and confirms that the data types of these new columns are integers.
 * test_erase_month: This test checks that the "month" column is no longer present after applying the erase_month function.
### Test_Exercici3
 
 * test_groupby_state_and_year: This test checks that the DataFrame after applying the groupby_state_and_year function only contains the columns "permit", "handgun" and "long_gun".
### Test_Exercici4
 
 * test_time_evolution: This test checks the plot of the time_evolution function. It verifies that the figure is created, that three plots are created, and titles and legend are checked.
### Test_Exercici5
 
 * test_groupby_state: Checks if the groupby_state function correctly groups the DataFrame by state and sums the "permit", "handgun" and "long_gun" columns. Compares the result with an expected DataFrame.
 * test_clean_states: Verifies that the clean_states function removes rows with the state "Guam" from the DataFrame. Ensures that other states remain present.
 * test_merge_datasets: Merges the original DataFrame with a population DataFrame based on state. Compares the result with an expected DataFrame that contains the data and population from 2014.
 * test_calculate_relative_values: Adds the relative values of the three measures. Checks if the new columns have been added and if the calculated values are correct.
### Test_Exercici6
 
 * test_choromap_geojson: Checks that the Output directory exists.
 * test_exercici6: Checks that the json file URL is active.
## License
 
Copyright (c) 2024 [Victor Marmol Romero]
This work is under a Creative Commons Attribution-NonCommercial 4.0 International License. https://creativecommons.org/licenses/by/3.0/es/legalcode.ca
 
## Contact
 
If you want to contact me, do not hesitate to do so through:
 
 - LinkedIn: https://www.linkedin.com/in/victormarmolromero/
 - email: vmarmolr@gmail.com
