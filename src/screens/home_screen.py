import streamlit as st
from src.components.header import header_home 
from src.components.footer import footer_home 
from src.ui.base_layout import style_base_layout, style_background_home

def home_screen():
    


    header_home()
    style_background_home()
    style_base_layout()



    col1,col2,col3,col4 =st.columns([1,1,1,1])

    with col2:

        st.header("I'm Teacher",text_alignment='center')
        st.image("https://tse4.mm.bing.net/th/id/OIP.Wv6MwK4OzV3D4bnuCxFvvAHaHa?r=0&pid=Api&P=0&h=180",width=400)
        if st.button('Teacher Portal',type='primary',icon=':material/arrow_outward:',icon_position='right'):

           st.session_state['login_type']='teacher'
           st.rerun()

    with col3:

        st.header("I'm Student",text_alignment='center')
        st.image("https://tse3.mm.bing.net/th/id/OIP.hYz0QZT68hgq1YAxlgUvJwHaHa?r=0&pid=Api&P=0&h=180",width=400)
        if st.button('Student Portal',type='primary',icon=':material/arrow_outward:',icon_position='right'):
            st.session_state['login_type']='student'
            st.rerun()

    footer_home()
