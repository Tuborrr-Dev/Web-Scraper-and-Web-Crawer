# Web Scraper Project

## Overview

This Python project is a web scraper designed to extract quotes, authors, and tags from the "Quotes to Scrape" website ([http://quotes.toscrape.com](http://quotes.toscrape.com)). The scraped data is then stored in an Excel file for further analysis or usage.

## Features

- **Web Scraping**: Automatically crawls through multiple pages of the website to extract quotes, authors, and associated tags.
- **Data Storage**: Saves the extracted data into an Excel file (`Quotes-Scraped.xlsx`) using the pandas library.
- **Pagination Handling**: Dynamically handles pagination by identifying and navigating to the next page of quotes until all pages have been scraped.
- **Error Handling**: Includes robust error handling for network timeouts, missing elements, and other potential issues during web scraping.

## Technologies Used

- **Python**: Programming language used for the entire project.
- **BeautifulSoup**: Python library for parsing HTML and XML documents, essential for web scraping.
- **pandas**: Library for data manipulation and analysis, used for creating and managing data in DataFrame format.
- **requests**: Python library for making HTTP requests, used for fetching web pages.
- **xlsxwriter**: Python library for writing Excel files, used via pandas for storing scraped data.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Tuborrr-Dev/Web-Scraper-and-Web-Crawer.git
