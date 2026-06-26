#!/usr/bin/env python3
"""
Blackjack Bot for Highrise
Main bot file
"""

import asyncio
import logging
from bot.blackjack_bot import BlackjackBot

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    """Main function to run the bot"""
    try:
        bot = BlackjackBot()
        logger.info("Starting Blackjack Bot...")
        await bot.start()
    except Exception as e:
        logger.error(f"Error starting bot: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    asyncio.run(main())
