import streamlit as st


st.write('')

import matplotlib.pyplot as plt

fig, ax = plt.subplots(1,1)
ax.plot([0,1.1,2,0.7])
st.pyplot(fig)