from products import Product, add_product, products
from data_handler import create_dataframe, predict_best_price


def main():

    df = create_dataframe(csv_file="products.csv")  # Assuming this function returns a DataFrame
    category_to_check = input("Which Category: ").capitalize()  # Define or get this value as needed
    best_price = predict_best_price(df, category_to_check)
    print(f"The best price for {category_to_check} is: {best_price}")

if __name__ == "__main__":
    main()
