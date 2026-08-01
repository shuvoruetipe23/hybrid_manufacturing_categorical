# Hybrid Manufacturing Operational Data Analysis & Statistical Modeling

An end-to-end data analysis and statistical hypothesis-testing project using Python, SciPy, and Seaborn to evaluate performance metrics, energy consumption, and failure risks in a hybrid manufacturing system.

---

## 🚀 Project Overview
This project applies probability and statistics concepts to real-world manufacturing operations data. The objective is to analyze machine performance, test operational hypotheses (such as processing time comparisons and energy variance), and uncover critical patterns affecting production efficiency, delays, and job failures.

---

## 🛠️ Tech Stack & Libraries
* **Language:** Python
* **Data Manipulation & Analysis:** Pandas, NumPy
* **Statistical Analysis:** SciPy (`scipy.stats`)
* **Data Visualization:** Matplotlib, Seaborn

---

## 📊 Key Analyses Performed
1. **Descriptive Statistics:** Summarized key operational variables like processing time, energy consumption, and machine availability.
2. **Independent T-Test:** Evaluated whether there is a statistically significant difference in processing times between different operation types (e.g., *Grinding* vs. *Lathe*).
3. **One-Way ANOVA Test:** Tested if mean energy consumption varies significantly across multiple manufacturing operation categories.
4. **Normality Testing:** Checked data distribution characteristics using the Shapiro-Wilk test.
5. **Operational Visualization:** Generated box plots, count plots, and scatter plots to visualize bottlenecks, job statuses (`Completed`, `Delayed`, `Failed`), and energy trends.

---

## 📁 Repository Structure
```text
├── hybrid_manufacturing_categorical.csv  # Dataset
├── analysis.py                           # Python script for statistical tests
├── visualization.py                      # Seaborn visualization script
└── README.md                             # Project Documentation
