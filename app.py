from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import re

def build_inverted_index():
    return {
        "price": "span[data-aut-id='itemPrice']",
        "title": "span[data-aut-id='itemTitle']",
        "details": "span[data-aut-id='itemDetails']"
    }

def extract_year_and_km(details_text):
    year = "N/A"
    km = "N/A"
    
    year_match = re.search(r'\b(19|20)\d{2}\b', details_text)
    if year_match:
        year = year_match.group()
    
    km_match = re.search(r'(\d{1,3}(?:,\d{3})*)\s*km', details_text, re.IGNORECASE)
    if km_match:
        km = km_match.group(1)
    
    return year, km

def scrape_olx_bike_prices(bike_names):
    firefox_options = Options()
    # Uncomment the line below if you want to run in headless mode
    # firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(options=firefox_options)
    base_url = "https://www.olx.in/items/q-{}"
    bike_data = []
    inverted_index = build_inverted_index()

    for bike_name in bike_names:
        search_url = base_url.format(bike_name.replace(" ", "-"))
        driver.get(search_url)
        
        try:
            # Wait for the items to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, inverted_index["title"]))
            )
            
            # Extract data using the inverted index
            title_elements = driver.find_elements(By.CSS_SELECTOR, inverted_index["title"])
            price_elements = driver.find_elements(By.CSS_SELECTOR, inverted_index["price"])
            details_elements = driver.find_elements(By.CSS_SELECTOR, inverted_index["details"])
            
            for title_elem, price_elem, details_elem in zip(title_elements, price_elements, details_elements):
                title = title_elem.text.strip()
                price = price_elem.text.strip()
                details = details_elem.text.strip()
                year, km = extract_year_and_km(details)
                bike_data.append([bike_name, title, price, year, km])
                
        except Exception as e:
            print(f"Error scraping data for {bike_name}: {e}")
        
        time.sleep(2)  # Small delay between searches

    driver.quit()

    # Save data to CSV
    with open('bike_prices.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Search Query", "Bike Title", "Price", "Year", "KM Driven"])
        writer.writerows(bike_data)

    print(f"Data has been saved to bike_prices.csv")

if __name__ == "__main__":
    bike_names = input("Enter bike names separated by commas: ").split(',')
    bike_names = [name.strip() for name in bike_names]  # Clean up extra spaces
    scrape_olx_bike_prices(bike_names)