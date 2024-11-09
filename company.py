import requests
from bs4 import BeautifulSoup
import csv

# Function to get company pages from a Wikipedia category
def get_company_urls(category_url):
    # Send HTTP request to the Wikipedia category page
    response = requests.get(category_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all links to company pages
    company_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        # Filter links that go to company pages (Wikipedia pages)
        if href.startswith('/wiki/') and 'List_of' not in href:
            company_links.append('https://en.wikipedia.org' + href)
    
    return company_links

# URL of the Wikipedia category or list of companies
category_url = 'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Companies'

# Get all company page URLs
company_urls = get_company_urls(category_url)

# Save to CSV
with open('company_urls.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Company Name", "URL"])
    for url in company_urls:
        writer.writerow([url.split('/')[-1].replace('_', ' ').title(), url])

print(f"Scraped {len(company_urls)} company URLs.")
