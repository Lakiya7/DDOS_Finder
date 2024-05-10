import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load

class DatasetLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        df = pd.read_csv(self.file_path)
        return df

    def clean_data(self, df):
        # Replace inf/-inf with NaN
        df.replace([np.inf, -np.inf], np.nan, inplace=True)

        # Select only numeric columns for mean replacement
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

        # Clip numeric columns to ensure no entry exceeds float64 limits
        max_float64 = np.finfo(np.float64).max
        df[numeric_cols] = df[numeric_cols].clip(lower=-max_float64, upper=max_float64)

        return df

class ModelTrainer:
    def __init__(self):
        self.pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
        ])

    def train_model(self, X_train, y_train):
        self.pipeline.fit(X_train, y_train)

    def save_model(self, filename):
        dump(self.pipeline, filename)

    def load_model(self, filename):
        self.pipeline = load(filename)

class ModelPredictor:
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def predict(self, X_test):
        return self.pipeline.predict(X_test)

class AlertGenerator:
    def __init__(self):
        self.alerts = []

    def generate_alert(self, attack_details):
        alert = {
            'timestamp': pd.Timestamp.now(),
            'severity': attack_details.get('severity', 'high'),
            'affected_devices': attack_details.get('affected_devices', []),
            'description': attack_details.get('description', 'DDoS attack detected')
        }
        self.alerts.append(alert)
        return alert
