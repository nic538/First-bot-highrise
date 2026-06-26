"""
Database management
"""

import logging
import json
import os
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

class Database:
    """Database manager for user data"""
    
    def __init__(self, db_file: str = "data/users.json"):
        self.db_file = db_file
        self.data: Dict[str, Any] = {}
        self._ensure_dir()
    
    def _ensure_dir(self):
        """Ensure data directory exists"""
        os.makedirs(os.path.dirname(self.db_file), exist_ok=True)
    
    async def connect(self):
        """Connect and load data"""
        try:
            if os.path.exists(self.db_file):
                with open(self.db_file, 'r') as f:
                    self.data = json.load(f)
                logger.info(f"Loaded data from {self.db_file}")
            else:
                self.data = {}
                logger.info("Starting with empty database")
        except Exception as e:
            logger.error(f"Error connecting to database: {e}")
            self.data = {}
    
    async def disconnect(self):
        """Save and disconnect"""
        await self.save()
    
    async def save(self):
        """Save data to file"""
        try:
            self._ensure_dir()
            with open(self.db_file, 'w') as f:
                json.dump(self.data, f, indent=2)
            logger.info("Database saved")
        except Exception as e:
            logger.error(f"Error saving database: {e}")
    
    async def get_user_balance(self, user_id: str) -> Optional[float]:
        """Get user balance"""
        user_data = self.data.get(str(user_id))
        return user_data.get('balance') if user_data else None
    
    async def set_user_balance(self, user_id: str, balance: float):
        """Set user balance"""
        user_id = str(user_id)
        if user_id not in self.data:
            self.data[user_id] = {}
        self.data[user_id]['balance'] = balance
        await self.save()
    
    async def get_user_stats(self, user_id: str) -> Dict[str, Any]:
        """Get user statistics"""
        return self.data.get(str(user_id), {})
    
    async def update_user_stats(self, user_id: str, stats: Dict[str, Any]):
        """Update user statistics"""
        user_id = str(user_id)
        if user_id not in self.data:
            self.data[user_id] = {}
        self.data[user_id].update(stats)
        await self.save()
