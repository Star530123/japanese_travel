class _District:
    def list(self):
        return [
            ["1", "北海道地方", "北海道", "北海道"],
            ["2", "東北地方", "本州", "青森縣"],
            ["3", "東北地方", "本州", "岩手縣"],
            ["4", "東北地方", "本州", "宮城縣"],
            ["5", "東北地方", "本州", "秋田縣"],
            ["6", "東北地方", "本州", "山形縣"],
            ["7", "東北地方", "本州", "福島縣"],
            ["8", "關東地方", "本州", "茨城縣"],
            ["9", "關東地方", "本州", "栃木縣"],
            ["10", "關東地方", "本州", "群馬縣"],
            ["11", "關東地方", "本州", "埼玉縣"],
            ["12", "關東地方", "本州", "千葉縣"],
            ["13", "關東地方", "本州", "東京都"],
            ["14", "關東地方", "本州", "神奈川縣"],
            ["15", "中部地方", "本州", "新潟縣"],
            ["16", "中部地方", "本州", "富山縣"],
            ["17", "中部地方", "本州", "石川縣"],
            ["18", "中部地方", "本州", "福井縣"],
            ["19", "中部地方", "本州", "山梨縣"],
            ["20", "中部地方", "本州", "長野縣"],
            ["21", "中部地方", "本州", "岐阜縣"],
            ["22", "中部地方", "本州", "静岡縣"],
            ["23", "中部地方", "本州", "愛知縣"],
            ["24", "近畿地方", "本州", "三重縣"],
            ["25", "近畿地方", "本州", "滋賀縣"],
            ["26", "近畿地方", "本州", "京都府"],
            ["27", "近畿地方", "本州", "大阪府"],
            ["28", "近畿地方", "本州", "兵庫縣"],
            ["29", "近畿地方", "本州", "奈良縣"],
            ["30", "近畿地方", "本州", "和歌山縣"],
            ["31", "中國地方", "本州", "鳥取縣"],
            ["32", "中國地方", "本州", "島根縣"],
            ["33", "中國地方", "本州", "岡山縣"],
            ["34", "中國地方", "本州", "廣島縣"],
            ["35", "中國地方", "本州", "山口縣"],
            ["36", "四國地方", "四國", "徳島縣"],
            ["37", "四國地方", "四國", "香川縣"],
            ["38", "四國地方", "四國", "愛媛縣"],
            ["39", "四國地方", "四國", "高知縣"],
            ["40", "九州地方", "九州", "福岡縣"],
            ["41", "九州地方", "九州", "佐賀縣"],
            ["42", "九州地方", "九州", "長崎縣"],
            ["43", "九州地方", "九州", "熊本縣"],
            ["44", "九州地方", "九州", "大分縣"],
            ["45", "九州地方", "九州", "宮崎縣"],
            ["46", "九州地方", "九州", "鹿兒島縣"],
            ["47", "沖繩地方", "琉球群島", "沖繩縣"],
        ]
    def dict(self):
        return {district[3]: district for district in self.list()}
district = _District()
LIST = district.list()
DICT = district.dict()