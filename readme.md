# Web Scraper Project (Currently = mainly for Bama website)


![Python](https://img.shields.io/badge/Python-3.x-blue)
![aiohttp](https://img.shields.io/badge/aiohttp-3.10.1-blue)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.12.3-green)

## Overview
This project is a web scraper that extracts links and titles from specified URLs. The extracted data is saved in JSON format.

## Project Structure
- `main.py`: The main script to run the scraper.
- `scrap.py`: Contains the `Scrape` class which handles the scraping logic.
- `scrawl.py`: Contains additional scraping utilities.
- `urls/`: Directory containing URL settings and configurations.
- `data/links.json`: Stores the extracted links.
- `data/titles.json`: Stores the extracted titles.
- `readme.md`: Project documentation.
## Requirements
- Python 3.x
- pip

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/serene1212/web-scraper.git
    cd web-scraper
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Copy the `sample.env` file to `.env`:
    ```sh
    cp sample.env .env
    ```

2. Edit the `.env` file to specify the categories and brands you want to scrape.

3. Run the scraper:
    ```sh
    python main.py
    ```

## Output
- The extracted links will be saved in `data/links.json`.
- The extracted titles will be saved in `data/titles.json`.

## License
This project is licensed under the [MIT License](LICENSE).