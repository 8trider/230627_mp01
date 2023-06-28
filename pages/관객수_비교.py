import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import streamlit as st
import plotly.graph_objects as go
import common
import pandas as pd

common.page_config()

st.title("21/22 Top 10 관객수 비교")

data_2021 = common.get_2021()
data_2022 = common.get_2022()

common.get_preprocessing(data_2021, data_2022)

df_2021 = data_2021[['영화명', '개봉일', '매출액', '매출액점유율', '누적매출액', '관객수', '누적관객수', '스크린수', '대표국적', '등급', '대표장르']]
df_2022 = data_2022[['영화명', '개봉일', '매출액', '매출액점유율', '누적매출액', '관객수', '누적관객수', '스크린수', '대표국적', '등급', '대표장르']]

top10_2021 = df_2021.iloc[:10, :]
top10_2022 = df_2022.iloc[:10, :]
# 데이터 설정
x = ['1위', '2위', '3위', '4위', '5위', '6위', '7위', '8위', '9위', '10위']  # x축 레이블
y1 = top10_2021.loc[:, '관객수']  # 첫 번째 막대 그래프 데이터
y2 = top10_2022.loc[:, '관객수']  # 두 번째 막대 그래프 데이터

    # 첫 번째 막대 그래프 생성
trace1 = go.Bar(
        x=x,
        y=y1,
        name='2021'
    )
    # 두 번째 막대 그래프 생성
trace2 = go.Bar(
        x=x,
        y=y2,
        name='2022'
    )
    # 데이터를 리스트로 묶고 레이아웃 설정
data = [trace1, trace2]
layout = go.Layout(
        barmode='group'  # 그룹 형태로 막대 그래프를 그리도록 설정
    )
    # 그래프 생성
fig = go.Figure(data=data, layout=layout)
fig.update_layout(
        title={
            'text': "21년 22년 탑 10 관객수 비교",
            'x': 0.5,  # 제목을 표 가운데로 위치시키기 위해 x 값 조정 (0.0 ~ 1.0)
            'xanchor': 'center',  # x 축 기준으로 제목을 가운데 정렬
            'yanchor': 'top'  # 제목을 상단에 위치
    })
    # 그래프 출력
# fig.show()
    # st.pyplot(fig)
st.plotly_chart(fig)