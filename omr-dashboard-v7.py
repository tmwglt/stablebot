from flask import Flask, render_template
import sqlite3
import pytz
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Connect to database
    conn = sqlite3.connect("tokens.db")
    cursor = conn.cursor()

    # Retrieve data from database
    cursor.execute("SELECT * FROM token_data ORDER BY timestamp DESC LIMIT 1")
    data = cursor.fetchone()

    # Close connection
    conn.close()

    # Format USDC balance as dollar amount
    data = "sushiswap has {:,.3f} USDC in its USDC contract wallet".format(data[1] / 10**3)


    return data


if __name__ == '__main__':
    app.run(debug=True)
