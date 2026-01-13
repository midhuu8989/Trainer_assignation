from difflib import SequenceMatcher

def fuzzy_match(a: str, b: str) -> bool:
    if not a or not b:
        return False
    return SequenceMatcher(None, a.lower(), b.lower()).ratio() > 0.6
