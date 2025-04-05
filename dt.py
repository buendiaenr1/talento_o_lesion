# para instalar
# python -m venv sklearn-env
# sklearn-env\Scripts\activate  # activate
# pip install -U scikit-learn



# en dos usar sklearn-env\Scripts\activate  
# para que funcione

from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
import numpy as np

# Datos simulados: [velocidad, fuerza, coordinación, fatiga]
datos = np.array([
    [5.0, 80, 7, 2],  # Atleta normal
    [6.5, 92, 8, 1],  # Talento potencial
    [4.8, 75, 6, 3],  # Atleta normal
    [5.2, 85, 5, 7],  # Riesgo de lesión (fatiga alta)
    [7.0, 95, 9, 1],   # Talento excepcional
    [5.0, 80, 7, 2],  # Atleta normal
    [6.5, 94, 8, 1],  # Talento potencial
    [4.8, 75, 6, 3],  # Atleta normal
    [5.2, 85, 5, 7],  # Riesgo de lesión (fatiga alta)
    [7.0, 95, 9, 1],   # Talento excepcional
    [5.0, 80, 7, 2],  # Atleta normal
    [6.5, 91, 8, 1],  # Talento potencial
    [4.8, 75, 6, 3],  # Atleta normal
    [5.2, 85, 5, 6],  # Riesgo de lesión (fatiga alta)
    [5.2, 85, 5, 7],  # Riesgo de lesión (fatiga alta)
    [5.2, 80, 5, 6],  # Riesgo de lesión (fatiga alta)
    [7.0, 95, 9, 1]   # Talento excepcional
])

# Entrenar Isolation Forest
modelo = IsolationForest(contamination=0.3, random_state=42)  # Ajustamos contamination para capturar más anomalías
modelo.fit(datos)

# Predecir anomalías
predicciones = modelo.predict(datos)

# Separar anomalías de datos normales
anomalias = datos[predicciones == -1]  # Anomalías detectadas
normales = datos[predicciones == 1]    # Datos normales

print(f"Total de anomalías detectadas: {len(anomalias)}")
print(f"Total de datos normales: {len(normales)}")

# Aplicar K-Means a las anomalías para clasificarlas en dos grupos: talentos y riesgos de lesión
if len(anomalias) > 0:
    kmeans = KMeans(n_clusters=2, random_state=42)  # Dividimos en 2 clusters
    clusters = kmeans.fit_predict(anomalias)        # Asignamos cada anomalía a un cluster

    # Interpretar clusters
    for i, cluster in enumerate(clusters):
        if anomalias[i][-1] <= 3:  # Si la fatiga es baja, probablemente sea un talento
            etiqueta = "Talento"
        else:  # Si la fatiga es alta, probablemente sea un riesgo de lesión
            etiqueta = "Riesgo de lesión"
        print(f"Anomalía {i+1}: Cluster {cluster} ({etiqueta}) - Datos: {anomalias[i]}")
else:
    print("No se detectaron anomalías.")