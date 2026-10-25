from statsbombpy import sb

competitions = sb.competitions()

premier = competitions[
    (competitions["competition_name"] == "Premier League")
    & (competitions["season_name"] == "2015/2016")
]
print(premier[["competition_id", "season_id", "season_name"]])

row = premier.iloc[0]
matches = sb.matches(
    competition_id=int(row["competition_id"]),
    season_id=int(row["season_id"]),
)
print("Матчей в сезоне:", len(matches))
print(matches[["match_id", "home_team", "away_team", "home_score", "away_score"]].head())

match_id = int(matches.iloc[0]["match_id"])
events = sb.events(match_id=match_id)
print("События матча (строки, колонки):", events.shape)

shots = events[events["type"] == "Shot"]
print("Ударов в матче:", len(shots))

print(shots.iloc[0])

for sho in shots.columns:
    if sho.startswith("shot"):
        print(sho)
print(shots["shot_outcome"].value_counts())
print((competitions["country_name"]=="Kazakhstan").any())