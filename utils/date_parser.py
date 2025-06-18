import re
from datetime import datetime, date, timedelta
from dateutil import parser as date_parser
from typing import Optional, Tuple

class AdvancedDateParser:
    def __init__(self):
        self.today = date.today()
        
    def parse_complex_date(self, text: str) -> Optional[date]:
        """Handle complex date expressions"""
        text = text.lower().strip()
        
        # Relative dates
        if "next week" in text:
            days_ahead = 7
            if "late" in text:
                days_ahead += 3  # Go to Thursday/Friday of next week
            elif "early" in text:
                days_ahead += 1  # Go to Tuesday of next week
            return self.today + timedelta(days=days_ahead)
        
        # Specific patterns
        patterns = {
            r"tomorrow": lambda: self.today + timedelta(days=1),
            r"day after tomorrow": lambda: self.today + timedelta(days=2),
            r"this (monday|tuesday|wednesday|thursday|friday|saturday|sunday)": self._parse_this_weekday,
            r"next (monday|tuesday|wednesday|thursday|friday|saturday|sunday)": self._parse_next_weekday,
            r"in (\d+) days?": lambda match: self.today + timedelta(days=int(match.group(1))),
            r"(\d+) days? from now": lambda match: self.today + timedelta(days=int(match.group(1))),
        }
        
        for pattern, handler in patterns.items():
            match = re.search(pattern, text)
            if match:
                try:
                    return handler(match) if callable(handler) else handler()
                except:
                    continue
        
        # Try standard date parsing
        try:
            parsed = date_parser.parse(text, fuzzy=True)
            return parsed.date()
        except:
            pass
        
        return None
    
    def _parse_this_weekday(self, match):
        """Parse 'this Monday', 'this Friday', etc."""
        weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        target_weekday = weekdays.index(match.group(1))
        current_weekday = self.today.weekday()
        
        days_ahead = target_weekday - current_weekday
        if days_ahead <= 0:  # If it's today or past, go to next week
            days_ahead += 7
            
        return self.today + timedelta(days=days_ahead)
    
    def _parse_next_weekday(self, match):
        """Parse 'next Monday', 'next Friday', etc."""
        weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        target_weekday = weekdays.index(match.group(1))
        current_weekday = self.today.weekday()
        
        days_ahead = target_weekday - current_weekday + 7  # Always next week
        return self.today + timedelta(days=days_ahead)