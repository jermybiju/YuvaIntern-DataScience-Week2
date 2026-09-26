import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the cleaned dataset from Week 1
df = pd.read_csv("data/titanic_cleaned.csv")

# Create images folder if it does not exist
os.makedirs("images", exist_ok=True)

# Style
sns.set_style("whitegrid")

# ---------- Chart 1: Survival by Sex and Passenger Class ----------
plt.figure(figsize=(8, 5))

ax = sns.barplot(
    x='pclass',
    y='survived',
    hue='sex',
    data=df,
    errorbar=None,
    palette={'male': '#4C72B0', 'female': '#DD8452'}
)

# Titles and labels
plt.title("Survival Rate by Passenger Class and Sex", fontsize=13, fontweight='bold')
plt.xlabel("Passenger Class (1 = First, 2 = Second, 3 = Third)", fontsize=11)
plt.ylabel("Survival Rate", fontsize=11)
plt.ylim(0, 1.0)

# Custom x-tick labels for readability
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(['1st Class', '2nd Class', '3rd Class'])

# Legend
plt.legend(title='Sex', loc='upper right')

# Add value labels on top of each bar
for container in ax.containers:
    ax.bar_label(container, fmt='%.2f', padding=3, fontsize=9)

plt.tight_layout()
plt.savefig("images/week2_chart1_survival_sex_class.png", dpi=150)
plt.close()

print("Chart 1 saved: images/week2_chart1_survival_sex_class.png")

# ---------- Chart 2: Age Distribution by Survival ----------
plt.figure(figsize=(9, 5))

sns.kdeplot(
    data=df,
    x='age',
    hue='survived',
    fill=True,
    common_norm=False,
    palette={0: '#C44E52', 1: '#55A868'},
    alpha=0.5,
    linewidth=2
)

plt.title("Age Distribution by Survival Status", fontsize=13, fontweight='bold')
plt.xlabel("Age (years)", fontsize=11)
plt.ylabel("Density", fontsize=11)

# Custom legend
plt.legend(title='Survived', labels=['Did Not Survive (0)', 'Survived (1)'], loc='upper right')

plt.tight_layout()
plt.savefig("images/week2_chart2_age_survival.png", dpi=150)
plt.close()

print("Chart 2 saved: images/week2_chart2_age_survival.png")

# ---------- Chart 3: Family Size vs Survival ----------
# Create family_size = sibsp + parch + 1 (including the passenger)
df['family_size'] = df['sibsp'] + df['parch'] + 1

plt.figure(figsize=(9, 5))

ax = sns.barplot(
    x='family_size',
    y='survived',
    data=df,
    errorbar=None,
    hue='family_size',
    palette='viridis',
    legend=False
)

plt.title("Survival Rate by Family Size", fontsize=13, fontweight='bold')
plt.xlabel("Family Size (Number of Family Members Aboard, including self)", fontsize=11)
plt.ylabel("Survival Rate", fontsize=11)
plt.ylim(0, 1.0)

# Value labels
for container in ax.containers:
    ax.bar_label(container, fmt='%.2f', padding=3, fontsize=9)

# Add count of passengers per family size below each bar (optional annotation)
counts = df['family_size'].value_counts().sort_index()
note = "Passenger counts per family size:\n" + ", ".join([f"{k}: {v}" for k, v in counts.items()])
plt.figtext(0.5, -0.05, note, ha='center', fontsize=9, style='italic')

plt.tight_layout()
plt.savefig("images/week2_chart3_family_size.png", dpi=150)
plt.close()

print("Chart 3 saved: images/week2_chart3_family_size.png")



# ---------- Chart 4: Fare Distribution by Passenger Class (Violin + Box) ----------
plt.figure(figsize=(9, 5))

# Violin plot (shows distribution shape) + inner box (shows quartiles)
ax = sns.violinplot(
    x='pclass',
    y='fare',
    data=df,
    hue='pclass',
    palette='Set2',
    inner='box',
    legend=False,
    cut=0
)

plt.title("Fare Distribution by Passenger Class", fontsize=13, fontweight='bold')
plt.xlabel("Passenger Class", fontsize=11)
plt.ylabel("Fare (pounds)", fontsize=11)

# Custom x-tick labels
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(['1st Class', '2nd Class', '3rd Class'])

# Add median values as text above each violin
medians = df.groupby('pclass')['fare'].median()
for i, cls in enumerate([1, 2, 3]):
    ax.text(i, medians[cls] + 5, f"Median: £{medians[cls]:.1f}",
            ha='center', fontsize=9, style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.8))

plt.tight_layout()
plt.savefig("images/week2_chart4_fare_by_class.png", dpi=150)
plt.close()

print("Chart 4 saved: images/week2_chart4_fare_by_class.png")


# ---------- Chart 5: Survival Heatmap (Sex x Class) ----------
# Create a pivot table: rows = sex, columns = pclass, values = mean survival
pivot = df.pivot_table(
    values='survived',
    index='sex',
    columns='pclass',
    aggfunc='mean'
)

plt.figure(figsize=(7, 4))

ax = sns.heatmap(
    pivot,
    annot=True,
    fmt='.2f',
    cmap='RdYlGn',
    vmin=0,
    vmax=1,
    linewidths=1,
    linecolor='white',
    cbar_kws={'label': 'Survival Rate'}
)

plt.title("Survival Rate Heatmap: Sex × Passenger Class", fontsize=13, fontweight='bold')
plt.xlabel("Passenger Class", fontsize=11)
plt.ylabel("Sex", fontsize=11)

ax.set_xticklabels(['1st Class', '2nd Class', '3rd Class'], rotation=0)
ax.set_yticklabels(['Female', 'Male'], rotation=0)

plt.tight_layout()
plt.savefig("images/week2_chart5_survival_heatmap.png", dpi=150)
plt.close()

print("Chart 5 saved: images/week2_chart5_survival_heatmap.png")



# ---------- Chart 6: Age vs Fare by Survival (Annotated Scatter) ----------
plt.figure(figsize=(10, 6))

# Scatter plot with survival as color
scatter = sns.scatterplot(
    data=df,
    x='age',
    y='fare',
    hue='survived',
    style='survived',
    palette={0: '#C44E52', 1: '#55A868'},
    alpha=0.6,
    s=40
)

plt.title("Age vs Fare by Survival Status", fontsize=13, fontweight='bold')
plt.xlabel("Age (years)", fontsize=11)
plt.ylabel("Fare (pounds)", fontsize=11)

# Legend customization
handles, labels = scatter.get_legend_handles_labels()
plt.legend(handles=handles, labels=['Did Not Survive', 'Survived'], 
           title='Survived', loc='upper right')

# Add annotation to highlight the highest fare passengers
max_fare_idx = df['fare'].idxmax()
max_fare = df.loc[max_fare_idx]
plt.annotate(
    f"Highest fare: £{max_fare['fare']:.0f}\n(Survived: {int(max_fare['survived'])})",
    xy=(max_fare['age'], max_fare['fare']),
    xytext=(max_fare['age'] - 25, max_fare['fare'] - 30),
    fontsize=9,
    arrowprops=dict(arrowstyle='->', color='gray'),
    bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', edgecolor='gray')
)

plt.tight_layout()
plt.savefig("images/week2_chart6_age_fare_scatter.png", dpi=150)
plt.close()

print("Chart 6 saved: images/week2_chart6_age_fare_scatter.png")