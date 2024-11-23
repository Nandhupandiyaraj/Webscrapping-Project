Project Overview

This project is a web scraping tool designed to extract news articles from the Times of India website. The script fetches the headline, publication date, and content of a specific news article and organizes the data into a structured format using Python libraries.
Features

    Web Scraping: Extracts key information (headline, date, and content) from a news article.
    Libraries Used:
        requests for fetching webpage content.
        BeautifulSoup (from bs4) for parsing HTML content.
        pandas for organizing and displaying data.
        lxml as the parser for BeautifulSoup.
    Output: The data is stored in a pandas DataFrame, making it easy to manipulate or save to a file.

Installation

    Clone or download the repository.
    Install the required Python libraries using pip:

    pip install requests beautifulsoup4 pandas lxml

Usage

    Open the Times New Web Scrapping.py file.
    Ensure the URL of the desired news article is set in the url variable:

url = requests.get('<article_url>')

Run the script:

    python Times\ New\ Web\ Scrapping.py

    The extracted data (headline, date, content) will be displayed in a pandas DataFrame.
Input

URL:
https://timesofindia.indiatimes.com/elections/lok-sabha-elections/uttar-pradesh/news/priyanka-salutes-congress-cadre-hails-their-courage-in-toughest-of-times/articleshow/110774557.cms
Output
Headline	Date	Content
Priyanka salutes Congress cadre...	November 23, 2024	The article's full content extracted from URL.
Customization

    To scrape a different news article, replace the URL in the url variable.
    To save the extracted data to a file, add the following code:

    df.to_csv('output.csv', index=False)

Limitations

    This script is designed specifically for the Times of India website and may require modifications for other websites.
    The script relies on the structure and class names of the website's HTML. Any changes to the website's structure may break the scraper.