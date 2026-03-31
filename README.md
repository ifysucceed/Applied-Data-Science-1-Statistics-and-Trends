# Statistical Analysis of Car Attributes and Market Trends

## 📌 Overview
This repository is about a statistical analysis project exploring trends and relationships within a car dataset. The project was completed as part of a *Statistics and Trends* assignment.

The aim of this analysis is to understand how different factors such as mileage, engine size, fuel type, age (year of manufacture), and manufacturer influence car prices. The project applies data preprocessing, visualization techniques, and statistical analysis to uncover meaningful patterns.

---

## 📊 Dataset Description

The dataset (`data.csv`) contains information about different cars, with the following attributes:

- **Manufacturer** – Brand of the car (e.g., Ford, BMW, Toyota)
- **Model** – Specific model of the car
- **Engine size** – Engine capacity (in litres)
- **Fuel type** – Type of fuel used (Petrol, Diesel, Hybrid, Electric)
- **Year of manufacture** – Production year of the vehicle
- **Mileage** – Distance the car has travelled
- **Price (GBP)** – Market price of the car in British Pounds (£)

---

## 📈 Analysis Performed

The project includes the following analyses:

### 1. Data Preprocessing
- Handling missing values
- Converting columns to appropriate data types
- Generating summary statistics (`describe`, `correlation`)

### 2. Data Visualisation

Three types of plots were created:

- **Relational Plot (Scatter Plot)**  
  Shows the relationship between mileage and price, discovered a negative between mileage and price, cars with higher mileage tend to have lower resale value.

- **Categorical Plot (Bar Chart)**  
  Displays average car prices across different manufacturers, showing differences between premium and budget brands.

- **Statistical Plot (Correlation Heatmap)**  
  Visualises relationships between numerical variables such as mileage, engine size, year, and price.

---

## 📐 Statistical Analysis

The project calculates the four main statistical moments for the **Price (GBP)** variable:

- **Mean** – Average price
- **Standard Deviation** – Spread of prices
- **Skewness** – Direction of distribution (left/right skew)
- **Kurtosis** – Shape of distribution (tails and outliers)

These metrics help describe how car prices are distributed in the dataset.

---

## 🚀 How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/ifysucceed/statistics-and-trends-assignment.git
cd statistics-and-trends-assignment
