# Assignment: Data Analysis and Visualization with Pandas and Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset

try:
    df = pd.read_csv('iris.csv')  # Replace with your actual file path
    print("Dataset loaded successfully.\n")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
    exit()

# Display first few rows
print("First five rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\nDataset Info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# Clean missing values (drop or fill as needed)
df.dropna(inplace=True)  # Assuming dropping for simplicity

# Task 2: Basic Data Analysis

print("\nDescriptive Statistics:")
print(df.describe())

# Grouping by species (assuming 'species' is a column)
if 'species' in df.columns:
    group_mean = df.groupby('species').mean(numeric_only=True)
    print("\nMean values grouped by species:")
    print(group_mean)

# Task 3: Data Visualization

# Line chart (Dummy: index vs petal length)
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['petal_length'], label='Petal Length')
plt.title('Line Chart of Petal Length Over Index')
plt.xlabel('Index')
plt.ylabel('Petal Length')
plt.legend()
plt.grid(True)
plt.show()

# Bar chart (Average petal length per species)
if 'species' in df.columns:
    plt.figure(figsize=(8, 5))
    group_mean['petal_length'].plot(kind='bar', color='skyblue')
    plt.title('Average Petal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Petal Length')
    plt.grid(axis='y')
    plt.show()

# Histogram of petal length
plt.figure(figsize=(8, 5))
plt.hist(df['petal_length'], bins=20, color='salmon', edgecolor='black')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.show()

# Scatter plot: sepal length vs petal length
plt.figure(figsize=(8, 5))
plt.scatter(df['sepal_length'], df['petal_length'], c='green')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.grid(True)
plt.show()

# Findings and Observations:
# (Write observations here after running and analyzing the plots)
# e.g., "Setosa species has significantly smaller petal lengths than the other species."

# End of Assignment
