from utils.functions import *
from dotenv import load_dotenv

load_dotenv()

routes = {
    "Dev": "https://awvdev.secure.thorough.care",
    "Stage": "https://groupaco1.secure.thoroughcare.us"
    }


if "ENVIRONMENT" in os.environ:
    environment = os.getenv('ENVIRONMENT')
else:
    environment = get_config("behave", "environment")

base_url = routes[environment]
driver_default = get_config("driver", "default")
