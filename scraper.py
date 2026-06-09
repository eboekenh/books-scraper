#!/usr/bin/env python3
"""
Scrape every book on books.toscrape.com homepage and save to CSV.
"""

import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# ---------------------------------------------------------------------------
# CONFIGURATION

BASE_URL    = "https://books.toscrape.com/"
OUTPUT_FILE = "books.csv"

RATING_MAP = {
    "Zero":  0,
    "One":   1,
    "Two":   2,
    "Three": 3,
    "Four":  4,
    "Five":  5,
}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}

# ---------------------------------------------------------------------------
# FETCHING

def fetch_page(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        print(f"✅ Status: {response.status_code} | Size: {len(response.text):,} chars")
        return response.text
    except requests.RequestException as e:
        print(f"❌ Error fetching page: {e}")
        return None

# ---------------------------------------------------------------------------
# EXTRACTION

def extract_title(card):
    return card.find("h3").find("a")["title"]

def extract_price(card):
    raw = card.find("p", class_="price_color").get_text(strip=True)
    return float(raw.replace("\u00a3", "").replace("£", "").replace("Â", ""))

def extract_rating(card):
    classes = card.find("p", class_="star-rating")["class"]
    word = classes[1]  # e.g. ["star-rating", "Three"] → "Three"
    return RATING_MAP.get(word, 0)

def extract_availability(card):
    return card.find("p", class_="instock availability").get_text(strip=True)

def extract_url(card, base_url):
    relative = card.find("h3").find("a")["href"]
    return urljoin(base_url, relative)

def extract_book(card, base_url):
    return {
        "title":        extract_title(card),
        "price":        extract_price(card),
        "rating":       extract_rating(card),
        "availability": extract_availability(card),
        "url":          extract_url(card, base_url),
    }

# ---------------------------------------------------------------------------
# DISPLAY

def stars(rating):
    return "\u2605" * rating + "\u2606" * (5 - rating)

def print_book_row(index, book):
    title = book["title"][:40].ljust(40)
    print(f"{index:>3}. {title}  £{book['price']:>6.2f}  {stars(book['rating'])}  {book['availability']}")

# ---------------------------------------------------------------------------
# SAVING

def save_to_csv(books, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["title", "price", "rating", "availability", "url"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)
    print(f"\n💾 Saved {len(books)} books to '{path}'")

# ---------------------------------------------------------------------------
# MAIN

def main():
    print("=" * 65)
    print("  📚 books.toscrape.com Scraper")
    print("=" * 65)

    html = fetch_page(BASE_URL)
    if not html:
        return

    soup  = BeautifulSoup(html, "html.parser")
    cards = soup.find_all("article", class_="product_pod")
    print(f"📦 Found {len(cards)} book cards\n")

    books = []
    for i, card in enumerate(cards, start=1):
        book = extract_book(card, BASE_URL)
        print_book_row(i, book)
        books.append(book)

    save_to_csv(books, OUTPUT_FILE)

    # Summary
    avg_price  = sum(b["price"]  for b in books) / len(books)
    avg_rating = sum(b["rating"] for b in books) / len(books)
    print(f"\n📊 Summary")
    print(f"   Total books : {len(books)}")
    print(f"   Avg price   : £{avg_price:.2f}")
    print(f"   Avg rating  : {avg_rating:.1f} / 5")

if __name__ == "__main__":
    main()