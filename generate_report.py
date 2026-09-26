"""
YuvaIntern Week 2 Report Generator
Creates a professional .docx report for Advanced Data Visualization and Storytelling.
"""

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------

def add_code_block(doc, code_text):
    para = doc.add_paragraph()
    para.paragraph_format.left_indent = Inches(0.25)
    para.paragraph_format.space_before = Pt(2)
    para.paragraph_format.space_after = Pt(4)
    run = para.add_run(code_text)
    run.font.name = 'Courier New'
    run.font.size = Pt(8)
    pPr = para._p.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), 'F2F2F2')
    pPr.append(shd)


def add_table(doc, headers, rows):
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = 'Light Grid Accent 1'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = str(h)
        for p in hdr[i].paragraphs:
            for r in p.runs:
                r.font.bold = True
                r.font.size = Pt(10)
    for row_data in rows:
        cells = table.add_row().cells
        for i, val in enumerate(row_data):
            cells[i].text = str(val)
            for p in cells[i].paragraphs:
                for r in p.runs:
                    r.font.size = Pt(10)
    doc.add_paragraph()


def add_bullet(doc, text, level=0):
    style = 'List Bullet' if level == 0 else 'List Bullet 2'
    doc.add_paragraph(text, style=style)


def add_image_with_caption(doc, img_path, caption, width=5.8):
    if os.path.exists(img_path):
        doc.add_picture(img_path, width=Inches(width))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
        cap = doc.add_paragraph()
        cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = cap.add_run(caption)
        run.font.italic = True
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)


# ------------------------------------------------------------------
# Build document
# ------------------------------------------------------------------

doc = Document()
style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(11)

# ---------- Title page ----------
doc.add_paragraph('\n\n')
t = doc.add_paragraph()
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = t.add_run('YuvaIntern')
r.font.size = Pt(20); r.font.bold = True; r.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)

s = doc.add_paragraph()
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = s.add_run('Virtual Data Science with Python Apprentice Internship')
r.font.size = Pt(14); r.font.italic = True

doc.add_paragraph()

h = doc.add_paragraph()
h.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = h.add_run('WEEK 2 REPORT')
r.font.size = Pt(16); r.font.bold = True

h = doc.add_paragraph()
h.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = h.add_run('Advanced Data Visualization and Storytelling with Python')
r.font.size = Pt(15); r.font.bold = True; r.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)

h = doc.add_paragraph()
h.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = h.add_run('The Titanic Survival Story — Six Visual Chapters')
r.font.size = Pt(12); r.font.italic = True

doc.add_paragraph('\n\n')

info = doc.add_table(rows=0, cols=2)
info.alignment = WD_TABLE_ALIGNMENT.CENTER
rows = [
    ('Submitted by', 'Jermy Biju'),
    ('Role', 'Virtual Data Science with Python Apprentice Intern'),
    ('Organization', 'YuvaIntern'),
    ('Internship Duration', 'August 24, 2026 – September 28, 2026'),
    ('Week 2 Duration', '30 – 35 hours'),
    ('Dataset', 'Titanic (cleaned in Week 1, 889 rows × 14 columns)'),
    ('Tools', 'Python 3.14, Pandas, Matplotlib, Seaborn, python-docx'),
]
for k, v in rows:
    cells = info.add_row().cells
    cells[0].text = k; cells[1].text = v
    for p in cells[0].paragraphs:
        for r in p.runs:
            r.font.bold = True; r.font.size = Pt(11)
    for p in cells[1].paragraphs:
        for r in p.runs:
            r.font.size = Pt(11)

doc.add_page_break()


# ---------- 1. Executive Summary ----------
doc.add_heading('1. Executive Summary', level=1)
doc.add_paragraph(
    'This report presents the Week 2 task of the YuvaIntern Virtual Data Science with '
    'Python Apprenticeship: Advanced Data Visualization and Storytelling with Python. '
    'The objective was to build a coherent visual narrative around the cleaned Titanic '
    'dataset from Week 1 and to communicate the findings to a non-technical audience.'
)
doc.add_paragraph(
    'Six visualizations were produced, each designed to answer a specific question and '
    'to contribute to an overall story. The story is simple: survival on the Titanic was '
    'not random. It was strongly associated with three observed characteristics of the '
    'passengers — sex, passenger class, and family size. Female passengers, especially in '
    '1st and 2nd class, had the highest observed survival rates. Male passengers in 3rd '
    'class had the lowest. An interesting non-obvious pattern also emerged: passengers '
    'travelling in family groups of two to four had higher survival than those travelling '
    'alone or in very large families.'
)
doc.add_paragraph(
    'All observations are reported as associations, not causal claims. The dataset is '
    'observational and the analysis is descriptive.'
)


