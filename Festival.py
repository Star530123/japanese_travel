#%%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import District as d

seasons = ["spring", "summer", "autumn", "winter"]
festival_seasons_html = []
for season in seasons:
    r = requests.get(
        f"https://www.tourism-alljapanandtokyo.org/category/festival-zh-hant/{season}-zh-hant?lang=zh-hant"
    )
    festival_seasons_html.append(BeautifulSoup(r.text, "html.parser"))

festival_dataframe = []
for season_html in festival_seasons_html:
    season = season_html.title.text[0:2]
    for festival in season_html.find_all("div", "list-gallery"):
        website = festival.find("a")["href"]
        date = festival.find_all("p")[0].text.strip()
        position = festival.find_all("p")[1].text.strip()
        position_detail = d.DICT.get(position)
        print(position)
        island = position_detail[2]
        region = position_detail[1]
        festival_name = festival.find("h1").text
        data = [season, date,island,region, position, festival_name, website]
        festival_dataframe.append(data)

columns = ["季節", "時間","列島","地方", "道都府縣", "祭典名稱", "網頁"]
df = pd.DataFrame(festival_dataframe, columns=columns) 
print(df)
df.to_excel("festival.xlsx")
# %%
