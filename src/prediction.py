import joblib
import pandas as pd

# Load the trained model
model = joblib.load("src/house_price_model.pkl")

# Load feature columns
feature_columns = joblib.load("src/feature_columns.pkl")


print("\n======================================")
print("       SMART HOUSE PRICE PREDICTOR")
print("======================================")

# Get house details
area = float(input("Enter house area (sq ft): "))
bedrooms = int(input("Enter number of bedrooms: "))
bathrooms = int(input("Enter number of bathrooms: "))
parking = int(input("Enter number of parking spaces: "))


# Location selection
print("\nAvailable Locations")
print("-------------------")
print("1. Berhampur")
print("2. Bhubaneswar")
print("3. Cuttack")
print("4. Puri")

location_choice = int(input("Choose location (1-4): "))


locations = {
    1: "Berhampur",
    2: "Bhubaneswar",
    3: "Cuttack",
    4: "Puri"
}


# Check location
if location_choice not in locations:
    print("\nInvalid location choice.")
    exit()


location = locations[location_choice]


# Create house data
input_data = {
    "area_sqft": area,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "parking": parking
}


# Add location columns
for loc in locations.values():

    column_name = "location_" + loc

    if loc == location:
        input_data[column_name] = 1
    else:
        input_data[column_name] = 0


# Convert to DataFrame
input_data = pd.DataFrame([input_data])


# Arrange columns in the same order as the model
input_data = input_data[feature_columns]


# Make prediction
predicted_price = model.predict(input_data)[0]


# Display result
print("\n======================================")
print("           PREDICTION RESULT")
print("======================================")

print("Area       :", area, "sq ft")
print("Bedrooms   :", bedrooms)
print("Bathrooms  :", bathrooms)
print("Parking    :", parking)
print("Location   :", location)

print("--------------------------------------")

print("Predicted Price : ₹", round(predicted_price, 2))
print("Price in Lakhs  : ₹", round(predicted_price / 100000, 2), "Lakh")

print("======================================")
print("       Thank you for using the")
print("       Smart House Price Predictor!")
print("======================================")