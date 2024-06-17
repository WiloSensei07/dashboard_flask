import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

df = pd.read_csv(r'C:\Users\Sinka\OneDrive - Legrand France\Support DATA IA\ML IA\HeartDiseaseUCI.csv', index_col=None)

def get_scatter_plot():
    fig = px.scatter(data_frame=df, x="age", y="chol", color="num")
    return pio.to_html(fig, full_html=False)

def get_bar_plot():
    fig = px.bar(data_frame=df, x="age", y="chol", color="num")
    return pio.to_html(fig, full_html=False)

def get_spider_plot(df):
    # Sélection des variables pour le radar chart
    variables = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']

    # Normaliser les variables par rapport à l'âge
    df_normalized = df.copy()
    for var in variables:
        df_normalized[var] = df_normalized[var] / df_normalized['age']

    # Calculer les moyennes des variables normalisées par classe 'num'
    df_grouped = df_normalized.groupby('num')[variables].mean().reset_index()

    # Création du radar chart
    fig = go.Figure()

    for i in range(df_grouped.shape[0]):
        fig.add_trace(go.Scatterpolar(
            r=df_grouped.loc[i, variables].values,
            theta=variables,
            fill='toself',
            name=f'Classe {df_grouped["num"].iloc[i]}'
        ))

    # Mise en forme du graphique
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, df_normalized[variables].max().max()]
            )),
        showlegend=True,
        title="Radar Chart des Variables Normalisées par Rapport à l'Âge"
    )

    return pio.to_html(fig, full_html=False)
