import streamlit as st
import pandas as pd
import numpy as np
st.title("Mental Health Analysis")
st.write("Hello, World!")
# df = pd.DataFrame(
#     np.random.randn(10,20),
#     columns=('col % d'% i for i in range(20)))
# st.dataframe(df.style.highlight_max(axis=1), width=1000, height=1000)
# st.table(df)
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c']
     )

st.line_chart(chart_data)