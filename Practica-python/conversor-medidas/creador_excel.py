import pandas as pd

# Dataframe la informacion basica con las piezas y centimentros para armar el excel

data = {
    "Piezas": ['Pata','Tablero','Puerta','Estante','Panel'],
    "Centimetros": [40,120,80,64,105]
}


df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel

df.to_excel('muebles_medidas.xlsx', index=False)