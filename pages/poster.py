import streamlit as st
st.divider()
tab_menus = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"]
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(tab_menus)
tab1.image("2021/01.png")
tab2.image("2021/02.png")
tab3.image("2021/03.png")
tab4.image("2021/04.png")
tab5.image("2021/05.jpg")
tab6.image("2021/06.png")
tab7.image("2021/07.png")
tab8.image("2021/08.png")
tab9.image("2021/09.jpg")
tab10.image("2021/10.png")