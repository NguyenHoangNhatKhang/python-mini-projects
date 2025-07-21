import json 

otemae_university_info = {
    "name": "大手前大学",
    "romaji": "Otemae University",
    "type": "私立大学",
    "locations": [
        {
            "campus": "伊丹キャンパス",
            "address": "〒664-0861 兵庫県伊丹市稲野町2丁目2番地",
            "city": "伊丹市",
            "prefecture": "兵庫県",
            "access": "阪急稲野駅から徒歩2分"
        },
        {
            "campus": "さくら夙川キャンパス",
            "address": "〒662-8552 兵庫県西宮市御茶家所町6番42号",
            "city": "西宮市",
            "prefecture": "兵庫県"
        }
    ],
    "website": "https://www.otemae.ac.jp",
    "departments": [
        {"name": "現代社会学部", "description": "社会、メディア、文化、教育について学ぶ"},
        {"name": "国際日本学部", "description": "日本語、国際交流、文化について学ぶ"},
        {"name": "経営学部", "description": "ビジネス、マーケティング、会計について学ぶ"},
        {"name": "看護学部", "description": "看護師として必要な知識とスキルを学ぶ"}
    ],
    "tuition": [
        {"department": "現代社会学部", "amount_yen": 1200000},
        {"department": "経営学部", "amount_yen": 1300000}
    ],
    "highlights": [
        "ベトナム、中国、ネパールなどからの留学生が多い",
        "留学生向けの奨学金や日本語補習クラスあり",
        "さくら夙川キャンパスは景観が美しく、施設も近代的",
        "課外活動、セミナー、オープンキャンパスが頻繁に開催される",
        "一部の学科はオンラインやハイブリッド学習にも対応"
    ],
    "fun_facts": [
        "「大手前」の名前は姫路城の大手前門に由来",
        "教育理念：未来への扉を開く、個性を育てる",
        "有名な卒業生やユーチューバーも在籍していた"
    ]
}


with open("ex.json","w") as file:
    json.dump(otemae_university_info,file)
