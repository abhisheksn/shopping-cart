import os
from pandas import read_csv
from dotenv import load_dotenv  # source:https://github.com/theskumar/python-dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}"  # > $12,000.71

csv_filepath = "data/products.csv"

products_df = read_csv("data/products.csv")
products = products_df.to_dict("records")

load_dotenv()
selected_ids = []
total_price = 0

tax_rate = os.getenv("TAX_RATE", default=0.0875)

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
  print("+ " + matching_prod["name"] +
        " (" + to_usd(matching_prod["price"]) + ")")
print("---------------------------------")
print("Subtotal:", to_usd(total_price))
print("Tax:", to_usd(tax))
print("Total:", to_usd(Total))
print("---------------------------------")
print("Thank you, see you again soon!")
print("---------------------------------")
user_email = input("Please enter your email:")

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL")


def send_email(subject="[Daily Briefing] This is a test", html="<p>Hello World</p>", recipient_address=SENDER_EMAIL_ADDRESS):
    """
    Sends an email with the specified subject and html contents to the specified recipient,

    If recipient is not specified, sends to the admin's sender address by default.
    """
    client = SendGridAPIClient(
        SENDGRID_API_KEY)  # > <class 'sendgrid.sendgrid.SendGridAPIClient>
    print("CLIENT:", type(client))
    print("SUBJECT:", subject)
    #print("HTML:", html)

    message = Mail(from_email=SENDER_EMAIL_ADDRESS,
                   to_emails=user_email, subject=subject, html_content=html)
    try:
        response = client.send(message)
        # > <class 'python_http_client.client.Response'>
        print("RESPONSE:", type(response))
        print(response.status_code)  # > 202 indicates SUCCESS
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
