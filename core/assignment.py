import pandas as pd
from core.validation import fuzzy_match

def match_trainer(module: str, tech: str, trainers: pd.DataFrame):
    for _, t in trainers.iterrows():
        if fuzzy_match(module, str(t.get("Acquired Skill", ""))) or fuzzy_match(tech, str(t.get("Acquired Skill", ""))):
            return t["Coach Name"]
    return None
