import pandas as pd

data = {
    "piezas" : ["pata", "Tablero", "Puerta", "Estante", "Panel Lateral"],
    "Centimetros" : [40, 120, 60, 30, 180],
}

df = pd.DataFrame(data)

#Guardar el dataframe en un archivo excel

df.to_excel("muebles_medidas.xlsx", index=False)