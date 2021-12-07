import os
from dotenv import load_dotenv
import cloudinary

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
api_secret = os.getenv('API_SECRET')
api_key = os.getenv('API_KEY')
FAUNA_KEY = os.getenv('FAUNA_KEY')
# configure cloudinary
cloudinary.config(
    cloud_name="BotFather",
    api_key=api_key,
    api_secret=api_secret
)
# fauna client config
client = FaunaClient(secret=FAUNA_KEY)

# Define Options
CHOOSING, CLASS_STATE, SME_DETAILS, CHOOSE_PREF, \
    SME_CAT, ADD_PRODUCTS, SHOW_STOCKS, POST_VIEW_PRODUCTS = range(8)