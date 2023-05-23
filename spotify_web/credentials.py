"""
General constants for web scraper
"""
import os

# Guide on how to add env. variables on Mac & Linux:
# https://www.youtube.com/watch?v=5iWhQWVXosU

CLIENT_ID = os.environ.get('SP_USER')
CLIENT_SECRET = os.environ.get('SP_PASS')
