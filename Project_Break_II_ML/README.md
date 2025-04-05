# Clasificación de Cobertura del Suelo con Random Forest

## 🇲🇽 Español

### Descripción del Proyecto
Este proyecto de Machine Learning tiene como objetivo clasificar diferentes tipos de cobertura del suelo utilizando datos ambientales y topográficos. Se ha empleado el **Forest Cover Type Dataset** para entrenar un clasificador basado en Random Forest. Este proyecto surge del interés en aplicar técnicas de ML en geología y minería, donde la identificación y clasificación del terreno es fundamental para la planificación y gestión ambiental.

### Dataset
- **Nombre:** Forest Cover Type Dataset
- **Fuente:** Kaggle / UCI ML Repository
- **Formato:** CSV
- **Descripción:** Contiene variables geográficas y topográficas (como altitud, pendiente, distancias y tipos de suelo) con la etiqueta `Cover_Type`, que clasifica el tipo de cobertura del suelo en 7 clases.
- **Tamaño:** Aproximadamente 581,012 registros y 55 columnas (dataset completo) / Muestra de 10,000 registros para GitHub.

### Estructura del Proyecto


### Cómo Ejecutar
1. Clona este repositorio.
2. Instala las siguientes librerías:  
   `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `joblib`.
3. Ejecuta el notebook en `src/results_notebook/ML_landcover_classification.ipynb`.
4. El modelo entrenado se guardará en `src/models/random_forest_covertype.pkl`.

### Presentación
- Se ha preparado un video de presentación (máximo 7 minutos) que explica:
  - El problema abordado.
  - El dataset y el proceso de exploración.
  - El desarrollo del modelo de ML y su evaluación.
  - Conclusiones y posibles mejoras.

---

## 🇺🇸 English

### Project Description
This Machine Learning project aims to classify different land cover types using environmental and topographic variables. The **Forest Cover Type Dataset** was used to train a model based on Random Forest. This project is driven by the interest in applying ML techniques in the fields of geology and mining, where identifying and classifying land cover is crucial for environmental planning and management.

### Dataset
- **Name:** Forest Cover Type Dataset
- **Source:** Kaggle / UCI ML Repository
- **Format:** CSV
- **Description:** Contains geographic and topographic features (such as elevation, slope, distances, and soil types) with the `Cover_Type` label that classifies land cover into 7 classes.
- **Size:** Approximately 581,012 records and 55 columns (complete dataset) / A sample of 10,000 records for GitHub.


### How to Run
1. Clone the repository.
2. Install the required libraries:  
   `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `joblib`.
3. Run the notebook located at `src/results_notebook/ML_landcover_classification.ipynb`.
4. The trained model will be saved in `src/models/random_forest_covertype.pkl`.

### Presentation
- A video presentation (maximum 7 minutes) is available that explains:
  - The problem tackled.
  - The dataset and the exploratory process.
  - The development and evaluation of the ML model.
  - Conclusions and possible improvements.


### Project Structure

