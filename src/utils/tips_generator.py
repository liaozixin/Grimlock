import random
from typing import List

_TIPS_POOL: List[str] = [
    "/help to view all available commands.",
    "/exit to quit Grimlock."
]

def get_random_tip() -> str:
    return random.choice(_TIPS_POOL)