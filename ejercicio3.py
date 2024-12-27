import pandas as pd

# Carga el dataset
df = pd.read_csv('dataset.csv')

# Formatea la fecha a (YYYY-MM-DD)
df['summary_date'] = pd.to_datetime(df['summary_date'], format='%Y.%m.%d').dt.date

# Rellena valores NaN en columnas numericas con 0
df['impressions'] = df['impressions'].fillna(0)
df['clicks'] = df['clicks'].fillna(0)
df['installs'] = df['installs'].fillna(0)
df['spend'] = df['spend'].fillna(0)

# Agrupa por nombre de campaña y calcula metricas
report = df.groupby('campaign_name').agg({
    'impressions': 'sum',
    'clicks': 'sum',
    'installs': 'sum',
    'spend': 'sum'
}).reset_index()

# Calcula CTR y CPI
report['CTR'] = report['clicks'] / report['impressions'].replace(0, 1)
report['CPI'] = report['spend'] / report['installs'].replace(0, 1)

# Guarda el informe final
report.to_csv('campaign_report.csv', index=False)


print("Informe generado correctamente. Detalles:")
print(report)
