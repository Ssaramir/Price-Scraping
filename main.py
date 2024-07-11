import os 
import subprocess
from datetime import datetime




current_date = datetime.now().strftime("%Y-%m-%d")
filename = f"Competitors_price_{current_date}.csv"
filepath = os.path.join("scraping_results", filename)


# Run the Scraper script
subprocess.run(["python", "scraper.py"])


# Run the Exploratory Data Analysis
# subprocess.run(["python", "eda.py"])