# ---------- 2. Introduction ----------
doc.add_heading('2. Introduction — Why Data Storytelling?', level=1)
doc.add_paragraph(
    'A good chart is not just a picture of data. It is an argument. Data storytelling is '
    'the practice of arranging charts, captions, and commentary so that a reader who has '
    'no data science background can follow a clear line of reasoning from beginning to end.'
)
doc.add_paragraph('A successful data story has three ingredients:')
add_bullet(doc, 'A question the reader cares about.')
add_bullet(doc, 'A chart that answers that question clearly and honestly.')
add_bullet(doc, 'A caption and commentary that explain what the chart shows and what it does not show.')
doc.add_paragraph(
    'Week 2 focuses on the third ingredient. Each visualization in this report is '
    'accompanied by (a) the question it answers, (b) the reason this chart type was '
    'chosen, and (c) the specific insight it contributes to the overall narrative.'
)
doc.add_page_break()

# ---------- 3. Dataset recap ----------
doc.add_heading('3. Dataset Recap', level=1)
doc.add_paragraph(
    'The dataset used is the cleaned version of the Titanic passenger dataset produced in '
    'Week 1. The raw file was acquired from the seaborn-data GitHub repository and cleaned '
    'as follows:'
)
add_bullet(doc, 'The deck column was dropped (≈77% missing values).')
add_bullet(doc, 'Missing age values were imputed using the median age within each (pclass, sex) subgroup.')
add_bullet(doc, 'Two rows with missing embarkation information were removed.')
add_bullet(doc, 'The 107 rows flagged by Pandas df.duplicated() were retained because they cannot be confirmed as true duplicates (no unique passenger identifier).')

doc.add_paragraph('Final cleaned shape: 889 rows × 14 columns, with zero missing values.')
doc.add_paragraph('This report uses the cleaned file data/titanic_cleaned.csv.')


# ---------- 4. Methodology ----------
doc.add_heading('4. Methodology', level=1)
doc.add_paragraph(
    'Each chart was developed in three stages: a clear question, a chart type chosen to '
    'answer that question, and annotations that highlight the key reading of the chart. '
    'Chart types were not chosen at random — the chosen form matches the question.'
)
add_table(doc,
          ['Chart', 'Question', 'Chart type chosen', 'Why this type'],
          [
              ('1', 'How did survival vary by sex and class?', 'Grouped bar chart',
               'Compares rates across two categorical variables side by side'),
              ('2', 'How did age differ between survivors and non-survivors?', 'Overlaid KDE',
               'Compares two distributions while preserving their shape'),
              ('3', 'Did travelling with family affect survival?', 'Bar chart with counts',
               'Highlights a non-monotonic pattern across an ordinal scale'),
              ('4', 'How did fare distributions differ by class?', 'Violin + inner box',
               'Shows median, spread, and skew simultaneously'),
              ('5', 'Can sex × class survival be seen at a glance?', 'Heatmap',
               'Encodes two categorical dimensions and one value in one view'),
              ('6', 'How do age and fare jointly relate to survival?', 'Annotated scatter',
               'Reveals clusters, outliers, and an annotated data point'),
          ])

doc.add_paragraph(
    'All charts were produced with Matplotlib and Seaborn and saved at 150 dpi for print '
    'quality. Charts were designed for a non-technical reader: titles state the question, '
    'axes are labelled in plain English, and key values are annotated directly on the '
    'chart so the reader does not need to estimate.'
)


# ---------- 5. The Visual Story ----------
doc.add_heading('5. The Visual Story — Six Chapters', level=1)

# --- Chapter 1 ---
doc.add_heading('5.1 Chapter 1 — Survival by Sex and Passenger Class', level=2)
add_image_with_caption(doc,
    'images/week2_chart1_survival_sex_class.png',
    'Figure 1: Survival rate by passenger class and sex. Values above each bar show the survival rate.')
