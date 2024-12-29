import os
import numpy as np
import pandas as pd
import pickle
import json
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score
import logging
import yaml
# from dvclive import Live

# Ensure the "logs" directory exists
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

# Logging configuration
logger = logging.getLogger(name='model_evaluation')
logger.setLevel(logging.DEBUG)

# setting up console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# setting up file handler
log_file_path = os.path.join(log_dir, 'model_evaluation.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def load_param(params_path: str) -> dict:
    """
    Load parameters from a YAML file

    Args:
    params_path: str: Path to the YAML file

    Returns:
    dict: Parameters
    """
    try:
        with open(params_path, 'r') as file:
            params = yaml.safe_load(file)

        logger.debug('Parameters retrieved from %s', params_path)
        return params
    except FileNotFoundError:
        logger.error('File not found: %s', params_path)
        raise
    except yaml.YAMLError as e:
        logger.error('YAMLError: %s', e)
        raise
    except Exception as e:
        logger.error('Unexpected Error: %s', e)
        raise


def load_model(file_path: str):
    """Load a trained model from a pickle file"""

    try:
        with open(file_path, 'rb') as file:
            model = pickle.load(file)

        logger.debug('Model loaded from %s', file_path)
        return model
    except FileNotFoundError:
        logger.debug('Model not found at: %s', file_path)
        raise
    except Exception as e:
        logger.error('Unexpected Error while lading the model: %s', e)
        raise


def load_data(file_path: str) -> pd.DataFrame:
    """Load data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        logger.debug('Data loaded from %s', file_path)
        return df
    except pd.errors.ParserError as e:
        logger.error('Failed to parse the CSV file: %s', e)
        raise
    except Exception as e:
        logger.error('Unexpected error occurred while loading the data: %s', e)
        raise


def evaluate_model(clf, X_test: np.ndarray, y_test: np.ndarray) -> dict:
    """Evaluate the model and return a evaluation result"""
    try:
        y_pred = clf.predict(X_test)
        y_pred_proba = clf.predict_proba(X_test)[:, 1]
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_pred)

        metrics_dict = {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'auc': auc
        }
        logger.info('Evaluation Metrcs Claculated')
        return metrics_dict

    except Exception as e:
        logger.error(
            'Unexpected Error occurred while evaluating the model: %s', e)
        raise


def save_metrics(metrics: dict, json_file_path: str) -> None:
    """Save the evaluation metrics to a JSON file."""

    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(json_file_path), exist_ok=True)
        with open(json_file_path, 'w') as file:
            json.dump(metrics, file, indent=4)
        logger.info('Metrics saved to %s', json_file_path)
    except Exception as e:
        logger.error('Failed to save metrics: %s', e)


def main():
    try:
        clf = load_model('./models/model.pkl')
        test_data = load_data('./data/processed/test_tfidf.csv')

        X_test = test_data.iloc[:, :-1].values
        y_test = test_data.iloc[:, -1].values

        metrics = evaluate_model(clf, X_test, y_test)
        save_metrics(metrics, json_file_path='reports/metrics.json')

    except Exception as e:
        logger.error('Failed to complete the model evaluation process: %s', e)
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
