# 📊 US Firearm Background Checks Analysis

> Data Science Programming final project for the **Universitat Oberta de Catalunya (UOC)**. This project explores the FBI NICS firearm background check dataset using Python for data cleaning, analysis, visualization, and testing. :contentReference[oaicite:0]{index=0}

---

## 🚀 Overview

This project follows a complete data analysis workflow, from importing raw datasets to generating interactive visualizations and statistical insights.

The analysis includes:

- 📥 Data ingestion from CSV files and online sources
- 🧹 Data cleaning and preprocessing
- 📊 Exploratory Data Analysis (EDA)
- 📈 Trend visualization
- 🗺️ Interactive choropleth maps
- ✅ Automated unit testing

---

## ✨ Features

- Import and clean real-world datasets
- Transform and engineer new features
- Aggregate data by state and year
- Analyze firearm permits and registrations
- Create interactive maps with Folium
- Visualize historical trends with Matplotlib
- Unit tests for every exercise

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Data Analysis | Pandas |
| Visualization | Matplotlib |
| Maps | Folium |
| Testing | unittest |
| Coverage | coverage.py |

---

## 📂 Project Structure

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

---

## 📚 Exercises

| Exercise | Description |
|----------|-------------|
| **Exercise 1** | Import and clean the original dataset |
| **Exercise 2** | Feature engineering from date columns |
| **Exercise 3** | Aggregate statistics by year and state |
| **Exercise 4** | Time-series visualization |
| **Exercise 5** | Population normalization and data merging |
| **Exercise 6** | Interactive choropleth maps |

---

## ▶️ Getting Started

### Clone the repository

```bash
git clone <repository-url>
cd <repository>
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the project

```bash
python main.py
```

---

## ✅ Running Tests

Run all unit tests:

```bash
python -m unittest discover Tests
```

Generate a coverage report:

```bash
coverage run -m unittest discover Tests
coverage html
```

---

## 📈 Outputs

The project generates:

- 📊 Historical trend visualizations
- 🗺️ Firearm permit map
- 🗺️ Handgun registration map
- 🗺️ Long gun registration map

---

## 🎯 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis
- Data Transformation
- Feature Engineering
- Data Visualization
- Geospatial Analysis
- Unit Testing
- Python Project Organization

---

## 📄 License

This project was developed for academic purposes as part of the **Data Science Programming** course at the **Universitat Oberta de Catalunya (UOC)**. :contentReference[oaicite:1]{index=1}

---

## 👤 Author

**Víctor Màrmol Romero**

📧 vmarmolr@gmail.com

💼 LinkedIn: https://linkedin.com/in/victormarmolromero
