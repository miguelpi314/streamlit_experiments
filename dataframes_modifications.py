import streamlit as st
import pandas as pd
import numpy as np

np.random.seed(0)
df = pd.DataFrame(np.random.randn(4, 3), columns=('Column 1', 'Column 2', 'Column 3'))

col1, col2 = st.columns(2)
with col1:
    st.subheader('Original dataframe')
    st.write(df)


df = df[df['Column 1'] > 0.5]

with col2:
    st.subheader('Mutated dataframe: Filter rows by condition')
    st.write(df)
