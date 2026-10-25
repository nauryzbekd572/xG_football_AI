import warnings
from statsbombpy import sb

warnings.filterwarnings("ignore", message="credentials were not supplied")
MATCH_ID = 3754217
events=sb.events(match_id=MATCH_ID)
shots=events[events["type"]=="Shot"]

print("Ударов всего:",len(shots))
print(shots["team"].value_counts())
shots["is_goal"] = (shots["shot_outcome"] == "Goal").astype(int)
print(shots["is_goal"].value_counts())
goals = shots[shots["is_goal"] == 1]
own_goals = events[events["type"].str.contains("Own Goal")]
print(own_goals[["type", "team", "player", "minute"]])