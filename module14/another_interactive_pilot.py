import pandas  as pd
import plotly.express as px

df = pd.read_csv("avgIQpercontrey.csv")

df["Population - 2023"] =df["Population - 2023"].str.replace(',','').astype(float)
fig = px.chorpleth(df,locations='Contry',locationmode='contry names',color='Average IQ',hover_name='Contry',
                    hover_data =['lireracy Rate','Nobel prices'],
                    projection='natural earth',title='Average IQ  Contry ')
fig.show()