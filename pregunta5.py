import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    "mes": ["Ene","Feb","Mar","Abr","May"],
    "ventas": [100, 120, 140, 160, 180]
})

plt.plot(df["mes"], df["ventas"])
plt.title("Tendencia de ventas")
plt.xlabel("Meses")
plt.ylabel("Ventas")
plt.show()
