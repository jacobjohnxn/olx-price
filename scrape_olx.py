import requests
from bs4 import BeautifulSoup
import csv

def scrape_olx(query, pages=1):
    all_bike_data = []

    for page in range(1, pages + 1):
        url = f'https://www.olx.in/items/q-{query}?page={page}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example of how to find the listings; update class names based on actual OLX page structure
        listings = soup.find_all('div', class_='EIR5N')  # Update the class name as per OLX's current structure
        
        for listing in listings:
            title = listing.find('h6', class_='tFvI7').get_text(strip=True) if listing.find('h6', class_='tFvI7') else 'N/A'
            price_text = listing.find('span', class_='price').get_text(strip=True) if listing.find('span', class_='price') else 'N/A'
            try:
                price = int(price_text.replace('₹', '').replace(',', '').strip())
            except ValueError:
                price = None

            # You may need to scrape additional details like year, condition, etc.
            # For now, we're just using title and price
            all_bike_data.append({
                'title': title,
                'price': price,
                # Add other fields if available
            })

    return all_bike_data

def save_to_csv(data, filename='data.csv'):
    keys = data[0].keys() if data else ['title', 'price']
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

if __name__ == '__main__':
    query = 'bike'  # Adjust the query as needed
    data = scrape_olx(query, pages=5)  # Scrape data from 5 pages
    save_to_csv(data)
    print("Data scraped and saved to data.csv")
