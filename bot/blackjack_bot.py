"""
Main Blackjack Bot class
"""

import logging
from bot.game.blackjack import BlackjackGame
from bot.economy.wallet import WalletManager
from bot.storage.database import Database

logger = logging.getLogger(__name__)

class BlackjackBot:
    """Main bot class for Blackjack"""
    
    def __init__(self):
        """Initialize the bot"""
        self.db = Database()
        self.wallet = WalletManager(self.db)
        self.game = BlackjackGame(self.wallet)
        logger.info("BlackjackBot initialized")
    
    async def start(self):
        """Start the bot"""
        logger.info("Bot started successfully")
        # Main bot loop would go here
        await self.db.connect()
    
    async def stop(self):
        """Stop the bot"""
        await self.db.disconnect()
        logger.info("Bot stopped")
