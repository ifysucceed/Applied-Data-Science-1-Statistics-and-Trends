"""
Statistics and Trends Assignment
Creator: Chukwufumnaya Favour Nonum
Description:Analysis of car dataset exploring relationships
between mileage, price, and engine size.
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns


def preprocessing(df):
    """
    Clean and prepare data for analysis.
    Returns the cleaned DataFrame.
    """
    print("Initial Data Overview:")
    print(df.head())
    print("\nSummary Statistics:")
    print(df.describe())

    # Drop rows with missing values
    df = df.dropna()

    # Convert columns to appropriate types
    df['Year of manufacture'] = df['Year of manufacture'].astype(int)
    df['Engine size'] = df['Engine size'].astype(float)
    df['Mileage'] = df['Mileage'].astype(float)
    df['Price(GBP)'] = df['Price(GBP)'].astype(float)

    print("\nCorrelation Matrix:")
    print(df.corr(numeric_only=True))

    return df


def plot_relational_plot(df):
    """
    Relational plot: Scatter plot showing relationship between Mileage and Price.
    """
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x='Mileage', y='Price(GBP)', hue='Fuel type', alpha=0.7)
    plt.title('Relationship between Mileage and Price by Fuel Type')
    plt.xlabel('Mileage')
    plt.ylabel('Price (GBP)')
    plt.savefig('relational_plot.png')
    plt.close()


def plot_categorical_plot(df):
    """
    Categorical plot: Average price by manufacturer.
    """
    plt.figure(figsize=(10, 6))
    avg_price = df.groupby('Manufacturer')['Price(GBP)'].mean().sort_values(
    ascending=False
).head(10)

    # Generate distinct viridis colors for each bar
    cmap = plt.colormaps['viridis']
    colors = cmap(np.linspace(0, 0.8, len(avg_price)))

    avg_price.plot(kind='bar', color=colors)
    plt.title('Average Car Price by Top 5 Manufacturers')
    plt.xlabel('Manufacturer')
    plt.ylabel('Average Price (GBP)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('categorical_plot.png')
    plt.close()


def plot_statistical_plot(df):
    """
    Statistical plot: Correlation heatmap.
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('statistical_plot.png')
    plt.close()


def statistical_analysis(df, col: str):
    """
    Calculate mean, standard deviation, skewness, and excess kurtosis of a column.
    """
    data = df[col].dropna()
    mean = np.mean(data)
    stddev = np.std(data)
    skew = ss.skew(data)
    excess_kurtosis = ss.kurtosis(data)
    return mean, stddev, skew, excess_kurtosis


def writing(moments, col):
    """
    Print statistical moments and interpretation.
    """
    print(f'\nFor the attribute "{col}":')
    print(f'Mean = {moments[0]:.2f}, '
          f'Standard Deviation = {moments[1]:.2f}, '
          f'Skewness = {moments[2]:.2f}, and '
          f'Excess Kurtosis = {moments[3]:.2f}.')

    skewness = moments[2]
    kurtosis = moments[3]

    if skewness > 0:
        skew_desc = "right-skewed"
    elif skewness < 0:
        skew_desc = "left-skewed"
    else:
        skew_desc = "symmetrical"

    if kurtosis > 0:
        kurt_desc = "leptokurtic (heavy tails)"
    elif kurtosis < 0:
        kurt_desc = "platykurtic (light tails)"
    else:
        kurt_desc = "mesokurtic (normal)"

    print(f"The data is {skew_desc} and {kurt_desc}.")


def main():
    df = pd.read_csv('data.csv')
    df = preprocessing(df)

    # Choose column to analyze statistically
    col = 'Price(GBP)'

    # Create plots
    plot_relational_plot(df)
    plot_categorical_plot(df)
    plot_statistical_plot(df)

    # Statistical moments
    moments = statistical_analysis(df, col)
    writing(moments, col)


if __name__ == '__main__':
    main()
