import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load and prepare data
def load_data(filepath):
    data = pd.read_csv(filepath)
    print("Columns in CSV file:", data.columns)  # Print column names

    # Remove currency symbols and commas, then convert columns to numeric
    data['Price'] = data['Price'].replace({'₹': '', ',': ''}, regex=True).astype(float)
    data['KM Driven'] = data['KM Driven'].replace(',', '', regex=True).astype(float)
    data['Year'] = pd.to_numeric(data['Year'], errors='coerce')

    return data

# Train the model
def train_model(data):
    # Ensure feature names match the prediction input
    X = data[['Year', 'KM Driven']]
    y = data['Price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Mean Squared Error: {mse}")
    return model

# Predict price for new bike
def predict_price(model, km_drive, year):
    new_bike = pd.DataFrame({
        'Year': [year],      # Ensure these column names match the training data
        'KM Driven': [km_drive]
    })
    predicted_price = model.predict(new_bike)
    return predicted_price[0]

# Main function
def main():
    # Load data
    filepath = r"C:\Users\jacob\OneDrive\Desktop\olx\bike_prices.csv"
    data = load_data(filepath)
    
    # Train model
    model = train_model(data)
    
    # Get user input
    km_drive = float(input("Enter the kilometers driven on the new bike: "))
    year = int(input("Enter the year of the new bike: "))
    
    # Predict price
    predicted_price = predict_price(model, km_drive, year)
    print(f"Predicted Price for the new bike: Rs{predicted_price:.2f}")

if __name__ == "__main__":
    main()
