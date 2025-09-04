import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({
    "mes": [1, 2, 3, 4, 5, 6],
    "ventas": [100, 120, 130, 150, 170, 180]
})

X = df[["mes"]]  
y = df["ventas"]

modelo = LinearRegression()
modelo.fit(X, y)

prediccion = modelo.predict([[7]])
print("Predicción de ventas para el mes 7:", prediccion[0])
