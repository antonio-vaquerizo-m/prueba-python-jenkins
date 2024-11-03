import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle

#Read global variables
RAW_DATA_DIR = '/workspace/MLOps-Docker-Jenkins/raw_data'
RAW_DATA_FILE = 'heart.csv'
PROCESSED_DATA_DIR = '/workspace/MLOps-Docker-Jenkins/processed_data'

# Set path for the input
raw_data_path = os.path.join(RAW_DATA_DIR, RAW_DATA_FILE)

# Read dataset
data = pd.read_csv(raw_data_path, sep=",")

# Drop useless variables
X = data.drop(['target'], axis='columns')
y = data['target'].to_frame()

train, test = train_test_split(data, test_size=0.3, stratify=data['target'])

# Set path to the outputs
train_path = os.path.join(PROCESSED_DATA_DIR, 'train.csv')
test_path = os.path.join(PROCESSED_DATA_DIR, 'test.csv')

# Save csv
train.to_csv(train_path, index=False)
test.to_csv(test_path,  index=False)