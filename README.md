# Company URL Scraper

This Python script scrapes a list of company pages from Wikipedia and saves their URLs into a CSV file. It focuses on extracting company names and their corresponding Wikipedia URLs from the [Wikipedia:WikiProject Companies](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Companies) page.

## Requirements

To run this script, you will need to have the following Python packages installed:

- `requests` - For sending HTTP requests to fetch the Wikipedia page.
- `beautifulsoup4` - For parsing and extracting data from the HTML content.
- `csv` - For writing the extracted URLs into a CSV file.

You can install the required packages using `pip`:

```bash
pip install requests beautifulsoup4
```

## How It Works

1. **Fetch Wikipedia Page**:  
   The script sends an HTTP request to the Wikipedia page for the category of companies:  
   `https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Companies`.

2. **Extract Links**:  
   It parses the page's HTML to find all the links that lead to individual company pages. The script filters out links that are part of "List_of" pages, as they aren't individual companies.

3. **Save to CSV**:  
   The URLs of the company pages are saved into a CSV file (`company_urls.csv`), where each row contains the company name and URL.

## Usage

1. Download the script (e.g., `company_scraper.py`) and run it from your terminal:
   ```bash
   python company_scraper.py
   ```

2. The script will output the total number of scraped company URLs and create a `company_urls.csv` file containing the company names and their URLs.

3. The CSV file will have the following format:
   ```
   Company Name, URL
   Apple, https://en.wikipedia.org/wiki/Apple
   Google, https://en.wikipedia.org/wiki/Google
   Microsoft, https://en.wikipedia.org/wiki/Microsoft
   ...
   ```

## Example Output

After running the script, you'll see the following printed in the terminal:
```
Scraped 50 company URLs.
```

A `company_urls.csv` file will be generated in the same directory containing the URLs of company pages from Wikipedia.
![image](https://github.com/user-attachments/assets/8caef7d6-2bd2-4221-91c8-61fbc761ad83)
