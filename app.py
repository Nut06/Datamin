import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
# from catboost import CatBoostClassifier

st.set_page_config(page_icon="🔎")
st.session_state.icon = "🔎"
@st.cache_resource
def load_model():
    model = xgb.XGBClassifier()
    model.load_model("./model/xgboost_model.bin")
    return model

if "model" not in st.session_state:
    st.session_state.model = load_model()

# Use Tailwind CSS classes to style the text
st.markdown(
    """
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
""",
    unsafe_allow_html=True,
)

# Change the background color and some styling using custom CSS
st.markdown(
    """
    <style>
        .stApp {
            background-color: #FFF6F1;  /* Light gray background */
        }
    </style>
""",
    unsafe_allow_html=True,
)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

# Header section
col1,margin1, col3, margin4, col5 = st.columns([15, 6, 14, 6, 12], gap="medium",vertical_alignment="center")

margin_left, header, margin_right = st.columns([15, 40, 14])
annoy, margin, search = st.columns([15, 40, 14])
with st.container():
    with col1:
        st.image("Image/hearteye.png", width=156)
    with col3:
        st.image("Image/jealous.png", width=171)
    with col5:
        st.image("Image/anxious.png", width=182)
    
with st.container():
    with header:
        st.markdown("""
        <div class="flex flex-col justify-center items-center">
            <h1 class="text-[#175c7d] text-7xl font-bold font-['Prompt'] leading-[99px] tracking-[6.48px] 
            text-center [text-shadow:_0px_4px_1px_rgb(0_0_0_/_0.22)]">Mental  Health</h1>
            <h1 class="text-[#175c7d] text-7xl font-bold font-['Prompt'] leading-[99px] tracking-[6.48px] 
            text-center [text-shadow:_0px_4px_1px_rgb(0_0_0_/_0.22)]">Detection</h1>
        </div>
        """, unsafe_allow_html=True)

with st.container():
    with annoy:
        st.image("Image/annoy.png", width=156)
    with search:
        st.image("Image/search.png", width=156)

st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)

angry, margin, laugh = st.columns([2,5,2], vertical_alignment="bottom")

with st.container():
    with angry:
        st.image("Image/angry.png", width=156)
    with laugh:
        st.image("Image/laughing.png", width=156)

st.markdown("<hr style='border: 2px solid #c9c4c4; width: 740px; margin: 64px auto;'>", unsafe_allow_html=True)

megaphone,objective,margin = st.columns([2,3,5], vertical_alignment="bottom")

with st.container():
    with megaphone:
        st.image("Image/megaphone.png", width=120)
    with objective:
        st.markdown("""
        <div>
            <h1 class="text-[#175c7d] text-7xl font-bold font-['Prompt'] leading-[99px] tracking-[6.48px] [text-shadow:_0px_4px_1px_rgb(0_0_0_/_0.22)]">Objective</h1>
        </div>
        """, unsafe_allow_html=True)
    
with st.container():
    st.markdown(
        """
        <div class="w-full max-w-3xl mx-auto bg-gradient-to-br from-gray-100 to-gray-200 rounded-2xl p-8 shadow-lg hover:shadow-xl transition-shadow duration-300">
            <div class="space-y-6">
                <div class="flex items-center space-x-3 p-4 bg-white/50 rounded-lg hover:bg-white/70 transition-colors duration-300">
                    <div class="flex-shrink-0">
                        <svg class="w-8 h-8 text-blue-800" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                        </svg>
                    </div>
                    <p class="text-black text-2xl font-bold font-['Prompt'] leading-relaxed">เพื่อวิเคราะห์ข้อมูล ปัจจัยต่างๆ ที่มีผลต่อการเกิดภาวะความเครียด</p>
                </div>
                <div class="flex items-center space-x-4 p-4 bg-white/50 rounded-lg hover:bg-white/70 transition-colors duration-300">
                    <div class="flex-shrink-0">
                        <svg class="w-8 h-8 text-blue-800" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
                        </svg>
                    </div>
                    <p class="text-black text-2xl font-bold font-['Prompt'] leading-relaxed">เพื่อวิเคราะห์ปัจจัยที่อาจส่งผลทำให้เกิดปัญหาทางสุขภาพจิต</p>
                </div>
                <div class="flex items-center space-x-4 p-4 bg-white/50 rounded-lg hover:bg-white/70 transition-colors duration-300">
                    <div class="flex-shrink-0">
                        <svg class="w-8 h-8 text-blue-800" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
                        </svg>
                    </div>
                    <p class="text-black text-2xl font-bold font-['Prompt'] leading-relaxed">เพื่อวิเคราะห์แนวโน้มบุคคลที่อาจมีปัญหาด้านสุขภาพจิต</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown("""
        <div class="flex justify-center mt-10">
    """, unsafe_allow_html=True)
    
    with st.container():
        margin_left, button, margin_right = st.columns([1, 1, 1])
        with button:
            if st.button("เริ่มทำเเบบทดสอบ",
                 use_container_width=False,
                 type="primary"):
                st.switch_page("./pages/form.py")
    
# if "df" not in st.session_state:
#     st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

# st.header("Choose a datapoint color")
# color = st.color_picker("Color", "#FF0000")
# st.divider()
# st.scatter_chart(st.session_state.df, x="x", y="y", color=color)


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
