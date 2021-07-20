import pymongo

mongo_db_username = 'student'
mongo_db_password = 'PqyqrY2aEC22B5SB'
mongo_db_database = 'stock-prices'

## instantiate an instance of MongoClient
client = pymongo.MongoClient(f"mongodb+srv://{mongo_db_username}:{mongo_db_password}@cluster0-ya1yr.mongodb.net/{mongo_db_database}?retryWrites=true")

## connect to a db and store in variable []_db
stocks_db = client[mongo_db_database] 

## connect to a collection in the database called 'prices' 
prices_collection = stocks_db.prices ## collection = db['prices']

# write your queries here
## Warmup
# 1. List all entries in the prices collection in the stock-prices database.
# 2. List all historical Microsoft stock prices
# 3. List all historical stock prices from 2004
# 4. List all historical stock prices from September
# 5. List all historical stock prices from September 2004
# 6. List all historical stock prices in order from lowest value to highest value
# 7. List all historical stock prices in order from highest value to lowest value
# 8. List the first 5 historical stocks in the database.
# 9. Find an historical stock that was valued at $100.52.
# 10. How many entries are there in the database for Apple stock prices?
## Showtime
# 11. List the first 10 Apple entries in the database.
# 12. List the January IBM stock prices from lowest to highest.
# 13. List all historical stock prices over $200.00
# 14. List all historical stock prices less than $10.00.
# 15. What company's (or companies') stock was valued at $9.78 in October, 2000? Return only the name of the company.
# 16. What was the price of Amazon's Stock in August, 2006? Return only the price.
# 17. What was the highest historical price of Microsoft's stock? Return only the price.
# 18. For how many months (in the historical database) has Apple's stock price been greater than $100.00? Return only the number of months.