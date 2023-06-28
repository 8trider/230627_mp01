import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import streamlit as st

import plotly.graph_objects as go
import common
import pandas as pd

#한글 폰트 적용
import matplotlib.font_manager as fm

common.page_config()

st.title("장르 현황")

data_2021 = common.get_2021()
data_2022 = common.get_2022()
common.get_preprocessing(data_2021, data_2022)

# 한글 폰트 설정
font_path = 'NanumGothic.ttf'  # 사용하고자 하는 한글 폰트 파일 경로로 변경해주세요
fontprop = fm.FontProperties(fname=font_path, size=12)

plt.rc('font', family=fontprop.get_name())
plt.rcParams['axes.unicode_minus'] = False

# Matplotlib 폰트 캐시 삭제
subprocess.call('rm -rf ~/.cache/matplotlib', shell=True)

df_2021 = data_2021[['영화명', '개봉일', '매출액', '매출액점유율', '누적매출액', '관객수', '누적관객수', '스크린수', '대표국적', '등급', '대표장르']]
df_2022 = data_2022[['영화명', '개봉일', '매출액', '매출액점유율', '누적매출액', '관객수', '누적관객수', '스크린수', '대표국적', '등급', '대표장르']]

gc_2021 = df_2021.loc[:,'대표장르'].value_counts()
gc_2022 = df_2022.loc[:,'대표장르'].value_counts()
tab_menus = ["2021", "2022"]
tab1, tab2 = st.tabs(tab_menus)
with tab1:
    from pywaffle import Waffle

    gc_2021_modified = {}

    for key, value in gc_2021.items():
        gc_2021_modified[key] = value // 20
    fig = plt.figure(
        FigureClass=Waffle,
        plots={
            111: {
                'values': gc_2021_modified,
                'labels': ["{0} ({1})".format(n, v) for n, v in gc_2021.items()],
                'legend': {'loc': 'upper left', 'bbox_to_anchor': (1, 1), 'fontsize': 8},
                'title': {'label': '2021 장르 (20개당 별 하나)', 'loc': 'left', 'fontproperties' : fontprop}
            }
        },
        rows=15,
        figsize=(15, 5),
        font_size=15,
        icons ='star'
    )
    plt.show()
    st.pyplot(fig)

with tab2:
    from pywaffle import Waffle

    gc_2022_modified = {}
    for key, value in gc_2022.items():
        gc_2022_modified[key] = value // 20
    fig = plt.figure(
        FigureClass=Waffle,
        plots={
            111: {
                'values': gc_2022_modified,
                'labels': ["{0} ({1})".format(n, v) for n, v in gc_2022.items()],
                'legend': {'loc': 'upper left', 'bbox_to_anchor': (1, 1), 'fontsize': 8},
                'title': {'label': '2022 장르 (20개당 별 하나)', 'loc': 'left', 'fontproperties' : fontprop}
            }
        },
        rows=15,
        figsize=(15, 5),
        font_size=15,
        icons='star'
    )
    plt.show()
    st.pyplot(fig)