import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

model = LinearRegression()

def train_model(df):
    df['category_encoded'] = df['category'].astype('category').cat.codes
    X = df[['category_encoded']]
    y = df['price']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)

def predict_best_price(df, category):
    category_code = pd.Series([category]).astype('category').cat.codes[0]
    predicted_price = model.predict([[category_code]])
    return predicted_price[0]
