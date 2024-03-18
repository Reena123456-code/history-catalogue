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
    while True:    
        print("please enter catagory, box no, colour, author, title to extend catalogue")
        print("data should be 5 items, seperated by commas")
        print("example: irish, 1,green, tadgh o'Keeffee, early Ireland")

        data_str = input("Enter your book info here: ")

        catalogue_data = data_str.split(",")
    
        if validate_data(catalogue_data):
            print("data valid")
            break

    return catalogue_data

def validate_data(values):
    """
    inside the try, convert string value of number into integer.
    convert string text to list
    or if there are not 5 values
    """
    try:
        class Book:
            def __init__(self, catagory, boxNo, colour, author, title):
                self.catagory = catagory
                self.boxNo = boxNo
                self.colour = colour
                self.author = author
                self.title = title

            def __str__(values):
                return f"{self.catagory},{self.boxNo},{self.colour},{self.author},{self.title}"

        if len(values) != 5:    
           raise ValueError(
            f"5 values required, you provided {len(values)}"
           )
    except ValueError as e:
        print(f"Invalid data:{e}, Please try again\n")
        return False

    return True    


def update_catalogue_worksheet(data):
    """
    update catalogue worksheet, add new row with data given
    """
    print("Updating catalogue worksheet...\n")
    catalogue_worksheet = SHEET.worksheet("catalogue")
    catalogue_worksheet.append_row(data)
    print("Catalogue worksheet updated successfully \n")

    
data = get_catalogue_data()
catalogue_data = (data)
update_catalogue_worksheet(catalogue_data)


