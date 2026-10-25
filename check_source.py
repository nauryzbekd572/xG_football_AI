from statsbombpy import sb
competititons=sb.competitions()
print("Размер таблицы:",competititons.shape)
print("Колонки:",competititons.columns.to_list())
print(competititons[["country_name","competition_name","season_name"]].head(10))
print("Страны:", competititons["country_name"].unique())
print(competititons["competition_name"].unique())