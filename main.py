import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pol_violence.plots import plot_fatalities_per_region

st.title('Political Violence across the world Data Explorer')
st.text('This is a web app to explore political violence data')


st.pyplot(fig)

#fig, ax = plt.subplots(1,1)
#ax.plot([0,1.1,2,0.7])
#st.pyplot(fig)