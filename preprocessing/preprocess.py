import pandas as pd
import os

def main():
    input_path = "/opt/ml/processing/input/data.csv"
    output_dir = "/opt/ml/processing/output"
    output_path = os.path.join(output_dir, "cleaned.csv")

    print("📥Reading input file", input_path)
    df = pd.read_csv(input_path)

    print("Original data shape:", df.shape)

    # Example cleaning: drop rows with NULL and normalize income
    df = df.dropna()
    if "income" in df.columns:
        df["income"] = df["income"] / 1000 # convert to K

    os.makedirs(output_dir, exist_ok=True)
    print("Saving the cleaned data to:", output_path)
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    main()