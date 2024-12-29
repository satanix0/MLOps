import os
import logging
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string
import nltk
nltk.download('stopwords')
nltk.download('punkt')

# Ensure the "logs" directory exists
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

# Logger Configuration
logger = logging.getLogger(name='data_preprocessing')
logger.setLevel('DEBUG')

# Setting up console handler
console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

# Setting up file handler
log_file_path = os.path.join(log_dir, 'data_preprocessing.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

# Formatting log messages
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def transform_text(text):
    """
    Transforms the input text by performing several preprocessing steps:
    1. Converts the text to lowercase.
    2. Tokenizes the text into individual words.
    3. Removes non-alphanumeric tokens.
    4. Removes stopwords and punctuation.
    5. Applies stemming to the words.
    6. Joins the processed tokens back into a single string.
    
    Args:
        text (str): The input text to be transformed.
    Returns:
        str: The transformed text after preprocessing.
    """

    ps = PorterStemmer()
    # Convert to lowercase
    text = text.lower()
    # Tokenize the text
    text = nltk.word_tokenize(text)
    # Remove non-alphanumeric tokens
    text = [word for word in text if word.isalnum()]
    # Remove stopwords and punctuation
    text = [word for word in text if word not in stopwords.words(
        'english') and word not in string.punctuation]
    # Stem the words
    text = [ps.stem(word) for word in text]
    # Join the tokens back into a single string
    return " ".join(text)


def preprocess_df(df, text_column='text', target_column='target'):
    """
    Parameters:
    df (pd.DataFrame): The input DataFrame to preprocess.
    text_column (str): The name of the column containing text data to be transformed. Default is 'text'.
    target_column (str): The name of the column containing target labels to be encoded. Default is 'target'.

    Returns:
    pd.DataFrame: The preprocessed DataFrame with encoded target column, duplicates removed, and transformed text column.

    Raises:
    KeyError: If the specified text_column or target_column is not found in the DataFrame.

    """
    try:
        logger.debug('Starting preprocessing for DataFrame')
        # Encode the target column
        encoder = LabelEncoder()
        df[target_column] = encoder.fit_transform(df[target_column])
        logger.debug('Target column encoded')

        # Remove duplicate rows
        df = df.drop_duplicates(keep='first')
        logger.debug('Duplicates removed')

        # Apply text transformation to the specified text column
        df.loc[:, text_column] = df[text_column].apply(func=transform_text)
        logger.debug('Text column transformed')
        return df

    except KeyError as e:
        logger.error('Column not found: %s', e)
        raise
    except Exception as e:
        logger.error('Error during text normalization: %s', e)
        raise


def main(text_column='text', target_column='target'):
    """
    Main function to load raw data, preprocess it, and save the processed data.
    """
    try:
        # Fetch the data from data/raw
        train_data = pd.read_csv('./data/raw/train.csv')
        test_data = pd.read_csv('./data/raw/test.csv')
        logger.debug('Data loaded properly')

        # Transform the data
        train_processed_data = preprocess_df(
            train_data, text_column, target_column)
        test_processed_data = preprocess_df(
            test_data, text_column, target_column)

        # Store the data inside data/processed
        data_path = os.path.join("./data", "interim")
        os.makedirs(data_path, exist_ok=True)

        train_processed_data.to_csv(os.path.join(
            data_path, "train_processed.csv"), index=False)
        test_processed_data.to_csv(os.path.join(
            data_path, "test_processed.csv"), index=False)

        logger.debug('Processed data saved to %s', data_path)
    except FileNotFoundError as e:
        logger.error('File not found: %s', e)
    except pd.errors.EmptyDataError as e:
        logger.error('No data: %s', e)
    except Exception as e:
        logger.error(
            'Failed to complete the data transformation process: %s', e)
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
