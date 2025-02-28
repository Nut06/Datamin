import streamlit as st
from catboost import CatBoostClassifier
import pandas as pd

st.markdown(
    """
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        .stApp {
            background-color: #FFF6F1;  /* Light gray background */
        }
    </style>
""",
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class='flex justify-center items-center mt-10 mb-7'>
        <h1 class='text-5xl font-bold text-center' style='color: #175c7d;'>
            <i class="fas fa-heartbeat" style="color: rgba(255, 0, 0, 0.41);"></i>
            ผลการตรวจสอบสุขภาพจิต
        </h1>
    </div>
    """,
    unsafe_allow_html=True,
)


# Load your model
@st.cache_data
def load_model():
    model = CatBoostClassifier()
    model.load_model("./model/catboost_model.cbm")
    return model

# Top feature
# ['days_indoors' 'changes_habits' 'mood_swings' 'mental_health_history'
#  'social_weakness' 'work_interest' 'coping_struggles' 'occupation_Student']

# Define mapping dictionaries
days_indoors_mapping = {
    "1-14 วัน": 0.0,
    "15-30 วัน": 1.0,
    "31-60 วัน": 2.0,
    "มากกว่า 2 เดือน": 3.0,
    "ออกไปข้างนอกทุกวัน": 4.0,
}

nmy_map = {"ไม่": 0.0, "อาจจะ": 1.0, "ใช่": 2.0}

mental_health_history_mapping = nmy_map
changes_habits_mapping = nmy_map
mood_swings_mapping = {"น้อย": 0.0, "ปานกลาง": 1.0, "มาก": 2.0}
social_weakness_mapping = nmy_map
work_interest_mapping = nmy_map


# Check if data exists in session state
if "form_data" in st.session_state:
    form_data = st.session_state.form_data

    # Preprocess data
    data = pd.DataFrame({
        'days_indoors': [form_data['days_indoors']],
        'changes_habits': [form_data['changes_habits']],
        'mood_swings': [form_data['mood_swings']],
        'mental_health_history': [form_data['mental_health_history']],
        'social_weakness': [form_data['social_weakness']],
        'work_interest': [form_data['work_interest']],
        'coping_struggles': [form_data['coping_struggles']],
        'occupation_Student': [form_data['occupation_Student']]
    })

    # Apply mapping
    data['days_indoors'] = data['days_indoors'].map(days_indoors_mapping)
    data['changes_habits'] = data['changes_habits'].map(changes_habits_mapping)
    data['mood_swings'] = data['mood_swings'].map(mood_swings_mapping)
    data['social_weakness'] = data['social_weakness'].map(social_weakness_mapping)
    data['work_interest'] = data['work_interest'].map(work_interest_mapping)
    data['mental_health_history'] = data['mental_health_history'].map(mental_health_history_mapping)


def show_prediction_dialog(prediction):
    
    margin_left, result, margin_right = st.columns([0.5, 17, 0.5])
    if prediction == 0.0:
        with result:
            st.markdown(
                """
                <div style="background-color: #f0f8ff; padding: 40px; border-radius: 10px; text-align: center; font-family: 'Prompt', sans-serif; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                    <i class="fas fa-smile-beam fa-3x" style="color: green; margin-bottom: 10px;"></i>
                    <h2 style="color: #175c7d; font-size: 24px; font-weight: bold;">ผลการทำนาย: ไม่พบความเครียดที่เพิ่มขึ้น</h2>
                    <p style="color: #333; font-size: 18px; line-height: 1.6;">
                        คุณมีแนวโน้มที่จะมีสุขภาพจิตที่ดี ขอให้คุณรักษาสิ่งนี้ไว้!<br>
                        การดูแลสุขภาพจิตที่ดีสามารถทำได้โดยการรักษาสมดุลในชีวิตประจำวัน <br>เช่น  การออกกำลังกาย การพักผ่อนที่เพียงพอ และการมีปฏิสัมพันธ์ที่ดีในสังคม
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )
    elif prediction == 1.0:
        with result:
            st.markdown(
                """
                <div class='flex justify-center items-center mt-10' style="box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); padding: 40px; border-radius: 10px;">
                    <h1 class='text-5xl font-bold text-center' style='color: #175c7d;'>
                        <i class="fas fa-heartbeat" style="color: rgba(255, 0, 0, 0.41);"></i>
                        ผลการตรวจสอบสุขภาพจิต
                    </h1>
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:  # prediction == 2.0
        with result:
            st.markdown(
                """
                <div class="flex flex-col items-center bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mt-4" style="box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); padding: 40px; border-radius: 10px;" role="alert">
                    <i class="fas fa-exclamation-triangle fa-3x mb-4"></i>
                    <strong class="font-bold text-xl mb-2">ผลการทำนาย: พบความเครียดที่เพิ่มขึ้น</strong>
                    <span class="block sm:inline text-lg">คุณมีความเครียดเพิ่มขึ้น ควรปรึกษาผู้เชี่ยวชาญเพื่อรับการดูแลที่เหมาะสม</span>
                    <span class="block sm:inline text-lg">การปรึกษาผู้เชี่ยวชาญสามารถช่วยให้คุณได้รับคำแนะนำและการสนับสนุนที่จำเป็นในการจัดการกับความเครียดและปัญหาสุขภาพจิตอื่น ๆ</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

def loading_forpredict(model):
    with st.spinner('กำลังทำนาย...'):
        prediction = model.predict(data)
    show_prediction_dialog(prediction)


model = load_model()
loading_forpredict(model)
