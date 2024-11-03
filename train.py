import pandas as pd

import json
import os
from joblib import dump
import pickle

from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Read global variables
PROCESSED_DATA_DIR = '/workspace/MLOps-Docker-Jenkins/processed_data'
MODEL_DIR = '/workspace/MLOps-Docker-Jenkins/models'
RESULTS_DIR = '/workspace/MLOps-Docker-Jenkins/results'

# Set path to inputs
train_data_file = 'train.csv'
train_data_path = os.path.join(PROCESSED_DATA_DIR, train_data_file)

# Read data
df = pd.read_csv(train_data_path, sep=",")

# Split data into dependent and independent variables
# Drop useless variables
X_train = df.drop(['target'], axis='columns')
y_train = df['target']


# Model 
logit_model = LogisticRegression(max_iter=10000)
logit_model = logit_model.fit(X_train, y_train)

# Cross validation
cv = StratifiedKFold(n_splits=3) 
val_logit = cross_val_score(logit_model, X_train, y_train, cv=cv).mean()

# Validation accuracy to JSON
train_metadata = {
    'validation_acc': val_logit
}


# Set path to output (model)

model_name = 'logit_model.joblib'
model_path = os.path.join(MODEL_DIR, model_name)

# Serialize and save model
dump(logit_model, model_path)


# Set path to output (metadata)
train_results_file = 'train_metadata.json'
results_path = os.path.join(RESULTS_DIR, train_results_file)

# Serialize and save metadata
with open(results_path, 'w') as outfile:
    json.dump(train_metadata, outfile)
