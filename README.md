# 🌬️ Air Quality Index (AQI) Prediction

A Machine Learning project focused on predicting the **Air Quality Index (AQI)** using historical air pollution data from various cities across India. Includes an interactive **Streamlit Web Application** for real-time predictions.

🌐 **Live Demo:** [Launch Air Quality Prediction App](https://airqualityprediction-a7ccrwxvnqrhdts93havbt.streamlit.app/)

---

## 📌 Project Overview

Air pollution is a major environmental issue affecting public health. This project analyzes atmospheric pollutant levels and builds predictive Machine Learning models to accurately forecast the AQI.

### Key Features
- **Exploratory Data Analysis (EDA)** and pollutant trend visualizations.
- Preprocessing pipeline handling missing values and feature scaling.
- Evaluation and comparison of multiple regression algorithms.
- Interactive Streamlit dashboard for real-time user input and AQI estimation.

---

## 📊 Dataset Parameters

The dataset is sourced from Kaggle's [Air Quality Data in India](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india).

| Feature Category | Atmospheric Pollutants & Indicators |
| :--- | :--- |
| **Particulate Matter** | PM2.5, PM10 |
| **Inorganic Gases** | NO, NO2, NOx, NH3, CO, SO2, O3 |
| **Volatile Organic Compounds (VOCs)** | Benzene, Toluene, Xylene |
| **Target Variable** | **AQI** (Air Quality Index) |

---

## 🤖 Machine Learning Models & Metrics

The project implements and compares the following algorithms:
- **Linear Regression**
- **Decision Tree Regressor**
- **Random Forest Regressor**

### Performance Metrics
- **MAE** (Mean Absolute Error)
- **RMSE** (Root Mean Squared Error)
- **R² Score**

---

## 🛠️ Technologies Used

- **Language:** Python
- **Data Manipulation:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-Learn
- **Web Framework:** Streamlit
- **Environment:** Jupyter Notebook

---

## 💻 Local Setup & Installation

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/harshkumar6581/Air_Quality_Prediction.git](https://github.com/harshkumar6581/Air_Quality_Prediction.git)
   cd Air_Quality_Prediction
