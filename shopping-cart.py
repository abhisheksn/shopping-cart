# shopping_cart.py
import os
from dotenv import load_dotenv  # source:https://github.com/theskumar/python-dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime

load_dotenv()

#If running CSV uncomment lines 9 to 16
#from pandas import read_csv

#csv_filepath = "data/products.csv"

#products_df = read_csv("data/products.csv")
#products = products_df.to_dict("records")

#Hard Coded list of products
#If running CSV comment lines 20 to 61
products = [
    {"id": 1, "name": "Chocolate Sandwich Cookies",
        "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id": 2, "name": "All-Seasons Salt", "department": "pantry",
        "aisle": "spices seasonings", "price": 4.99},
    {"id": 3, "name": "Robust Golden Unsweetened Oolong Tea",
        "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id": 4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce",
        "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id": 5, "name": "Green Chile Anytime Sauce", "department": "pantry",
        "aisle": "marinades meat preparation", "price": 7.99},
    {"id": 6, "name": "Dry Nose Oil", "department": "personal care",
        "aisle": "cold flu allergy", "price": 21.99},
    {"id": 7, "name": "Pure Coconut Water With Orange",
        "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id": 8, "name": "Cut Russet Potatoes Steam N' Mash",
        "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id": 9, "name": "Light Strawberry Blueberry Yogurt",
        "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id": 10, "name": "Sparkling Orange Juice & Prickly Pear Beverage",
       "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id": 11, "name": "Peach Mango Juice", "department": "beverages",
        "aisle": "refrigerated", "price": 1.99},
    {"id": 12, "name": "Chocolate Fudge Layer Cake",
        "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id": 13, "name": "Saline Nasal Mist", "department": "personal care",
        "aisle": "cold flu allergy", "price": 16.00},
    {"id": 14, "name": "Fresh Scent Dishwasher Cleaner",
        "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id": 15, "name": "Overnight Diapers Size 6",
        "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id": 16, "name": "Mint Chocolate Flavored Syrup",
        "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id": 17, "name": "Rendered Duck Fat", "department": "meat seafood",
        "aisle": "poultry counter", "price": 9.99},
    {"id": 18, "name": "Pizza for One Suprema Frozen Pizza",
        "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id": 19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend",
        "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id": 20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink",
        "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]  # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#Converting numeric value to USD formatted string
#source: Professor Rossetti
def to_usd(my_price):
    return f"${my_price:,.2f}"  # > $12,000.71

# Python Script

selected_ids = []
total_price = 0

#Alter the tax rate by creating a .env file
# source:https://github.com/theskumar/python-dotenv
tax_rate = os.getenv("TAX_RATE", default=0.0875)

#Obtaining the date and time for printing receipt
# source:https://www.programiz.com/python-programming/datetime/current-datetime
now = datetime.today()
dt_string = now.strftime("%Y/%m/%d %I:%M %p")

while True:
  selected_id = input("Please enter a Product ID (1-20) or type 'DONE':")
  if selected_id == "DONE":
    break
  else:
    selected_ids.append(selected_id)

print("---------------------------------")
print("Cartaway")
print("www.cartaway.com")
print("---------------------------------")
print("Checkout at:", dt_string)
print("---------------------------------")
print(f"You have selected {len(selected_ids)} products:")
for selected_id in selected_ids:
  prod = [x for x in products if str(x["id"]) == str(selected_id)]
  matching_prod = prod[0]
  total_price = total_price + matching_prod["price"]
  tax = (total_price * float(tax_rate))
  Total = (total_price + tax)
  print("+ " + matching_prod["name"] + " (" + to_usd(matching_prod["price"]) + ")")
print("---------------------------------")
print("Subtotal:", to_usd(total_price))
print("Tax:", to_usd(tax))
print("Total:", to_usd(Total))
print("---------------------------------")
print("Thank you, see you again soon!")
print("---------------------------------")
user_input = input("Do you want an e-receipt ('y'/'n')?:")
if user_input == "n":
    exit()
else:
    user_email = input("Please enter your Email address:")

#source: code from https://github.com/abhisheksn/daily-briefings-py
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL")

def send_email(subject="[Daily Briefing] This is a test", html="<p>Hello World</p>", recipient_address=SENDER_EMAIL_ADDRESS):
    client = SendGridAPIClient(SENDGRID_API_KEY)  # > <class 'sendgrid.sendgrid.SendGridAPIClient>
    #print("HTML:", html)
    message = Mail(from_email=SENDER_EMAIL_ADDRESS,
                   to_emails=user_email, subject=subject, html_content=html)
    try:
        response = client.send(message)
        print("Email Successfully delivered")  # > 202 indicates SUCCESS
        return response
    except Exception as e:
        print("OOPS", type(e), e)
        return None

if __name__ == "__main__":
 html = ""
 html += f"<h3>Your e-receipt from Cartaway!</h3>"
 html += "<img src = https://www.shareicon.net/data/128x128/2016/05/04/759867_food_512x512.png>"
 html += f"<h3>Shopping date: {dt_string}</h3>"

 html += f"<h4>You selected {len(selected_ids)} products:</h4>"
 html += "<ul>"
 for selected_id in selected_ids:
    prod = [x for x in products if str(x["id"]) == str(selected_id)]
    matching_prod = prod[0]
    html += f"<li> {matching_prod['name']} ({to_usd(matching_prod['price'])})</li>"
 html += "</ul>"

 html += "<ul>"
 html += f"<li>Subtotal: {to_usd(total_price)}</li>"
 html += f"<li>Tax: {to_usd(tax)}</li>"
 html += f"<li>Total: {to_usd(Total)}</li>"
 html += "</ul>"

 html += f"<h3> Thanks for shopping with Cartaway. See you again soon!</h3>"

send_email(subject="Cartaway receipt", html=html)
