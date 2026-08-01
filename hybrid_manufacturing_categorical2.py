import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_theme(style="whitegrid")


df = pd.read_csv('hybrid_manufacturing_categorical.csv')


plt.figure(figsize=(15, 10))


plt.subplot(2, 2, 1)
sns.boxplot(x='Operation_Type', y='Energy_Consumption', data=df, palette='Set2')
plt.title('Energy Consumption Across Different Operation Types', fontsize=12, fontweight='bold')
plt.xlabel('Operation Type', fontsize=10)
plt.ylabel('Energy Consumption', fontsize=10)


plt.subplot(2, 2, 2)
sns.countplot(x='Machine_ID', hue='Job_Status', data=df, palette='viridis')
plt.title('Job Status Distribution per Machine', fontsize=12, fontweight='bold')
plt.xlabel('Machine ID', fontsize=10)
plt.ylabel('Count', fontsize=10)
plt.legend(title='Job Status')


plt.subplot(2, 2, 3)
sns.scatterplot(x='Processing_Time', y='Energy_Consumption', hue='Job_Status', data=df, alpha=0.7, palette='coolwarm')
plt.title('Processing Time vs Energy Consumption', fontsize=12, fontweight='bold')
plt.xlabel('Processing Time', fontsize=10)
plt.ylabel('Energy Consumption', fontsize=10)


plt.tight_layout()
plt.show()