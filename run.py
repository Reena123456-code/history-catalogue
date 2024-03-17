import gspread
import pandas
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE) 
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('history-catalogue1')


def get_catalogue_data():
    """
    Get catalogue data input from the user
    """ 
    print("please enter catagory, box no, colour author, title to extend catalogue")
    print("data should be 6 items, seperated by commas")
    print("example: irish, 1,green, tadgh o'Keeffee, early Ireland")

    data_str = input("Enter your book info here: ")

    catalogue_data = data_str.split(",")
    validate_data(catalogue_data)

def validate_data(values):
    """
    inside the try, convert string value of number into integer.
    convert string text to list
    or if there are not 5 values
    """
    try:
        if len(values) != 5:    
           raise ValueError(
            f"5 values required, you provided {len(values)}"
           )
    except ValueError as e:
        print(f"Invalid data:{e}, Please try again\n")


get_catalogue_data()


