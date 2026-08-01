import pandas as pd
import scipy.stats as stats
import numpy as np

# 1. Load the dataset
print("--- Loading Dataset ---")
df = pd.read_csv('hybrid_manufacturing_categorical.csv')
print(f"Total Rows: {df.shape[0]}, Total Columns: {df.shape[1]}\n")


print("--- 1. Descriptive Statistics (Processing Time & Energy Consumption) ---")
print("Processing Time Summary:")
print(df['Processing_Time'].describe())
print("\nEnergy Consumption Summary:")
print(df['Energy_Consumption'].describe())
print("-" * 60)


print("\n--- 2. Independent T-Test (Grinding vs Lathe Processing Time) ---")
grinding_time = df[df['Operation_Type'] == 'Grinding']['Processing_Time']
lathe_time = df[df['Operation_Type'] == 'Lathe']['Processing_Time']

t_stat, t_pval = stats.ttest_ind(grinding_time, lathe_time)
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {t_pval:.4f}")

if t_pval < 0.05:
    print("Result: There is a statistically significant difference in processing time between the two operations.")
else:
    print("Result: No significant difference found in processing time between the two operations.")
print("-" * 60)


print("\n--- 3. One-Way ANOVA Test (Energy Consumption across Operation Types) ---")
groups = [group['Energy_Consumption'].values for name, group in df.groupby('Operation_Type')]
f_stat, f_pval = stats.f_oneway(*groups)

print(f"F-statistic: {f_stat:.4f}")
print(f"P-value: {f_pval:.4f}")

if f_pval < 0.05:
    print("Result: There is a significant variance in energy consumption across different operation types.")
else:
    print("Result: No significant variation in energy consumption across operation types.")
print("-" * 60)


print("\n--- 4. Normality Test (Shapiro-Wilk Test for Energy Consumption) ---")


sample_data = df['Energy_Consumption'].sample(n=min(500, len(df)), random_state=42)
norm_stat, norm_pval = stats.shapiro(sample_data)

print(f"Shapiro Statistic: {norm_stat:.4f}")
print(f"P-value: {norm_pval:.4f}")

if norm_pval > 0.05:
    print("Result: The data is normally distributed.")
else:
    print("Result: The data is non-normal (does not follow a normal distribution).")
print("-" * 60)