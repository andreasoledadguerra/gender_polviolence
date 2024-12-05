
#concepto: modularización; bloques que se encargan de algo específico

import streamlit as st

def page1():
    st.header("You are in the page 1")
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/eb/Ateez_at_The_World_EP._2_Outlaw_Showcase.jpg", width=2100)

def page2():
    st.header("You are in the page 2")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/SEVENTEEN%28%EC%84%B8%EB%B8%90%ED%8B%B4%29_-_%27Ready_to_love%27_%EC%9D%91%EC%9B%90%EB%B2%95_3m_25s.jpg/1920px-SEVENTEEN%28%EC%84%B8%EB%B8%90%ED%8B%B4%29_-_%27Ready_to_love%27_%EC%9D%91%EC%9B%90%EB%B2%95_3m_25s.jpg", width=2100)


tab1, tab2 = st.tabs(["Page 1", "Page 2"])


with tab1:
    page1()

with tab2:
    page2()