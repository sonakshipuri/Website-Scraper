import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_audible_data(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        html_content = response.text

        soup = BeautifulSoup(html_content, "html.parser")

        book_listings = soup.find_all("div", class_="bc-col-7")
        all_books_data = []

        for book_listing in book_listings:
            title_element = book_listing.find("li", class_="bc-list-item").find("h3", class_="bc-heading").find("a", class_="bc-link bc-color-link")
            author_element = book_listing.find("li", class_="bc-list-item authorLabel")

            title = title_element.get_text(strip=True) if title_element else None
            author = author_element.get_text(strip=True) if author_element else None
            if author and author.startswith("By:"):
                author = author[len("By:"):].strip()

            book_data = {
                "Title": title,
                "Author": author,
            }
            all_books_data.append(book_data)
        return all_books_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []
    except Exception as e:
        print(f"An error occurred during scraping: {e}")
        return []


def write_to_csv(data, filename="audible_books.csv"):
    if not data:
        print("No data to write to CSV.")
        return

    fieldnames = list(data[0].keys())

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data written to {filename}")



target_url = "https://www.audible.com/charts/best"
book_data = scrape_audible_data(target_url)
if book_data:
    write_to_csv(book_data)
