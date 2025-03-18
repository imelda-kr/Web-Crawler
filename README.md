(**ENG**)
# Web Crawler in Python

This project implements a simple **Web Crawler** in Python, which crawls a webpage, fetches its HTML content, and extracts links for further processing.

## How Does It Work?

1. **Connecting to the Server** – The crawler uses a **socket** to send an HTTP request to the web server.
2. **Fetching the HTML Page** – The server returns the HTML code, which the crawler analyzes.
3. **Extracting Links** – The crawler scans the HTML content and extracts all links (`href=...`).
4. **Visiting New Pages** – The crawler repeats the process for each discovered link.
5. **Limit of 50 Pages** – The crawler stops after visiting 50 links.
6. **Filtering Invalid Responses** – If a page does not return **"200 OK"**, it is ignored.

---

## Technologies Used
- Python 3
- Socket library (for network communication)
- Regular expressions (for extracting links)

---

## Project Structure

```
📁 web-crawler
│── crawler.py      # Main script for running the crawler
│── README.md       # Project documentation
```

---

## How to Run?

### 1. Clone the Repository
```sh
 git clone https://github.com/your-github/web-crawler.git
 cd web-crawler
```

### 2. Run the Script
```sh
python crawler.py
```

---

## Configuration
If you want to change the starting page or domain, edit these lines in `crawler.py`:
```python
ip = 'www.optimazadar.hr'  # Host website
page = '1280/djelatnost1280.html'  # Initial subpage
```

---

## Limitations
1. Visits **a maximum of 50 pages**
2. Does not follow links to other domains
3. Ignores pages that do not return **200 OK** status

---

## License
Feel free to use and modify it!

(**HRV**)
# Web Crawler u Pythonu

Ovaj projekt implementira jednostavni **Web Crawler** u Pythonu, koji pretražuje web-stranicu, dohvaća HTML sadržaj i izdvaja linkove za daljnju obradu.

## Kako radi?

1. **Spajanje na server** – Crawler koristi **socket** za slanje HTTP zahtjeva na web server.
2. **Dohvaćanje HTML stranice** – Server vraća HTML kôd koji crawler analizira.
3. **Pretraga linkova** – Iz HTML-a se izdvajaju svi linkovi (href=...).
4. **Posjećivanje novih stranica** – Crawler ponavlja proces za svaki pronađeni link.
5. **Ograničenje od 50 stranica** – Crawler se zaustavlja nakon što posjeti 50 linkova.
6. **Filtriranje neispravnih odgovora** – Ako stranica ne vrati **"200 OK"**, ona se preskače.

---

## Tehnologije korištene
- Python 3
- Socket biblioteka (za mrežnu komunikaciju)
- Regularni izrazi (za prepoznavanje linkova)

---

## Struktura projekta

```
📁 web-crawler
│── crawler.py      # Glavna skripta za pokretanje crawlanja
│── README.md       # Dokumentacija projekta
```

---

## Kako pokrenuti?

### 1. Kloniraj repozitorij
```sh
 git clone https://github.com/tvoj-github/web-crawler.git
 cd web-crawler
```

### 2. Pokreni skriptu
```sh
python crawler.py
```

---

## Podešavanje
Ako želiš promijeniti početnu stranicu ili domenu, u `crawler.py` izmijeni ove linije:
```python
ip = 'www.optimazadar.hr'  # Host stranice
page = '1280/djelatnost1280.html'  # Početna podstranica
```

---

## Ograničenja
1. Posjećuje **maksimalno 50 stranica**
2. Ne prati linkove na druge domene
3. Zanemaruje stranice koje ne vraćaju **200 OK** status

---

## Licenca
 Slobodno koristi i modificiraj kod!

