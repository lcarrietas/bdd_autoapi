"""
Config file
"""
import os

TOKEN_TODO = os.getenv("TOKEN")
HEADERS = {
    "Authorization": f"Bearer {TOKEN_TODO}"
}
ABS_PATH = os.path.abspath(__file__ + "../../../")

BASE_URL = "https://api.todoist.com/rest/v2/"
