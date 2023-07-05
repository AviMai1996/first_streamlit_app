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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(menu_list)
