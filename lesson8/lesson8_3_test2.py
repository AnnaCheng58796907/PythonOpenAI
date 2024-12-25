from tools import fetch_youbike_data
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

youbike_data:list[dict] = fetch_youbike_data()

# 使用streamlit分2個欄位
# 使用you_bike_data:list的資料, 取出所有的行政區域(sarea), 不可以重複
# 左邊是選擇行政區域(sarea), 使用下拉式表單
# 右邊是顯示該行政區域的YouBike站點資訊的表格資料
# 最下方是顯示該行政區域的YouBike站點資訊的地圖
area_list = list(set(map(lambda value:value['sarea'], youbike_data)))

col1, col2 = st.columns([1, 3])
with col1:
    selected_sarea = st.selectbox("行政區域", area_list)

with col2:
    def filter_func(value:dict)->bool:
        return value['sarea'] == selected_sarea

    filter_list = list(filter(filter_func, youbike_data))
    show_data:list[dict] = [{
                            '站點' : item['sna'],
                            '總車輛數' : item['tot'],
                            '可借車輛數' : item['sbi'],
                            '可還車輛數' : item['bemp'],
                            '營業中' : item['act'],
                            'latitude' : float(item['lat']),
                            'longitude' : float(item['lng'])
                            } for item in filter_list]
    st.dataframe(show_data)

# 將資料轉換為 DataFrame
df = pd.DataFrame(show_data)

# 組合站點資訊文字
df['site_info'] = df.apply(
    lambda row: f"站點:{ row['站點'] }\n 可借:{ row['可借車輛數'] }\n 可還:{ row['可還車輛數'] }", 
    axis=1
)

# 創建地圖對象，設置初始位置和縮放級別
m = st.map(
    data=df,
    latitude='latitude',
    longitude='longitude',
    color='#FF0000',  # 紅色標記
    size=15,          # 標記大小
    )

# 在地圖上添加站點標記
for _, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=row['站點'],
    ).add_to(m)