import pandas as pd
import plotly.express as px
import datetime as dt
from statistics import mean

class Seasons:
    WINTER = [12, 1, 2]
    SPRING = [3, 4, 5]
    SUMMER = [6, 7, 8]
    AUTUMN = [9, 10, 11]

class TempAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_overview(self):
        temps = [x['temperature'] for x in self.data]
        return {'average': round(mean(temps), 2), 'min': min(temps), 'max': max(temps)}

    def get_monthly_avg(self):
        result = {}
        for r in self.data:
            m = r['date'].strftime('%B')
            result.setdefault(m, []).append(r['temperature'])
        return {m: round(mean(v), 2) for m, v in result.items()}

    def get_seasonal_avg(self):
        s_map = {'Winter': Seasons.WINTER, 'Spring': Seasons.SPRING, 'Summer': Seasons.SUMMER, 'Autumn': Seasons.AUTUMN}
        out = {}
        for s, months in s_map.items():
            temps = [x['temperature'] for x in self.data if x['date'].month in months]
            if temps:
                out[s] = round(mean(temps), 2)
        return out

data_2022 = [
    {'date': dt.datetime(2022, 1, 8), 'temperature': 3},
    {'date': dt.datetime(2022, 2, 12), 'temperature': 6},
    {'date': dt.datetime(2022, 3, 15), 'temperature': 11},
    {'date': dt.datetime(2022, 4, 10), 'temperature': 16},
    {'date': dt.datetime(2022, 5, 22), 'temperature': 20},
    {'date': dt.datetime(2022, 6, 14), 'temperature': 26},
    {'date': dt.datetime(2022, 7, 8), 'temperature': 33},
    {'date': dt.datetime(2022, 8, 19), 'temperature': 31},
    {'date': dt.datetime(2022, 9, 10), 'temperature': 24},
    {'date': dt.datetime(2022, 10, 27), 'temperature': 15},
    {'date': dt.datetime(2022, 11, 18), 'temperature': 8},
    {'date': dt.datetime(2022, 12, 25), 'temperature': 2},
]

a = TempAnalyzer(data_2022)
o = a.get_overview()
m = a.get_monthly_avg()
s = a.get_seasonal_avg()


df_m = pd.DataFrame({'Month': list(m.keys()), 'Temp': list(m.values())})
month_order = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]
df_m['Month'] = pd.Categorical(df_m['Month'], categories=month_order, ordered=True)
df_m = df_m.sort_values('Month')


px.bar(df_m, x='Month', y='Temp', title='Monthly Avg Temps 2022', color='Temp').show()

df_s = pd.DataFrame({'Season': list(s.keys()), 'Temp': list(s.values())})
px.bar(df_s, x='Season', y='Temp', title='Seasonal Avg Temps 2022', color='Temp').show()

df_o = pd.DataFrame({'Type': ['Min', 'Avg', 'Max'], 'Temp': [o['min'], o['average'], o['max']]})
px.bar(df_o, x='Type', y='Temp', title='Yearly Stats 2022', color='Temp').show()
