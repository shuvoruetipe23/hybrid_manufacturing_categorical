import pandas as pd
import scipy.stats as stats
import numpy as np

# 1. Load dataset
df = pd.read_csv('hybrid_manufacturing_categorical.csv')

print("=" * 60)
print("--- ADVANCED STATISTICAL ANALYSES ---")
print("=" * 60)


print("\n[1] Chi-Square Test (Operation Type vs Job Status)")
contingency_table = pd.crosstab(df['Operation_Type'], df['Job_Status'])
chi2, p_chi2, dof, ex = stats.chi2_contingency(contingency_table)

print(f"Chi2 Statistic: {chi2:.4f}")
print(f"P-value: {p_chi2:.4f}")

if p_chi2 < 0.05:
    print("Result: Job status is dependent on the operation type (Statistically Significant).")
else:
    print("Result: Job status is independent of the operation type.")
print("-" * 60)



print("\n[2] Pearson Correlation (Processing Time vs Energy Consumption)")
corr, p_corr = stats.pearsonr(df['Processing_Time'], df['Energy_Consumption'])

print(f"Correlation Coefficient (r): {corr:.4f}")
print(f"P-value: {p_corr:.4f}")

if p_corr < 0.05:
    print("Result: There is a statistically significant linear correlation between processing time and energy consumption.")
else:
    print("Result: No significant linear correlation found.")
print("-" * 60)



print("\n[3] Mann-Whitney U Test (Energy Consumption: Completed vs Failed Jobs)")
completed_energy = df[df['Job_Status'] == 'Completed']['Energy_Consumption']
failed_energy = df[df['Job_Status'] == 'Failed']['Energy_Consumption']

u_stat, p_mw = stats.mannwhitneyu(completed_energy, failed_energy, alternative='two-sided')

print(f"U-statistic: {u_stat:.4f}")
print(f"P-value: {p_mw:.4f}")

if p_mw < 0.05:
    print("Result: There is a significant difference in energy consumption between completed and failed jobs.")
else:
    print("Result: No significant difference in energy consumption between completed and failed jobs.")
print("=" * 60)