import warnings
from statsbombpy import sb
warnings.filterwarnings("ignore",message="credentials were not supplied")
MATCH_ID = 3754217

events=sb.events(match_id=MATCH_ID)
shots=events[events["type"]=="Shot"].copy()

xs=[]
ys=[]

for loc in shots["location"]:
    xs.append(loc[0])
    ys.append(loc[1])
shots["x"] = xs
shots["y"] = ys

shots["is_goal"] = (shots["shot_outcome"] == "Goal").astype(int)

columns = ["team", "minute", "x", "y", "shot_body_part", "shot_type", "play_pattern", "is_goal"]
table = shots[columns]

print(table.head())
print(table.isna().sum())
print(table["shot_body_part"].value_counts())
print(table["shot_type"].value_counts())
print(table[["x", "y"]].describe())