import argparse
import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier

def model_fn(model_dir):
    return joblib.load(os.path.join(model_dir, "model.joblib"))

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--output-data-dir", type=str, default=os.environ.get('SM_OUTPUT_DATA_DIR'))
    parser.add_argument("--model-dir", type=str, default=os.environ.get('SM_MODEL_DIR'))
    parser.add_argument("--train", type=str, default=os.environ.get('SM_CHANNEL_TRAIN'))

    args = parser.parse_args()

    # Load data
    df = pd.read_csv(os.path.join(args.train, "cleaned.csv"))
    X = df.drop(["customer_ID", "churned"], axis=1)
    y = df["churned"]

    # Train a simple model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)

    # Save the model
    joblib.dump(model, os.path.join(args.model_dir, "model.joblib"))

if __name__ == "__main__":
    main()