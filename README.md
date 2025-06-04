# Cryptocurrency Liquidity Prediction for Market Stability

This project uses machine learning to predict the **liquidity ratio** of cryptocurrencies based on market data such as price, volume, and volatility. It is designed to help monitor and ensure stability in the crypto market by forecasting potential liquidity risks.

## 📊 Problem Statement

The cryptocurrency market is highly volatile. A drop in liquidity can lead to massive price fluctuations, making it difficult for traders and institutions to operate efficiently. This project aims to:
- Analyze historical market data
- Engineer useful features (moving averages, volatility metrics, etc.)
- Predict the **liquidity ratio** using machine learning (Random Forest Regressor)

## 🛠️ Features

- Data preprocessing and cleaning
- Feature engineering (MA, volatility)
- Model training with Random Forest
- Evaluation using MAE, RMSE, R²
- Final model saved and ready for prediction

## 📁 Project Structure

crypto_liquidity_prediction/
│
├── data/ # Raw and processed datasets
├── notebooks/ # Jupyter notebooks
│ └── crypto_model.ipynb # Full EDA + Model Training notebook
├── models/ # Trained model file (.pkl)
├── README.md # This file
└── requirements.txt # Python dependencies


## 🔍 Model Evaluation

| Metric      | Score     |
|-------------|-----------|
| MAE         | 5.33      |
| RMSE        | 15.69     |
| R² Score    | 0.01      |

*(Model can be improved with more data and hyperparameter tuning.)*

## 📦 Requirements

- Python 3.10+
- pandas, numpy
- scikit-learn
- matplotlib, seaborn
- joblib

Install all dependencies:

```bash
pip install -r requirements.txt
