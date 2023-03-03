from selenium import webdriver
from utils.config import *


class Browser(object):

    drivers = {
        "chrome": ["Chrome", "89.0"],
        "firefox": ["Firefox", "76.0"],
        "edge": ["MicrosoftEdge", "81.0"],
        "safari": ["Safari", "13.0"]
    }

    @classmethod
    def set_up(cls, browser=driver_default, scenario_name="test"):
        try:
            if os.getenv('EXECUTION') == 'local':
                driver = eval("webdriver." + cls.drivers[browser][0] + "()")
            else:
                user_name = os.getenv('USER_NAME')
                grid_url = os.getenv('GRID_URL')
                access_key = os.getenv('ACCESS_KEY')
                remote_url = "http://" + user_name + ":" + access_key + grid_url
                capabilities = {
                    "name": scenario_name,
                    "build": "ThoroughCare-Feb-9",
                    "browserName": cls.drivers[browser][0],
                    "version": cls.drivers[browser][1],
                    "platform": os.getenv('PLATFORM'),
                    "network": False,
                    "visual": False,
                    "video": True,
                    "console": False,
                    "resolution": "1920x1080",
                    "idleTimeout": "270",
                    "timezone": "UTC-05:00"
                }

                driver = webdriver.Remote(command_executor=remote_url,
                                          desired_capabilities=capabilities)
            return driver
        except Exception as e:
            print("error:", e)