doc.add_paragraph(
    'Question: Which combination of sex and class had the highest and lowest survival?'
)
doc.add_paragraph(
    'Chart choice: A grouped bar chart is the clearest way to compare a rate across two '
    'categorical dimensions at once. The reader can scan six bars and immediately see both '
    'the sex gap and the class gradient.'
)
doc.add_paragraph('Key readings:')
add_bullet(doc, 'Female, 1st class: 97% — the highest of any group.')
add_bullet(doc, 'Female, 2nd class: 92%.')
add_bullet(doc, 'Female, 3rd class: 50%.')
add_bullet(doc, 'Male, 1st class: 37%.')
add_bullet(doc, 'Male, 2nd class: 16%.')
add_bullet(doc, 'Male, 3rd class: 14% — the lowest of any group.')
doc.add_paragraph(
    'Insight: There is a clear association between both sex and class with survival. The '
    'gap between female and male survival is large in every class, and the gap between '
    '1st and 3rd class is large within each sex. This is the anchor chart of the whole '
    'story: whatever else the data shows, sex and class are the two strongest visible '
    'predictors of survival.'
)


# --- Chapter 2 ---
doc.add_heading('5.2 Chapter 2 — Age Distribution by Survival Status', level=2)
add_image_with_caption(doc,
    'images/week2_chart2_age_survival.png',
    'Figure 2: Age distributions of survivors (green) and non-survivors (red) using overlaid KDE curves.')
doc.add_paragraph('Question: Did age itself separate survivors from non-survivors?')
doc.add_paragraph(
    'Chart choice: A histogram would require two side-by-side panels, which makes '
    'comparison harder. An overlaid Kernel Density Estimate (KDE) shows both distributions '
    'on the same axis, so the reader can compare their shapes directly.'
)
doc.add_paragraph('Key readings:')
add_bullet(doc, 'The survivor distribution peaks sharply around ages 22–25.')
add_bullet(doc, 'The non-survivor distribution peaks slightly later, around ages 28–32, and is wider overall.')
add_bullet(doc, 'A small secondary bump appears in the non-survivor curve at ages 0–10.')
add_bullet(doc, 'Above age 50, the survivor curve drops below the non-survivor curve.')
doc.add_paragraph(
    'Insight: Age alone does not cleanly separate survivors from non-survivors — the two '
    'curves overlap heavily. The small bump of young children in the non-survivor curve is '
    'important: it shows that even among children, survival was not guaranteed. This '
    'reinforces the reading of Chapter 1 — the strongest visible factors are sex and '
    'class, not age.'
)


# --- Chapter 3 ---
doc.add_heading('5.3 Chapter 3 — Survival by Family Size', level=2)
add_image_with_caption(doc,
    'images/week2_chart3_family_size.png',
    'Figure 3: Survival rate by family size. Family size is defined as sibsp + parch + 1 (the passenger included).')
doc.add_paragraph(
    'Question: Did passengers travelling with family survive at a different rate from those '
    'travelling alone?'
)
doc.add_paragraph(
    'Chart choice: Family size is a small ordered integer (1 to 11), so a bar chart keeps '
    'the reading intuitive. Passenger counts per group are included as a footnote because '
    'the largest families contain very few passengers, and that context matters.'
)
doc.add_paragraph('Key readings:')
add_bullet(doc, 'Family size 1 (alone): 30% survival.')
add_bullet(doc, 'Family size 2–4: 55%, 58%, 72% — the highest survival range.')
add_bullet(doc, 'Family size 5–6: 20%, 14% — sharp drop.')
add_bullet(doc, 'Family size 8 and 11: 0% survival (very few passengers each).')
doc.add_paragraph(
    'Insight: This is the most interesting non-obvious pattern in the dataset. Survival '
    'is not "more family is better". There is a sweet spot at family sizes 2–4. Travelling '
    'completely alone was associated with lower survival (30%), but travelling in a very '
    'large family (5+) was associated with even lower survival. This non-monotonic shape '
    '— up then down — is what makes this chart worth a chapter of its own.'
)


# --- Chapter 4 ---
doc.add_heading('5.4 Chapter 4 — Fare Distribution by Passenger Class', level=2)
add_image_with_caption(doc,
    'images/week2_chart4_fare_by_class.png',
    'Figure 4: Fare distribution by passenger class. The violin shape shows the distribution; the inner box shows quartiles; the label shows the median.')
