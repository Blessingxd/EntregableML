import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("stopwords")

texto1 = "La empresa tuvo un gran crecimiento en sus ventas"
texto2 = "El reporte muestra un incremento positivo en los ingresos"

tokens1 = word_tokenize(texto1.lower())
tokens2 = word_tokenize(texto2.lower())

stop_words = stopwords.words("spanish")
tokens1_limpio = [t for t in tokens1 if t.isalpha() and t not in stop_words]
tokens2_limpio = [t for t in tokens2 if t.isalpha() and t not in stop_words]

print("---Texto 1 limpio---")
print(tokens1_limpio)
print("---Texto 2 limpio---")
print(tokens2_limpio)

palabras_clave = ["crecimiento", "ventas"]

vector1 = [1 if p in tokens1_limpio else 0 for p in palabras_clave]
vector2 = [1 if p in tokens2_limpio else 0 for p in palabras_clave]

print("Vector 1:", vector1)
print("Vector 2:", vector2)
