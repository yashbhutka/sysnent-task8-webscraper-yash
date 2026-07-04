import requests
from bs4 import BeautifulSoup
import csv

# Target website
url = "https://books.toscrape.com/"

# Send request
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# Open CSV file
with open("data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Write header row
    writer.writerow(["Title"])

    # Extract data (example: all <h2> tags)
    for item in soup.find_all("h3"):
        title = item.text.strip()
        writer.writerow([title])

print("Data saved to data.csv")