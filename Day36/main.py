import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla, Inc."
PERCENTAGE_THRESHOLD = 5  # Alert threshold (5%)

# API Endpoints
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Get environment variables
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
YOUR_PHONE = os.getenv("YOUR_PHONE")


def get_stock_data():
    """Fetch stock data from Alpha Vantage API"""
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": STOCK_API_KEY,
    }
    response = requests.get(STOCK_ENDPOINT, params=params)
    response.raise_for_status()
    return response.json()


def get_news_articles():
    """Fetch news articles related to the company"""
    params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "pageSize": 3,  # Get top 3 articles
        "sortBy": "publishedAt",
    }
    response = requests.get(NEWS_ENDPOINT, params=params)
    response.raise_for_status()
    return response.json().get("articles", [])


def send_sms(message):
    """Send SMS via Twilio"""
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=message,
        from_=TWILIO_PHONE,
        to=YOUR_PHONE
    )
    print(message.sid)
    return message.sid



def main():
    try:
        # Get stock data
        stock_data = get_stock_data()
        time_series = stock_data["Time Series (Daily)"]
        sorted_dates = sorted(time_series.keys(), reverse=True)

        # Get latest two trading days
        latest_day = sorted_dates[0]
        previous_day = sorted_dates[1]

        # Calculate percentage difference
        latest_close = float(time_series[latest_day]["4. close"])
        previous_close = float(time_series[previous_day]["4. close"])
        percentage_diff = ((latest_close - previous_close) / previous_close) * 100

        print(f"Price change: {percentage_diff:.2f}%")

        # Check if change exceeds threshold (fixed logic)
        if abs(percentage_diff) > PERCENTAGE_THRESHOLD:
            # Get news articles
            articles = get_news_articles()

            # Determine direction (up/down)
            direction = "🔺" if percentage_diff > 0 else "🔻"

            # Format and send messages
            for article in articles:
                message = (
                    f"{STOCK_NAME}: {direction}{abs(round(percentage_diff))}%\n"
                    f"Headline: {article.get('title', 'No Title')}\n"
                    f"Brief: {article.get('description', 'No Description')}"
                )
                print(f"Sending SMS:\n{message}")
                send_sms(message)


    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()