import streamlit
import pandas as pd

streamlit.title('One Piece')

streamlit.header('Crew')

streamlit.text('Luffy')
streamlit.text('Zoro')
streamlit.text('Nami')
streamlit.text('Robin')
streamlit.text('Sanji')
streamlit.text('Chopper')
streamlit.text('Brook')
streamlit.text('Ussop')
streamlit.text('Franky')
streamlit.text('Jimbei')

streamlit.header('🥗Menu List For Crew🍞')

menu_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(menu_list)
