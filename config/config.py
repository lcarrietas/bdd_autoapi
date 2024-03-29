"""
Config file
"""
import os

TOKEN_TODO = os.getenv("TOKEN")
HEADERS = {
    "Authorization": f"Bearer {TOKEN_TODO}"
}
ABS_PATH = os.path.abspath(__file__ + "../../../")

WEB_HOOK = os.getenv("WEB_HOOK")

BASE_URL = "https://api.todoist.com/rest/v2/"

TOKEN_INFLUX = os.getenv("TOKEN_INFLUX")
