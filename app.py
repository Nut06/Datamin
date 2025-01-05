import streamlit as st
import pandas as pd
import numpy as np
st.title("Mental Health Analysis")
st.write("Hello, World!")
# if st.checkbox("Show dataframe"):
#      chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])
#      st.line_chart(chart_data)

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])
    
st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)

# if "counter" not in st.session_state:
#     st.session_state.counter = 0

# st.session_state.counter += 1

# st.header(f"This page has run {st.session_state.counter} times.")
# st.button("Run it again")

# left_column, right_column = st.columns(2)
# left_column.button("Press me!")
# with right_column:
#      selected = st.radio(
#           "Choose a number",
#           list(range(1, 4)))
#      st.write("You selected %d" % selected)

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })

# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])
# 'You selected:', option

# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

# df = pd.DataFrame(
#     np.random.randn(10,20),
#     columns=('col % d'% i for i in range(20)))
# st.dataframe(df.style.highlight_max(axis=1), width=1000, height=1000)
# st.table(df)
# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c']
#      )

# st.line_chart(chart_data)
# x = st.slider('Select a number')
# st.write(x, 'squared is', x ** 2)
# st.session_state.name = st.text_input("Enter your name")
# st.write("Hello", st.session_state.name)