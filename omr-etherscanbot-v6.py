import requests
import json
import time
import sqlite3

# Set API key and contract address
api_key = "PJWHHSP4CRUSQ5CJKZUXMSZD3GJ6IK2BR8"
contract_address = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"

# Set address of the wallet you want to check
wallet_address = "0x397ff1542f962076d0bfe58ea045ffa2d347aca0"

# Connect to database and create table
conn = sqlite3.connect("tokens.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS token_data (timestamp INTEGER, num_tokens INTEGER)")

# Run indefinitely
while True:
    # Send request to Etherscan API
    url = "https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress={}&address={}&tag=latest&apikey={}".format(contract_address, wallet_address, api_key)
    response = requests.get(url)

    # Check for errors
    if response.status_code != 200:
        raise ValueError("Error: API request unsuccessful")

    # Extract number of tokens from response
    data = response.json()
    num_tokens = data['result']

    # Get current timestamp
    timestamp = int(time.time())

    # Insert data into table
    cursor.execute("INSERT INTO token_data VALUES (?, ?)", (timestamp, num_tokens))

    # Commit changes
    conn.commit()

    # Sleep for 10 seconds
    time.sleep(10)

# Close connection
conn.close()
