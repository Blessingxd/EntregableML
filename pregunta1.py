import pandas as pd
import numpy as np

df = pd.DataFrame({
    "empresa": ["A", "B", "C", "D"],
    "precio": [100, 120, 90, 150],
    "ventas": [50, 70, 30, 80]
})

print("Columna precio:")
print(df["precio"])

df["ingresos"] = df["precio"] * df["ventas"]
print("DataFrame con ingresos:")
print(df)

print("Empresas con ingresos > 8000:")
print(df[df["ingresos"] > 8000])
