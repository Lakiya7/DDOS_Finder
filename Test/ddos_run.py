import unittest
import pandas as pd
import numpy as np
from ddos_finder import DatasetLoader

class TestDatasetLoader(unittest.TestCase):
    def setUp(self):
        # Ensure the CSV file path is correct
        self.loader = DatasetLoader('Dataset_scan.csv')

    def test_load_data(self):
        df = self.loader.load_data()
        self.assertIsInstance(df, pd.DataFrame)

    def test_clean_data(self):
        df = self.loader.load_data()
        cleaned_df = self.loader.clean_data(df)
        numeric_cols = cleaned_df.select_dtypes(include=[np.number]).columns
        self.assertFalse(np.isnan(cleaned_df[numeric_cols]).any().any())

if __name__ == '__main__':
    unittest.main()
