import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the DataFrame
df = pd.read_csv('Heart.csv')

# EDA Example 1: Distribution of Age
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='Age', bins=20)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# EDA Example 2: Boxplot of Cholesterol Levels by Sex
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Sex', y='Chol')
plt.title('Cholesterol Levels by Sex')
plt.xlabel('Sex (0: Female, 1: Male)')
plt.ylabel('Cholesterol Level')
plt.show()

# EDA Example 3: Countplot of Chest Pain Types
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='ChestPain')
plt.title('Count of Chest Pain Types')
plt.xlabel('Chest Pain Type')
plt.ylabel('Count')
plt.show()

# EDA Example 4: Correlation Heatmap of Numeric Variables
numeric_columns = ['Age', 'RestBP', 'Chol', 'MaxHR', 'Oldpeak']
numeric_df = df[numeric_columns]
correlation_matrix = numeric_df.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Numeric Variables')
plt.show()

# EDA Example 5: Pairplot of Selective Variables
selected_columns = ['Age', 'RestBP', 'Chol', 'MaxHR', 'Oldpeak', 'AHD']
selected_df = df[selected_columns]
sns.pairplot(selected_df, hue='AHD')
plt.title('Pairplot of Selective Variables')
plt.show()

# EDA Example 6: Bar Plot of Thalassemia Types
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Thal')
plt.title('Count of Thalassemia Types')
plt.xlabel('Thalassemia Type')
plt.ylabel('Count')
plt.show()

# EDA Example 7: Scatter Plot of Resting Blood Pressure and Cholesterol
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='RestBP', y='Chol')
plt.title('Resting Blood Pressure vs. Cholesterol')
plt.xlabel('Resting Blood Pressure')
plt.ylabel('Cholesterol Level')
plt.show()

# EDA Example 8: Violin Plot of Resting Blood Pressure by Chest Pain Type
plt.figure(figsize=(8, 6))
sns.violinplot(data=df, x='ChestPain', y='RestBP')
plt.title('Resting Blood Pressure by Chest Pain Type')
plt.xlabel('Chest Pain Type')
plt.ylabel('Resting Blood Pressure')
plt.show()

# EDA Example 9: Bar Plot of Maximum Heart Rate by Thalassemia Type
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x='Thal', y='MaxHR')
plt.title('Maximum Heart Rate by Thalassemia Type')
plt.xlabel('Thalassemia Type')
plt.ylabel('Maximum Heart Rate')
plt.show()

# EDA Example 10: Pie Chart of Gender Distribution
gender_counts = df['Sex'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(gender_counts, labels=['Female', 'Male'], autopct='%1.1f%%', startangle=90)
plt.title('Gender Distribution')
plt.show()

# EDA Example 11: Line Plot of Cholesterol Levels Over Age
plt.figure(figsize=(8, 6))
sns.lineplot(data=df, x='Age', y='Chol')
plt.title('Cholesterol Levels Over Age')
plt.xlabel('Age')
plt.ylabel('Cholesterol Level')
plt.show()

# EDA Example 12: Swarm Plot of Resting Blood Pressure and Maximum Heart Rate by Atherosclerotic Heart Disease
plt.figure(figsize=(10, 6))
sns.swarmplot(data=df, x='AHD', y='RestBP', hue='MaxHR')
plt.title('Resting Blood Pressure and Maximum Heart Rate by Atherosclerotic Heart Disease')
plt.xlabel('Atherosclerotic Heart Disease')
plt.ylabel('Resting Blood Pressure')
plt.legend(title='Maximum Heart Rate')
plt.show()