doc.add_paragraph('Question: How wide was the spread of fares, and how did it differ by class?')
doc.add_paragraph(
    'Chart choice: A bar chart would hide the shape of the distribution. A violin plot '
    'shows the full distribution shape, while the inner box plot shows the quartiles. '
    'This is a compact way to show median, spread, skew, and outliers together.'
)
doc.add_paragraph('Key readings:')
add_bullet(doc, '1st class median fare: £58.7. Range extends up to £512 (extreme outlier).')
add_bullet(doc, '2nd class median fare: £14.2. Tight distribution.')
add_bullet(doc, '3rd class median fare: £8.1. Very tight, low distribution.')
doc.add_paragraph(
    'Insight: Fare is strongly stratified by class, and 1st class fares are heavily '
    'right-skewed with a handful of very high values. This helps interpret Chapter 1: the '
    'apparent association between high fare and survival is largely a reflection of the '
    'association between high fare and 1st class. Fare alone is not a clean predictor of '
    'survival; it is entangled with class.'
)


# --- Chapter 5 ---
doc.add_heading('5.5 Chapter 5 — Survival Heatmap: Sex × Passenger Class', level=2)
add_image_with_caption(doc,
    'images/week2_chart5_survival_heatmap.png',
    'Figure 5: Heatmap of survival rate by sex and passenger class. Dark green = high survival; dark red = low survival.')
doc.add_paragraph(
    'Question: Can the whole sex × class survival picture be shown in a single view?'
)
doc.add_paragraph(
    'Chart choice: This chart is a companion to Chapter 1. A heatmap uses color to encode '
    'the survival rate so the reader can see the full 2 × 3 table in one glance. It is '
    'well suited for an executive summary or a slide.'
)
doc.add_paragraph('Key readings (identical numbers to Chapter 1, different form):')
add_bullet(doc, 'Female 1st: 0.97 (dark green).')
add_bullet(doc, 'Female 2nd: 0.92 (green).')
add_bullet(doc, 'Female 3rd: 0.50 (yellow).')
add_bullet(doc, 'Male 1st: 0.37 (yellow).')
add_bullet(doc, 'Male 2nd: 0.16 (red).')
add_bullet(doc, 'Male 3rd: 0.14 (dark red).')
doc.add_paragraph(
    'Insight: The chart reinforces the anchor finding visually: the top-left cell is '
    'almost always fully green, and the bottom-right cell is almost always fully red. '
    'Whatever the reader remembers from this report, this image is designed to be the one.'
)


# --- Chapter 6 ---
doc.add_heading('5.6 Chapter 6 — Age vs Fare by Survival Status', level=2)
add_image_with_caption(doc,
    'images/week2_chart6_age_fare_scatter.png',
    'Figure 6: Scatter plot of age vs fare, colored by survival status. The highest-fare passenger is annotated.')
doc.add_paragraph(
    'Question: When we look at age and fare together, what patterns become visible?'
)
doc.add_paragraph(
    'Chart choice: A scatter plot places every passenger as a single point. Color encodes '
    'survival. This chart is designed to show clusters, outliers, and one specific '
    'data point that anchors the story.'
)
doc.add_paragraph('Key readings:')
add_bullet(doc, 'The highest-fare passenger paid £512 and survived (annotated).')
add_bullet(doc, 'Almost all passengers with fares above £100 are coloured green (survived).')
add_bullet(doc, 'The dense low-fare region contains a mixture of red and green, showing that low fare alone did not determine outcome.')
add_bullet(doc, 'There is no simple "age line" separating survivors from non-survivors.')
doc.add_paragraph(
    'Insight: This chart closes the loop. High fare is associated with survival, but the '
    'association is driven by class, not by fare itself. Age does not visually separate '
    'the two groups. Together, the six charts support a single conclusion: the strongest '
    'visible factors associated with survival were sex, class, and family size — not age '
    'or fare by themselves.'
)


# ---------- 6. Business / Scientific Implications ----------
doc.add_heading('6. Business and Scientific Implications', level=1)
doc.add_paragraph(
    'The task asks for a written summary of potential business or scientific implications. '
    'The Titanic dataset is historical, but the analytical pattern generalises to several '
    'modern settings.'
)

doc.add_heading('6.1 Implications for real-world data work', level=2)
add_bullet(doc, 'Interaction effects matter. Looking at sex or class alone would have missed the fact that the largest and smallest survival gaps appear in specific combinations. In any business analysis, checking two variables together often reveals patterns that single-variable summaries hide.')
add_bullet(doc, 'Non-monotonic patterns are easy to miss. The family-size "sweet spot" at 2–4 members would be invisible to a correlation coefficient. This is a reminder that correlation-only summaries can hide the most interesting findings.')
add_bullet(doc, 'Correlated features are not independent evidence. Fare and class are strongly related. Treating them as separate predictors can overstate their combined effect.')

