# 📚 Books to Scrape — Python Web Scraper

A beginner-friendly web scraper that extracts all books from [books.toscrape.com](https://books.toscrape.com) and saves the data to a CSV file. Built with `requests`, `BeautifulSoup`, `pandas`, and `matplotlib`.

---

## 🗂️ Project Structure

```
books-scraper/
├── books_scraper.ipynb   # Main Jupyter notebook (scraping + analysis + charts)
├── books.csv             # Output file (generated after running)
├── books_analysis.png    # Charts (generated after running)
└── README.md             # This file
```

---

## 📦 What It Extracts

| Field        | Example                            |
|--------------|------------------------------------|
| Title        | A Light in the Attic               |
| Price        | 51.77                              |
| Rating       | 3                                  |
| Availability | In stock                           |
| URL          | https://books.toscrape.com/...     |

---

## 🚀 How to Run

### Option A — Google Colab (easiest, no setup needed)

1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Click **File → Upload notebook**
3. Upload `books_scraper.ipynb`
4. Click **Runtime → Run all**
5. The CSV will download automatically at the end

### Option B — Locally with Jupyter

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/books-scraper.git
cd books-scraper

# 2. Install dependencies
pip install requests beautifulsoup4 pandas matplotlib notebook

# 3. Launch Jupyter
jupyter notebook books_scraper.ipynb
```

Then run all cells from top to bottom.

---

## 📊 What the Notebook Does

| Step | Description |
|------|-------------|
| 1    | Install & import libraries |
| 2    | Set configuration (URL, headers, rating map) |
| 3    | Fetch the homepage HTML politely |
| 4    | Parse HTML and find all book cards |
| 5    | Define one extraction function per field |
| 6    | Loop all cards and collect data |
| 7    | Load into a pandas DataFrame |
| 8    | Print summary statistics |
| 9    | Plot price & rating charts |
| 10   | Save to `books.csv` |
| 11   | Auto-download on Colab |

---

## 🔑 Key Concepts Covered

- `requests.get()` with headers and timeout
- `response.raise_for_status()` for error handling
- `BeautifulSoup` for HTML parsing
- `find()` and `find_all()` for element selection
- Reading HTML attributes like `title`, `href`, `class`
- `urljoin()` to resolve relative URLs
- `pandas` DataFrame for data analysis
- `matplotlib` for visualization
- `csv` / `pandas` for CSV export

---

## 📈 Sample Output

```
  1. A Light in the Attic               £51.77  ★★★☆☆
  2. Tipping the Velvet                 £53.74  ★☆☆☆☆
  3. Soumission                         £50.10  ★☆☆☆☆
  ...

📊 Summary
   Total books  : 20
   Average price: £35.07
   Average rating: 2.55 / 5
```

---

## 🛠️ Requirements

```
requests
beautifulsoup4
pandas
matplotlib
```

Install all at once:
```bash
pip install requests beautifulsoup4 pandas matplotlib
```

---

## ⚠️ Disclaimer

This scraper targets [books.toscrape.com](https://books.toscrape.com), a website built specifically for scraping practice. Do not use this code on real websites without checking their `robots.txt` and terms of service.

---

## 📄 License

MIT — free to use, modify, and share.
