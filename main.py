import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Authenticate with local JSON
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open Google Sheet
sheet = client.open("MNQ OI Tracker").sheet1

# CME scraping (placeholder until we map HTML)
oi_today = 123456  # Replace with dynamic value
oi_yesterday = int(sheet.cell(2, 2).value)
delta = oi_today - oi_yesterday
bias = "↑ Buildup" if delta > 0 else "↓ Liquidation" if delta < 0 else "Flat"

# Insert row
today = datetime.today().strftime('%Y-%m-%d')
sheet.insert_row([today, oi_today, oi_yesterday, delta, bias], index=2)
print("OI Logged to Sheet.")
