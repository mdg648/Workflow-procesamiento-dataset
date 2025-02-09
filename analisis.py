import pandas as pd
import sys

# leer csv
if len(sys.argv) < 2:
    print("Por favor, proporciona el nombre del archivo CSV como argumento.")
    sys.exit(1)

csv_file = sys.argv[1]
df = pd.read_csv(csv_file)

import matplotlib.pyplot as plt

# calcular puntos medios por partido para cada equipo
df['total_pts_home'] = df.groupby('team_name_home')['pts_home'].transform('mean')
df['total_pts_away'] = df.groupby('team_name_away')['pts_away'].transform('mean')

# combinar los puntos medios de local y visitante
df_home = df[['team_name_home', 'total_pts_home']].drop_duplicates().rename(columns={'team_name_home': 'team_name', 'total_pts_home': 'avg_pts'})
df_away = df[['team_name_away', 'total_pts_away']].drop_duplicates().rename(columns={'team_name_away': 'team_name', 'total_pts_away': 'avg_pts'})

# concatenar y calcular el promedio total
df_combined = pd.concat([df_home, df_away])
df_avg = df_combined.groupby('team_name')['avg_pts'].mean().reset_index()

# ordenar de mayor a menor
df_avg = df_avg.sort_values(by='avg_pts', ascending=False)

# graficar
plt.figure(figsize=(17, 8))
plt.barh(df_avg['team_name'], df_avg['avg_pts'], color='skyblue')
plt.xlabel('Puntos Medios por Partido')
plt.ylabel('Equipo')
plt.title('Puntos Medios por Partido de Cada Equipo (Temporada 2021-2022)')
plt.gca().invert_yaxis()

# guardar la grafica
plt.savefig('puntos_medios_por_equipo.png')
plt.show()