# YuvaIntern — Data Science with Python (Week 2)

**Intern:** Jermy Biju
**Role:** Virtual Data Science with Python Apprentice Intern
**Organization:** YuvaIntern
**Internship Duration:** August 24, 2026 – September 28, 2026

## Week 2 Task
Advanced Data Visualization and Storytelling with Python

## Dataset
Cleaned Titanic dataset from Week 1 (889 rows × 14 columns, zero missing values).

## What was done
Six sophisticated visualizations, each designed to answer a specific question and contribute to an overall narrative about survival on the Titanic:

| # | Chart | Question |
|---|-------|----------|
| 1 | Grouped bar chart | How did survival vary by sex and class? |
| 2 | Overlaid KDE | How did age differ between survivors and non-survivors? |
| 3 | Bar chart with counts | Did travelling with family affect survival? |
| 4 | Violin + inner box | How did fare distributions differ by class? |
| 5 | Heatmap | Can sex × class survival be seen at a glance? |
| 6 | Annotated scatter | How do age and fare jointly relate to survival? |

## Project structure

YuvaIntern-DataScience-Week2/
├── data/
│ └── titanic_cleaned.csv
├── images/
│ ├── week2_chart1_survival_sex_class.png
│ ├── week2_chart2_age_survival.png
│ ├── week2_chart3_family_size.png
│ ├── week2_chart4_fare_by_class.png
│ ├── week2_chart5_survival_heatmap.png
│ └── week2_chart6_age_fare_scatter.png
├── report/
│ └── YuvaIntern_Week2_Report.docx
├── analysis.py
├── generate_report.py
├── .gitignore
└── README.md


## Tools
Python 3.14, Pandas, Matplotlib, Seaborn, python-docx

## How to run
python analysis.py # generates all 6 charts
python generate_report.py # builds the DOCX report


## Key findings
- Female passengers in 1st and 2nd class had the highest observed survival (97% and 92%).
- Male passengers in 3rd class had the lowest observed survival (14%).
- A non-obvious "sweet spot" appeared at family sizes 2–4 (highest survival).
- Fare and class are strongly entangled; fare alone is not a clean predictor.

## Note
All findings are reported as associations, not causal claims. The dataset is observational.

## Related repositories
- [Week 1 — Data Acquisition, Cleaning and EDA](https://github.com/jermybiju/YuvaIntern-DataScience-Week1)