"""
Configuration file for Blackjack Bot
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class"""
    
    # Bot settings
    BOT_TOKEN = os.getenv('BOT_TOKEN', '')
    
    # Highrise settings
    HIGHRISE_API_URL = os.getenv('HIGHRISE_API_URL', 'https://api.highrise.game')
    
    # Database settings
    DB_PATH = os.getenv('DB_PATH', 'data/users.json')
    
    # Game settings
    STARTING_BALANCE = int(os.getenv('STARTING_BALANCE', 1000))
    MIN_BET = int(os.getenv('MIN_BET', 10))
    MAX_BET = int(os.getenv('MAX_BET', 10000))
    
    # Debug mode
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
