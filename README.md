# Audible Web Scraper

## Overview

This Python script is designed to scrape book data (title and author) from the Audible website's charts page. It uses the `requests` library to fetch the HTML content and `BeautifulSoup` to parse the HTML and extract the relevant information. The scraped data is then saved to a CSV file.

## Features

* Scrapes book titles and authors from Audible's best-selling charts.
* Handles potential errors during the scraping process (e.g., network errors, changes in website structure).
* Saves the scraped data to a CSV file.
* Includes logging for better error handling and debugging.
* Cleans author names by removing the "By:" prefix.
