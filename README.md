# Competitor Price Scraping Project

## Project Overview

This project involves developing a web scraper to extract competitor pricing data from multiple online sources. The scraped data is then used to perform Exploratory Data Analysis (EDA) to facilitate decision-making for stakeholders. This project is designed to help businesses understand the competitive landscape and adjust their pricing strategies accordingly.

## Features

- **Web Scraping:** Utilizes BeautifulSoup and Selenium to extract pricing data from various competitor websites.
- **Data Storage:** Stores scraped data in CSV format for easy access and analysis.
- **Exploratory Data Analysis (EDA):** Performs EDA on the collected data to generate insights and support decision-making.

## Technologies Used

- **Programming Language:** Python
- **Web Scraping Libraries:** BeautifulSoup, Selenium
- **Data Analysis Libraries:** pandas, NumPy
- **Data Storage Format:** CSV, JSON

## Project Structure

.
├── config.json                # Configuration file with website URLs and selectors
├── scraper.py                 # Main script for scraping competitor pricing data
├── requirements.txt           # Python dependencies
└── scraping_results/          # Directory where scraped data is stored
    └── competitors_price_<date>.csv



## Usage

1. **Install Dependencies:**
pip install -r requirements.txt

2. **Configure the Scraper:**
- Update the `config.json` file with the target websites and CSS selectors for product data.

3. **Run the Scraper:**
python scraper.py


The scraped data will be saved in the `scraping_results` directory with a date-based filename.

## Future Enhancements

- **Enhanced Data Analysis:** Add more sophisticated EDA techniques to generate deeper insights.
- **Visualization:** Incorporate data visualization tools to present the data in a more intuitive way.
- **Automation:** Schedule the scraper to run periodically and update the data automatically.

## License

This project is not yet open-source.
