import warnings
from statsbombpy import sb

warnings.filterwarnings("ignore", message="credentials were not supplied")

matches = sb.matches(competition_id=2, season_id=27)

for match_id in [3754217, 3754213]:
    info = matches[matches["match_id"] == match_id]
    print(match_id)
    print(info[["home_team", "away_team", "home_score", "away_score"]])