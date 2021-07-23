# "Shopping Cart" Project!

A fun project simulating a Shopping Cart checkout experience at a grocery store. The output display is a receipt of the user's purchase. There is also an additional option to send the receipt as an Email to an Email ID of the user's choice (see below for setup instructions).

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/abhisheksn/shopping-cart) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```
cd ~/Desktop/shopping-cart
```

## Create Environment
Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-env":

```
conda create -n shopping-env python=3.8 #(first time only)
```
```
conda activate shopping-env
```

## Install Packages
After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```
pip install -r requirements.txt
```

## Setup
In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify the prevailing Sales Tax Rate at your location. You can also include the SendGrid API credentials in the same ".env" file:

```
#this is the .env file
#Sales Tax Rate
TAX_RATE=0.0875
```

```
#this is the .env file
#SENDGRID EMAIL Credentials
SENDGRID_API_KEY= "_________________"
SENDER_EMAIL= "________________"
```

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [".gitignore"](/.gitignore) file). This means each person who uses our code needs to create their own local ".env" file.

> NOTE:Follow these [SendGrid setup instructions](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/sendgrid.md#setup) to sign up for a SendGrid account, configure your account's email address (i.e. `SENDER_EMAIL`), and obtain an API key (i.e. `SENDGRID_API_KEY`)

## Run Python Script

```
python shopping-cart.py
```

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment.

## User input
Upon running the Python script, you will be prompted to enter a Product ID between 1 to 20. Please stick to this range of Product IDs. Once all the products have been selected, type 'DONE' to complete the checkout experience.

Once the checkout has been completed and receipt displayed, you will be asked if you want an e-receipt. If you choose "y" then you will be asked to type the Email ID to receive an e-receipt. If you choose "n" then the program will be exited.

> NOTE: If you see an error message, please recheck the SendGrid API account setup and ensure the API Key and Sender Email Address are accurate.

## Further Exploration

<b><i>To run the product list from a ".csv" file</b></i>, instead of a hard-coded set of projects or from a Google Sheet, try the following steps.

1. In the root directory of your repository, create a folder called "data".
2. Add your ".csv" file, with the products information to the "data" folder. You can name the ".csv" file as "products.csv"
3. Update the .gitignore file as follows to ensure your "products.csv" file does not get tracked in version control or uploaded to Github:
   ```
    # this is the .gitignore file
    # ignore the CSV file inventory in the data directory:
    data/products.csv
   ```
4. Now, in the ["shopping-cart.py"](/shopping-cart.py) file, uncomment lines 11 to 16 and comment the lines 42 to 83. Also, ensure lines 19 to 38 are commented.
5. Run the python script and follow the user input steps as stated above.

<b><i>To run the product list from a Google Sheet</b></i>, instead of a hard-coded set of projects or a ".csv" file, try the following steps.

1. Follow [these](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/gspread.md) instructions to setup and obtain your Google API credentials ".json" file
2. Move a copy of the credentials file into your project repository, typically into the root directory or perhaps a directory called "auth", and note its filepath. For the example below, we'll refer to a file called "google-credentials.json" in an "auth" directory (i.e. "auth/google-credentials.json").
3. Finally, before committing, add the credentials filepath to your repository's ".gitignore" file to ensure it does not get tracked in version control or uploaded to GitHub:
    ```
    # this is the .gitignore file
    # ignore the google api credentials file at the following location:
    auth/google-credentials.json
    ```
4. Use this [example](https://docs.google.com/spreadsheets/d/1s28XMh70eUAWOSSYxnBDs3Jng7olQDwIxxe-d8R-d_I/edit?usp=drive_web&ouid=104152363882296967034) Google Sheet, or create your own. Note the document's unique identifier (e.g. 1s28XMh70eUAWOSSYxnBDs3Jng7olQDwIxxe-d8R-d_I) from its URL, and store the identifier in an environment variable called GOOGLE_SHEET_ID.
5. If you create your own, make sure it contains a sheet called "Products-2021" with column headers id, name, department, price, and availability_date. If you choose a different sheet name, customize it via an environment variable called SHEET_NAME. Finally, modify the document's sharing settings to grant "edit" privileges to the "client email" address specified in the credentials file.
    ```
    #this is the .env file
    # Google Auth credentials
    GOOGLE_SHEET_ID= "____________"
    SHEET_NAME= "______________"
    ```
6. Now, in the ["shopping-cart.py"](/shopping-cart.py) file, uncomment lines 19 to 38 and comment the lines 42 to 83. Also, ensure lines 11 to 16 are commented.
7. Run the python script and follow the user input steps as stated above.

> NOTE: I have used the worksheet "Shopping Clean" from the attached Google Sheet for this project and not "Products-2021".
