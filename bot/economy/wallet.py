"""
Wallet and economy management
"""

import logging
from typing import Optional

logger = logging.getLogger(__name__)

class WalletManager:
    """Manages user wallets and economy"""
    
    STARTING_BALANCE = 1000
    
    def __init__(self, database):
        self.db = database
    
    async def get_balance(self, user_id: str) -> float:
        """Get user balance"""
        try:
            balance = await self.db.get_user_balance(user_id)
            return balance if balance is not None else self.STARTING_BALANCE
        except Exception as e:
            logger.error(f"Error getting balance for {user_id}: {e}")
            return 0
    
    async def add_balance(self, user_id: str, amount: float) -> bool:
        """Add balance to user"""
        try:
            current = await self.get_balance(user_id)
            new_balance = current + amount
            await self.db.set_user_balance(user_id, new_balance)
            return True
        except Exception as e:
            logger.error(f"Error adding balance for {user_id}: {e}")
            return False
    
    async def subtract_balance(self, user_id: str, amount: float) -> bool:
        """Subtract balance from user"""
        try:
            current = await self.get_balance(user_id)
            if current < amount:
                logger.warning(f"Insufficient balance for {user_id}")
                return False
            new_balance = current - amount
            await self.db.set_user_balance(user_id, new_balance)
            return True
        except Exception as e:
            logger.error(f"Error subtracting balance for {user_id}: {e}")
            return False
