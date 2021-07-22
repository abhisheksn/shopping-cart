# "Shopping Cart" Project!

A fun project simulating a Shopping Cart checkout experience at a grocery store. The output display is a receipt of the user's purchase. There is also an additional option to send the receipt as an email to an email ID of the user's choice (see below for setup instructions).

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
#Sales Tax Rate
TAX_RATE=0.0875
```

```
#SENDGRID EMAIL Credentials
SENDGRID_API_KEY="_________________"
SENDER_EMAIL="________________"
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

Once the checkout has been completed and receipt displayed, you will be asked to type the Email ID to receive an e-receipt. A output of '202' refers to the being successfully sent.

> NOTE: If you see an error message, please recheck the SendGrid API account setup and ensure the API Key and Sender Email Address are accurate.

## Further Exploration

To run the product list from a ".csv" file, instead of a hard-coded set of projects, try the following steps.

1. In the root directory of your repository, create a folder called "data".
2. Add your ".csv" file, with the products information to the "data" folder. You can name the ".csv" file as "products.csv"
3. Update the .gitignore file as follows to ensure your "products.csv" file does not get uploaded to version control
   ```
    # ignore the CSV file inventory in the data directory:
    data/products.csv
   ```
4. Now, in the ["shopping-cart.py"](/shopping-cart.py) file, uncomment lines 9 to 16 and comment the lines 20 to 61.
5. Run the python script and follow the user input steps as stated above.
