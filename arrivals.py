import streamlit as st
import numpy as np
import pandas as pd

st.header("Tourist Arrivals from Chinese Taipei to Malaysia")

option = st.sidebar.selectbox(
    'Select year',
     ['2014','2015','2016','2017', '2018'])


data = pd.DataFrame({'Year':[2014,2015,2016,2017,2018],
                     1 :[25938,24053,26218,26410,30938],
                     2 :[24197,26115,29510,28322,35748],
                     3 :[20462,19268,19769,25197,29043],
                     4 :[18434,20462,22099,25834,31324],
                     5 :[20335,21482,20128,25397,31523],
                     6 :[22993,24683,23342,27227,32921],
                     7 :[36603,36760,40877,38281,48411],
                     8 :[30188,31498,34274,34609,40453],
                     9 :[18940,21661,25643,26913,30779],
                     10 :[20131,21367,19469,32646,28968],
                     11 :[19100,20265,20277,21760,23172],
                     12 :[17344,15610,19255,20331,20642]})

if option=='2014':
  data_14 = pd.DataFrame(data.iloc[0,1:])
  st.line_chart(data_14)

elif option=='2015':
  data_15 = pd.DataFrame(data.iloc[1,1:])
  st.line_chart(data_15)

elif option=='2016':
  data_16 = pd.DataFrame(data.iloc[2,1:])
  st.line_chart(data_16)

elif option=='2017':
  data_17 = pd.DataFrame(data.iloc[3,1:])
  st.line_chart(data_17)

else:
  data_18 = pd.DataFrame(data.iloc[4,1:])
  st.line_chart(data_18)