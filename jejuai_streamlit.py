import streamlit as st

dan = st_number_input("단 입력>>")

for i in range(1,10):
    st_write(f'{dan}*{i} = {dan *i}'}
    
