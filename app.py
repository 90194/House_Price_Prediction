from flask import Flask, render_template, request, url_for
from flask_ngrok import run_with_ngrok
import model0910.modelTest_tpe as model_tpe
import model0910.modelTest_tph as model_tph
import pandas as pd
from datetime import datetime
from pathlib import Path
import sqlalchemy as db
from collections import Counter
import random

# 讀取CSV檔案
# data = pd.read_csv(r'./test_data.csv', encoding='utf-8-sig')


#連接資料庫
path_to_db = "./db/test_data.db"
table_tpe = 'tpe'   # 表格名稱
table_tph = 'tph'
# 建立資料庫引擎
engine = db.create_engine(f'sqlite:///{path_to_db}', connect_args={'check_same_thread': False})
# 建立資料庫連線
connection  = engine.connect()

# 取得資料庫的元資料（資料庫預設編碼、表格清單、表格的欄位與型態、... 等）
metadata = db.MetaData()

# 取得 genres 資料表的 Python 對應操作物件
table_tpe_genres = db.Table(table_tpe, metadata, autoload_with=engine)
table_tph_genres = db.Table(table_tph, metadata, autoload_with=engine)

app = Flask(__name__)

city_mapping = {
    'cityarea': {
        '中正區': [ 0, 0, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        '大同區': [ 0, 1, 2, 1, 3, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        '中山區': [ 0, 0, 2, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        '松山區': [ 0, 2, 1, 1, 2, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        '大安區': [ 0, 1, 2, 0, 2, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        '萬華區': [ 0, 0, 1, 1, 3, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        '信義區': [ 0, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        '士林區': [ 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        '北投區': [ 0, 0, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        '內湖區': [ 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        '南港區': [ 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        '文山區': [ 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       
        '板橋區': [ 0, 1, 2, 1, 3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
        '汐止區': [ 0, 1, 0, 1, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
        '新店區': [ 0, 1, 2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
        '永和區': [ 0, 0, 1, 0, 4, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
        '中和區': [ 0, 1, 2, 0, 2, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
        '土城區': [ 0, 1, 1, 0, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
        '三峽區': [ 0, 1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
        '樹林區': [ 0, 0, 0, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,0],
        '鶯歌區': [ 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,0],
        '三重區': [ 0, 0, 2, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,0],
        '新莊區': [ 0, 1, 2, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,0],
        '泰山區': [ 0, 1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        '林口區': [ 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        '蘆洲區': [ 0, 0, 2, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        '五股區': [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        '八里區': [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        '淡水區': [ 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        },
    'house_type': {
        '住宅大樓': [ 1, 0, 0, 0 ],
        '公寓': [ 0, 1, 0, 0 ],
        '套房':[ 0, 0, 1, 0 ],
        '華廈': [ 0, 0, 0, 1 ],
        }
    }
#將回傳的資料做轉換
def form_data_get(data , city_mapping):
    
    selected_cityarea = data.get('cityarea')
    selected_type = data.get('house_type')
    cityarea_code = city_mapping.get('cityarea', {}).get(selected_cityarea, [0] * 12)
    house_type = city_mapping.get('house_type', {}).get(selected_type ,[1, 0, 0, 0])

    square_meters = int(data.get('square_meters'))if data.get('square_meters') != '' else 0
    house_pattern_r = int(data.get('bedroom_pattern'))if data.get('bedroom_pattern') != '' else 3
    house_pattern_lr = int(data.get('livingRoom_pattern'))if data.get('livingRoom_pattern') != '' else 1
    house_pattern_br = int(data.get('bathroom_pattern'))if data.get('bathroom_pattern') != '' else 2

    house_age = int(data.get('house_age'))if data.get('house_age') != '' else 1
    house_parking = int(data.get('house_parking'))if data.get('house_parking') != '' else 1
    house_elevator = int(data.get('house_elevator'))if data.get('house_elevator') != '' else 1
    house_management = int(data.get('house_management'))if data.get('house_management') != '' else 1
    # house_type = int(data.get('house_type'))if data.get('house_type') != '' else 0

    return{
            
            'house_parking': house_parking,
            'Floor_Arabic': 3,
            'house_age': house_age,
            'transactionYear': 2024,
            'house_pattern_r': house_pattern_r,
            'house_pattern_lr': house_pattern_lr,
            'house_pattern_br': house_pattern_br,
            'square_meters': square_meters,
            # 'num_Garbage':0,
            # 'num_Hospital':0,
            # 'num_Metro':1,
            # 'num_Railway':0,
            # 'num_Primary_School':1,
            # 'num_Sec_School':1,
            'cityarea_code': cityarea_code,
            'material':2,
            'house_type': house_type,
            'house_elevator': house_elevator,
            'house_management': house_management,
        }
#將已處理完的表單資料{}轉為[]
def dict_numeric_values(data):
    numeric_values = []

    # 遍歷 processed_data 字典中的每个值，並检查是否为数字，如果是数字则添加到列表中
    for value in data.values():
        if isinstance(value, (int, float)):
            numeric_values.append(value)
        elif isinstance(value, list):
            # 如果值是列表，则将其中的数字元素添加到列表中
            numeric_values.extend([v for v in value if isinstance(v, (int, float))])

    return numeric_values

@app.route('/')
def index():
    return render_template('index-demo.html',
                           page_header="page_header")

@app.route('/members')
def members():
    return render_template('members.html',
                           page_header="page_header")

# 24.98537160000002
# 121.5628432
results = []
@app.route('/map')
def map():   
    return render_template('map.html',
                           page_header="page_header", results=results[0:5])

# practice start
@app.route('/form')
def get_form():
    return render_template('form.html', page_header="Form")

@app.route('/form_result', methods=['POST'])
def form_result():
    if request.method == 'POST':
        global results
        form_data_dict = dict(request.form)
        area = int(request.form.get('square_meters'))
        age = int(request.form.get('house_age'))
        print(form_data_dict,end="\n"+("-"*80)+"\n")
        dist_tpe = {"中正區" : 100, "大同區":103, "中山區":104, "松山區":105, "大安區":106, "萬華區":108, "信義區":110, "士林區":111, "北投區":112, "內湖區":114, "南港區":115, "文山區":116}
        list_tph_name = ["萬里區", "金山區", "板橋區", "汐止區", "深坑區", "石碇區", "瑞芳區", "平溪區", 
                "雙溪區", "貢寮區", "新店區", "坪林區", "烏來區", "永和區", "中和區", "土城區", 
                "三峽區", "樹林區", "鶯歌區", "三重區", "新莊區", "泰山區", "林口區", "蘆洲區", 
                "五股區", "八里區", "淡水區", "三芝區", "石門區"]
        list_tph_nb = [207, 208, 220, 221, 222, 223, 224, 226, 227, 228, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241, 242, 243, 244, 247, 248, 249, 251, 252, 253]
        dist_tph = dict(zip(list_tph_name, list_tph_nb))
        if form_data_dict["city"] == "臺北市":
            query = db.select(table_tpe_genres).where(table_tpe_genres.c.District==dist_tpe[form_data_dict['cityarea']]).where(table_tpe_genres.c.TotalArea_ping.between(area-5, 500 if area==45 else area+5)).where(table_tpe_genres.c.Type==form_data_dict['house_type']).where(table_tpe_genres.c.Bedrooms==form_data_dict['bedroom_pattern']).where(table_tpe_genres.c.HouseAge.between(age, 500 if age==41 else area+9)).order_by(db.desc(table_tpe_genres.c.TransactionDate_AD))
            query2 = db.select(table_tpe_genres).where(table_tpe_genres.c.District==dist_tpe[form_data_dict['cityarea']]).where(table_tpe_genres.c.TotalArea_ping.between(area-5, 500 if area==45 else area+5)).where(table_tpe_genres.c.Type==form_data_dict['house_type']).order_by(db.desc(table_tpe_genres.c.TransactionDate_AD))
            # 使用form_data_get函數處理表單數數據
            processed_data = form_data_get(request.form ,city_mapping)
            # 接processed_data轉numeric_values
            numeric_values = dict_numeric_values(processed_data)
            print(numeric_values,end="\n"+("-"*80)+"\n")
            predict = model_tpe.recog_digit(numeric_values)

        elif form_data_dict["city"] == "新北市":
            query = db.select(table_tph_genres).where(table_tph_genres.c.District==dist_tph[form_data_dict['cityarea']]).where(table_tph_genres.c.TotalArea_ping.between(area-5, 500 if area==45 else area+5)).where(table_tph_genres.c.Type==form_data_dict['house_type']).where(table_tph_genres.c.Bedrooms==form_data_dict['bedroom_pattern']).where(table_tph_genres.c.HouseAge.between(age, 500 if age==41 else area+9)).order_by(db.desc(table_tph_genres.c.TransactionDate_AD))
            query2 = db.select(table_tph_genres).where(table_tph_genres.c.District==dist_tph[form_data_dict['cityarea']]).where(table_tph_genres.c.TotalArea_ping.between(area-5, 500 if area==45 else area+5)).where(table_tph_genres.c.Type==form_data_dict['house_type']).order_by(db.desc(table_tph_genres.c.TransactionDate_AD))
            # datas = [50.25,3,1,0,0.352941176,2012,27,4,2,2,184.27,0,130.33,15.74]
            processed_data = form_data_get(request.form ,city_mapping)
            numeric_values = dict_numeric_values(processed_data)
            print(numeric_values,end="\n"+("-"*80)+"\n")
            predict = model_tph.recog_digit(numeric_values)
        # 執行sql指令
        proxy = connection.execute(query)
        results = proxy.fetchall()
        # print(results,end="\n"+("-"*80)+"\n")
        date_count = dict(Counter(elem[3] for elem in results))
        # print(date_count)
        over_five = False
        # 若最近的交易日期筆數超過五筆，則會隨機從中取5筆
        try:
            if date_count[results[0][3]] > 5:
                result_over_five = results[0:date_count[results[0][3]]]
                random.shuffle(result_over_five)
                over_five =True
        except IndexError:
            proxy = connection.execute(query2)
            results = proxy.fetchall()
            warning = "*提供以下5筆相似條件房屋資料供參考"
            
            return render_template('form_result.html', page_header="review file", data=predict, results=results[0:5], warning=warning)

        return render_template('form_result.html', page_header="review file", data=predict, results=result_over_five[0:5] if over_five else results[0:5])


if __name__ == '__main__':
    # app.run(debug=True)
    
    app.run()
    run_with_ngrok(app)
# Close connection & engine
connection.close()
engine.dispose()