doc.add_heading('6.2 Implications for data storytelling practice', level=2)
add_bullet(doc, 'Chart form should match the question. Grouped bars for comparisons, KDE for distributions, violins for shape + quartiles, heatmaps for two-dimensional categorical data, and scatter plots for outliers.')
add_bullet(doc, 'Annotations do the storytelling. Labelling the exact percentage on top of each bar, or annotating the highest-fare passenger, removes ambiguity and turns the chart into an argument rather than a picture.')
add_bullet(doc, 'Show counts where they matter. The very small family sizes (8 and 11) look dramatic on the chart but represent very few passengers. Reporting counts protects against over-reading the data.')

doc.add_heading('6.3 What this analysis does not claim', level=2)
doc.add_paragraph(
    'This analysis is observational and descriptive. No causal claim is made about why any '
    'survival rate differs between groups. The patterns are described as associations and '
    'are intended as a starting point for further investigation, not as evidence of any '
    'underlying policy or mechanism.'
)


# ---------- 7. Conclusion ----------
doc.add_heading('7. Conclusion', level=1)
doc.add_paragraph(
    'Week 2 demonstrated that the same dataset can tell a much richer story when the '
    'right visual forms are paired with the right questions. Six charts — a grouped bar, '
    'a KDE overlay, a bar chart with counts, a violin plot, a heatmap, and an annotated '
    'scatter — were combined into a single narrative about survival on the Titanic. '
    'The strongest visible associations in the data are with sex, passenger class, and '
    'family size. Age and fare, on their own, are weaker and more entangled with the '
    'other variables.'
)
doc.add_paragraph(
    'The feedback from Week 1 asked for greater analytical depth and polished formatting. '
    'This report addresses both: three charts were designed to expose interaction effects '
    'and non-monotonic patterns that a single-variable view would miss, and the '
    'documentation for each chart now explains the reasoning behind the chart type, the '
    'specific reading of the chart, and the boundary of what the chart does and does not '
    'claim.'
)


# ---------- 8. Appendix — code ----------
doc.add_heading('8. Appendix — Key Code Snippets', level=1)

doc.add_heading('8.1 Grouped bar chart (Chapter 1)', level=2)
add_code_block(doc, '''sns.barplot(
    x='pclass', y='survived', hue='sex', data=df,
    errorbar=None,
    palette={'male': '#4C72B0', 'female': '#DD8452'}
)''')

doc.add_heading('8.2 Overlaid KDE (Chapter 2)', level=2)
add_code_block(doc, '''sns.kdeplot(
    data=df, x='age', hue='survived',
    fill=True, common_norm=False,
    palette={0: '#C44E52', 1: '#55A868'},
    alpha=0.5
)''')

doc.add_heading('8.3 Family size feature (Chapter 3)', level=2)
add_code_block(doc, '''df['family_size'] = df['sibsp'] + df['parch'] + 1

sns.barplot(
    x='family_size', y='survived', data=df,
    errorbar=None, hue='family_size',
    palette='viridis', legend=False
)''')

doc.add_heading('8.4 Violin plot (Chapter 4)', level=2)
add_code_block(doc, '''sns.violinplot(
    x='pclass', y='fare', data=df,
    hue='pclass', palette='Set2',
    inner='box', legend=False, cut=0
)''')

doc.add_heading('8.5 Heatmap (Chapter 5)', level=2)
add_code_block(doc, '''pivot = df.pivot_table(
    values='survived', index='sex',
    columns='pclass', aggfunc='mean'
)

sns.heatmap(pivot, annot=True, fmt='.2f',
            cmap='RdYlGn', vmin=0, vmax=1)''')

doc.add_heading('8.6 Annotated scatter (Chapter 6)', level=2)
add_code_block(doc, '''sns.scatterplot(
    data=df, x='age', y='fare',
    hue='survived', style='survived',
    palette={0: '#C44E52', 1: '#55A868'},
    alpha=0.6, s=40
)

max_fare_idx = df['fare'].idxmax()
max_fare = df.loc[max_fare_idx]
plt.annotate(f"Highest fare: £{max_fare['fare']:.0f}",
             xy=(max_fare['age'], max_fare['fare']))''')


# ---------- Save ----------
os.makedirs('report', exist_ok=True)
out = 'report/YuvaIntern_Week2_Report.docx'
doc.save(out)
print(f"Report saved to: {out}")