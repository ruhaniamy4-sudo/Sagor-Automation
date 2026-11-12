import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PORT = int(os.getenv("PORT", 5000))
    FB_PAGE_ACCESS_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN")
    FB_VERIFY_TOKEN = os.getenv("FB_VERIFY_TOKEN")
    STEADFAST_API_KEY = os.getenv("STEADFAST_API_KEY")
    STEADFAST_SECRET_KEY = os.getenv("STEADFAST_SECRET_KEY")
    STEADFAST_BASE_URL = os.getenv(
        "STEADFAST_BASE_URL", "https://portal.packzy.com/api/v1"
    )
