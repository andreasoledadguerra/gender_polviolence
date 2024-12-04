import streamlit as st

tab1, tab2 = st.tabs(["Page 1", "Page 2"])

with tab1:
    st.header("You are in the page 1")
    st.image("https://es.wikipedia.org/wiki/Ateez#/media/Archivo:Ateez_at_The_World_EP._2_Outlaw_Showcase.jpg", width=2100)
with tab2:
    st.header("You are in the page 2")
    st.image("https://es.wikipedia.org/wiki/Seventeen_(grupo_musical)#/media/Archivo:SEVENTEEN(%EC%84%B8%EB%B8%90%ED%8B%B4)_-_'Ready_to_love'_%EC%9D%91%EC%9B%90%EB%B2%95_3m_25s.jpg", width=2100)


