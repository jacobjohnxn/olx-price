# OLX Price Prediction using Web Scraping

This project uses web scraping to predict the selling price of items (such as bikes) by gathering similar listings from OLX. The prediction is based on user input, including the item name, kilometers driven, location, and year of purchase.

## Description

The OLX Price Prediction app utilizes web scraping techniques with Selenium to extract data from OLX listings. By analyzing listings similar to the user's input, the app estimates a fair selling price. The project is particularly useful for individuals looking to sell items like bikes, as it predicts a competitive price based on real market data.

## Features

- Web scraping of OLX listings based on user inputs
- Prediction of selling prices for items like bikes
- User inputs include item name, kilometers driven, location, and year of buying
- Data storage in CSV for future reference

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Selenium
- Firefox browser
- Geckodriver (for Selenium)
- Other required Python libraries (listed in `requirements.txt`)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/olx-price-prediction.git
   
   ```

    Navigate to the project directory:

cd olx-price-prediction
```bash
cd olx-price-prediction
```
Install the required packages:
    Download and set up Geckodriver:
        Make sure Geckodriver is installed and added to your system PATH.
        You can download it from: https://github.com/mozilla/geckodriver/releases

Edit the app to suit your needs:
        If necessary, modify app.py to customize scraping logic or prediction algorithms.

Running the Application

    Run the app:

```bash
    python app.py
```
Input details:
        Enter the item name (e.g., Bike Name)
        Enter the kilometers driven
        Enter the location
        Enter the year of purchase

  Prediction:
        The app will scrape OLX for similar listings and predict an appropriate selling price for the input item based on the data retrieved.

Example Usage

Suppose you want to sell a bike:

    Bike Name: Yamaha FZ
    KM Driven: 20,000 km
    Location: Delhi
    Year of Buying: 2018

After inputting this data, the app will predict a competitive price by scraping similar bikes listed on OLX.
Project Structure

bash

├── app.py                    # Main script that runs the web scraper and predicts prices
├── requirements.txt           # Required Python packages
├── README.md                  # Project documentation
├── bike_prices.csv            # CSV file to store scraped data

Notes

    Make sure that the OLX website is accessible from your location, as it may block requests based on region or excessive scraping activity.
    Depending on the website structure, you may need to update the selectors in app.py.
