import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

TropicalExcel = pd.read_excel('Registros Tropical Detox.xlsx')

FiltrarDatos = TropicalExcel.loc[:202,['Jugo','Sabor','Textura']]

Frutas = FiltrarDatos['Jugo'].value_counts()

def NumSabor(row):
      if row['Sabor'] == 'Dulce':
        return 1
      elif row['Sabor'] == 'Ácido':
        return 2
      elif row['Sabor'] == 'Tropical':
        return 3
      elif row['Sabor'] == 'Intenso':
        return 4
      elif row['Sabor'] == 'Exótico':
        return 5
      elif row['Sabor'] == 'Jugoso':
        return 6
      elif row['Sabor'] == 'Ligero':
        return 7
      elif row['Sabor'] == 'Refrescante':
        return 8
      elif row['Sabor'] == 'Natural':
        return 9
      elif row['Sabor'] == 'Cítrico':
        return 10
      elif row['Sabor'] == 'Agrio':
        return 11
FiltrarDatos['NumeroSabor'] = FiltrarDatos.apply(NumSabor, axis = 1)

Textura = FiltrarDatos['Textura'].value_counts()

#Reemplazar El nombre de la textura por un numero
FiltrarDatos['Textura'] = FiltrarDatos['Textura'].replace('Cremosa',1)
FiltrarDatos['Textura'] = FiltrarDatos['Textura'].replace('Crispy',2)
FiltrarDatos['Textura'] = FiltrarDatos['Textura'].replace('Suave',3)
FiltrarDatos['Textura'] = FiltrarDatos['Textura'].replace('Refrescante',4)
FiltrarDatos['Textura'] = FiltrarDatos['Textura'].replace('Pulposo',5)
FiltrarDatos['Textura'] = FiltrarDatos['Textura'].replace('Jugosa',6)
FiltrarDatos['Textura'] = FiltrarDatos['Textura'].replace('Gelatinosa',7)
FiltrarDatos['Textura'] = FiltrarDatos['Textura'].replace('Fibrosa',8)
FiltrarDatos['Textura'] = FiltrarDatos['Textura'].replace('Pulposa',9)

#Reemplazar el nombre del jugo por un numero
FiltrarDatos['Jugo'] = FiltrarDatos['Jugo'].replace('Uva',1)
FiltrarDatos['Jugo'] = FiltrarDatos['Jugo'].replace('Sandía',2)
FiltrarDatos['Jugo'] = FiltrarDatos['Jugo'].replace('Piña',3)
FiltrarDatos['Jugo'] = FiltrarDatos['Jugo'].replace('Pera',4)
FiltrarDatos['Jugo'] = FiltrarDatos['Jugo'].replace('Naranja',5)
FiltrarDatos['Jugo'] = FiltrarDatos['Jugo'].replace('Melocotón',6)
FiltrarDatos['Jugo'] = FiltrarDatos['Jugo'].replace('Maracuyá',7)
FiltrarDatos['Jugo'] = FiltrarDatos['Jugo'].replace('Manzana',8)
FiltrarDatos['Jugo'] = FiltrarDatos['Jugo'].replace('Mandarina',9)
FiltrarDatos['Jugo'] = FiltrarDatos['Jugo'].replace('Limón',10)
FiltrarDatos['Jugo'] = FiltrarDatos['Jugo'].replace('Kiwi',11)
FiltrarDatos['Jugo'] = FiltrarDatos['Jugo'].replace('Guayaba',12)
FiltrarDatos['Jugo'] = FiltrarDatos['Jugo'].replace('Fresa',13)
FiltrarDatos['Jugo'] = FiltrarDatos['Jugo'].replace('Frambuesa',14)
FiltrarDatos['Jugo'] = FiltrarDatos['Jugo'].replace('Durazno',15)
FiltrarDatos['Jugo'] = FiltrarDatos['Jugo'].replace('Arándano',16)
FiltrarDatos['Jugo'] = FiltrarDatos['Jugo'].replace('Mango',18)
FiltrarDatos['Jugo'] = FiltrarDatos['Jugo'].replace('Cereza',19)

FiltrarDatos = FiltrarDatos.drop(['Sabor'], axis = 1)

FiltrarDatos.columns = ['Jugo', 'Textura', 'Sabor']

# Convertir la columna 'Jugo' a tipo float
FiltrarDatos['Jugo'] = FiltrarDatos['Jugo'].astype(int)

# Crear la columna "promedio"
FiltrarDatos['promedio'] = (FiltrarDatos['Jugo'] + FiltrarDatos['Textura'] + FiltrarDatos['Sabor']) / 2

# Seleccionar las variables relevantes para la regresión
variables = ['Sabor', 'Textura','Jugo']

# Comenta la variable de arriba y descomenta la variable de abajo si quieres quitar el jugo
# variables = ['Sabor', 'Textura']

X = FiltrarDatos[variables]
y = FiltrarDatos['promedio']

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de regresión lineal
model = LinearRegression()
# Entrenar el modelo
model.fit(X_train, y_train)
# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Realizar una predicción
def prediccion(nmat, nlecto, apoyo):
    pred = model.predict([[nmat, nlecto, apoyo]])
    return pred
# Sin Jugo
# def prediccion(nmat, nlecto, ):
#     pred = model.predict([[nmat, nlecto]])
#     return pred

def recomendar_jugo(promedio):
    if 1 <= promedio < 2:
        return 'Uva'
    elif 2 <= promedio < 3:
        return 'Sandía'
    elif 3 <= promedio < 4:
        return 'Piña'
    elif 4 <= promedio < 5:
        return 'Pera'
    elif 5 <= promedio < 6:
        return 'Naranja'
    elif 6 <= promedio < 7:
        return 'Melocotón'
    elif 7 <= promedio < 8:
        return 'Maracuyá'
    elif 8 <= promedio < 9:
        return 'Manzana'
    elif 9 <= promedio < 10:
        return 'Mandarina'
    elif 10 <= promedio < 11:
        return 'Limón'
    elif 11 <= promedio < 12:
        return 'Kiwi'
    elif 12 <= promedio < 13:
        return 'Guayaba'
    elif 13 <= promedio < 14:
        return 'Fresa'
    elif 14 <= promedio < 15:
        return 'Frambuesa'
    elif 15 <= promedio < 16:
        return 'Durazno'
    elif 16 <= promedio < 17:
        return 'Arándano'
    elif 17 <= promedio < 18:
        return 'Mango'
    elif 18 <= promedio < 19:
        return 'Cereza'
    else:
        return 'No se encontró una recomendación de jugo'
