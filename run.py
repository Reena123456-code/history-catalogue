import gspread
from google.oauth2.service_account import Credentials

SCOPE =[
    "https://googleapis.com/auth/spreadsheets",
    "https://googleapis.com//auth/drive.file",
    "https://googleapis.com/auth/drive"
]

CREDS =Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
#SHEET - GSPREAD_CLIENT.open('history-catalogue')

from tabulate import tabulate
data = [
    ["Castles",	1,	"Yellow", "Tadhg O'Keeffe", "Medieval Ireland: An Archaeology"],
    ["Castles",	1,	"Yellow", "Tadhg O'Keeffe",	"Barryscourt Castle And The Irish Tower-House"],
    ["Castles",	1,	"Yellow", "Tadhg O'Keeffe",	"Medieval Ireland: The Barryscourt Lectures I -X"],
    ["Castles",	1,	"Yellow", "Mairead Ashe FitzGerald", "Castles Of Ireland"],
    ["Castles",	1,	"Yellow", "Conleth Manning", "From Ringforts To Fortified Houses Studies On Castles"],
    ["Castles",	2,	"Yellow", "H.G Leask", "Irish Castles"],
    ["Castles",	2,	"Yellow", "David Sweetnam",	"The Medieval Castles Of Ireland"],
    ["Castles", 2,	"Yellow", "Thomas Johnson Westropp", "Fortified Headlands & Castles, & Coast Of Munster"],
    ["Castles",	2,	"Yellow", "J.E Kaufmann", "The Medieval Fortress"],
    ["Castles",	2,	"Yellow", "Mark Samuel Wycliffe", "The Tower Houses Of  West Cork"],
    ["Castles",	3,	"Yellow", "Marc Morris", "Castle: A History Of The Buildings That Shaped Medieval Britain"],
    ["Castles",	3,	"Yellow", "Bill Wilsdon", "Plantation Castles On The Erne"],
    ["Castles",	3,	"Yellow", "Rodney Castleden", "Castles Of Britain And Ireland"],
    ["Castles",	3,	"Yellow", "Charles Philips", "The Medieval Castle: Design, Construction, Daily Life"],
    ["Archaeology",	1, "Light Blue", "Geraldine T. Sprout",	"Archaeological Survey Of The Barony Of Ikerrin"],
    ["Archaeology",	1, "Light Blue", "A. O'Sullivan, R. Sands & Kelly",	"Coolure Demesne Crannog Derravaragh An Introduction To Archaeology And Landscapes"],
    ["Archaeology",	1, "Light Blue", "Christine Baker",	"The Archaeology Of Killeen Castle Co. Meath"],
    ["Archaeology",	1, "Light Blue", "Tom Fourwinds", "Monu-mental About Prehistoric Antrim"],
    ["Archaeology",	1, "Light Blue", "Tadhg O'Keeffe", "Ireland's Round Towers"],
    ["Archaeology",	1, "Light Blue", "Brian Lalor",	"The Irish Round Towers Origin And Architecture"],
    ["Maynooth Research Guides", 1,	"Light Green", "Susan M. Parkes", "A Guide To Sources For The History Of Irish Education 1780-1922"],
    ["Maynooth Research Guides", 1,	"Light Green", "C.J. Woods", "Travellers' Accounts As Source - Material For Irish Historians"],
    ["Maynooth Research Guides", 1,	"Light Green", "Tadhg O'Keeffe", "Medieval Irish Buildings 1100 -1600"],
    ["Maynooth Research Guides", 1,	"Light Green", "Frances McGee",	"The Archives Of The Valuation Of Ireland 1830 - 1865"],
    ["Maynooth Research Guides", 1,	"Light Green", "Ciaran & Margaret O'hOgartaigh", "Business Achival Sources For Local Historian"],
]
headers = ["Catagory", "Box No.", "Color", "Author", "Title"]
table = tabulate(data, headers=headers, tablefmt="grid")
print(table)