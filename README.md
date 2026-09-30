# 🚗 Used Car Price Prediction – Web Scraping + Machine Learning

An end-to-end mini pipeline that scrapes used-car listings from TrueCar, stores them in a MariaDB database, and predicts a car's price from its mileage and model year using a Decision Tree.

## How It Works
```
TrueCar listings ──► BeautifulSoup scraper ──► MariaDB (cars table) ──► Decision Tree ──► Price prediction
```
1. **Scraping** – collects name, mileage, year and price from ~100 listing pages
2. **Storage** – cleans the values with regex and inserts them into MariaDB
3. **Training** – filters records by the car model the user enters
4. **Prediction** – user inputs mileage and year; the model returns an estimated price

## Tech Stack
Python · Requests · BeautifulSoup · Regex · MariaDB · scikit-learn

## Database Setup
```sql
CREATE DATABASE python;
USE python;

CREATE TABLE cars (
    id    INT AUTO_INCREMENT PRIMARY KEY,
    name  VARCHAR(255),
    miles INT,
    year  INT,
    price INT
);
```

## Getting Started
```bash
git clone https://github.com/<your-username>/car-price-prediction.git
cd car-price-prediction
pip install requests beautifulsoup4 mariadb scikit-learn
```
Set your database credentials in the script, then run:
```bash
python predict_car_price.py
```

### Example
```
Enter Your Car name : Toyota Camry
Miles : 45000
Year : 2018
Price : 18500 $
```

## Notes
- TrueCar's HTML structure may change over time; CSS selectors may need updating.
- Scraping should respect the website's terms of service and `robots.txt`.

## Future Improvements
- Replace `DecisionTreeClassifier` with a regression model (e.g. `DecisionTreeRegressor`, Random Forest)
- Load database credentials from environment variables
- Use parameterised SQL queries
- Separate scraping, training and prediction into modules

## Author
**Alireza Esmaeili**
