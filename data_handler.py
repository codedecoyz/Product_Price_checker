import pandas as pd
from models import train_model

def create_dataframe(csv_file):
    df = pd.read_csv(csv_file)
    train_model(df)  # Train the model when creating the DataFrame
    return df

def predict_best_price(df, category):
    # Implement your logic here
    # For example, returning the minimum price for the given category
    best_price = df[df['category'] == category]['price'].min()
    return best_price
