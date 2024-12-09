import pandas as pd


def cm_a_pulgadas(cm):
    return cm / 2.54


# leer el archivo excel
df = pd.read_excel("muebles_medidas.xlsx")

# añadir una columna al DataFrame que sea en pulgadas
df["Pulgadas"] = df["Centimetros"].apply(cm_a_pulgadas)

df.to_excel("mueble_medidas_convertidas.xlsx", index=False)

print('Conversion Completada.')