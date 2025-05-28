import streamlit as st
import pandas as pd

st.set_page_config(page_icon=st.session_state.icon)
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
            Mental Health Assessment Results
        </h1>
    </div>
    """,
    unsafe_allow_html=True,
)


# Load your model
# @st.cache_resource
# def load_model():
#     model = CatBoostClassifier()
#     model.load_model("./model/catboost_model.cbm")
#     return model

# Top feature
# ['days_indoors' 'changes_habits' 'mood_swings' 'mental_health_history'
#  'social_weakness' 'work_interest' 'coping_struggles' 'occupation_Student']

# Define mapping dictionaries
days_indoors_mapping = {
    "1-14 days": 0.0,
    "15-30 days": 1.0,
    "31-60 days": 2.0,
    "More than 2 months": 3.0,
    "I go out every day": 4.0,
}

nmy_map = {"No": 0.0, "Maybe": 1.0, "Yes": 2.0}

mental_health_history_mapping = nmy_map
changes_habits_mapping = nmy_map
mood_swings_mapping = {"Low": 0.0, "Moderate": 1.0, "High": 2.0}
social_weakness_mapping = nmy_map
work_interest_mapping = nmy_map


# Check if data exists in session state
if "form_data" in st.session_state:
    form_data = st.session_state.form_data

    # Preprocess data
    data = pd.DataFrame(
        {
            "days_indoors": [form_data["days_indoors"]],
            "changes_habits": [form_data["changes_habits"]],
            "mood_swings": [form_data["mood_swings"]],
            "mental_health_history": [form_data["mental_health_history"]],
            "social_weakness": [form_data["social_weakness"]],
            "work_interest": [form_data["work_interest"]],
            "coping_struggles": [form_data["coping_struggles"]],
            "occupation_Student": [form_data["occupation_Student"]],
        }
    )

    # Apply mapping
    data["days_indoors"] = data["days_indoors"].map(days_indoors_mapping)
    data["changes_habits"] = data["changes_habits"].map(changes_habits_mapping)
    data["mood_swings"] = data["mood_swings"].map(mood_swings_mapping)
    data["social_weakness"] = data["social_weakness"].map(social_weakness_mapping)
    data["work_interest"] = data["work_interest"].map(work_interest_mapping)
    data["mental_health_history"] = data["mental_health_history"].map(
        mental_health_history_mapping
    )


def show_prediction_dialog(prediction):

    margin_left, result, margin_right = st.columns([0.5, 12, 0.5])
    if prediction == 0.0:
        with result:
            st.markdown(
                """
                <div style="background-color: #f0f8ff; padding: 40px; border-radius: 10px; text-align: center; font-family: 'Prompt', sans-serif; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                    <i class="fas fa-smile-beam fa-3x" style="color: green; margin-bottom: 10px;"></i>
                    <h2 style="color: #175c7d; font-size: 24px; font-weight: bold;">Prediction Result: No Increased Stress Detected</h2>
                    <p style="color: #333; font-size: 18px; line-height: 1.6;">
                        You show signs of good mental health. Keep it up!<br>
                        Maintain your mental well-being by keeping a balanced lifestyle,<br>
                        including regular exercise, adequate rest, and positive social interactions.
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )
    elif prediction == 1.0:
        with result:
            st.markdown(
                """
                <div style="background-color: #e0f7fa; padding: 30px; border-radius: 12px; text-align: center; font-family: 'Prompt', sans-serif; box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);">
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                    <i class="fas fa-exclamation-circle fa-3x" style="color: #ff9800; margin-bottom: 10px;"></i>
                    <h2 style="color: #00796b; font-size: 24px; font-weight: bold;">Prediction Result: Possible Increased Stress</h2>
                    <p style="color: #555; font-size: 18px; line-height: 1.8;">
                        You may be experiencing increased stress. Please monitor your symptoms and take care of your mental health.<br>
                        Try engaging in relaxing activities such as exercise,<br>
                        meditation, or talking with friends and family.<br>
                        If stress persists, consider consulting a mental health professional<br>
                        for appropriate guidance and care.
                    </p>
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
                    <strong class="font-bold text-xl mb-2">Prediction Result: Increased Stress Detected</strong>
                    <span class="block sm:inline text-lg">You are experiencing increased stress. Please consult a mental health professional for appropriate care.</span>
                    <span class="block sm:inline text-lg">Professional consultation can help you receive necessary guidance and support in managing stress and other mental health concerns.</span>
                </div>
                """,
                unsafe_allow_html=True,
            )


def loading_forpredict(model):
    with st.spinner("Analyzing..."):
        prediction = model.predict(data)
    show_prediction_dialog(prediction)


if "model" in st.session_state:
    model = st.session_state.model
    prediction = model.predict(data)
    show_prediction_dialog(prediction)

# model = load_model()
# prediction = model.predict(data)
# show_prediction_dialog(prediction)

st.markdown(
    """
            <div class='flex justify-center items-center mt-7 mb-7'>
            </div>
            """,
    unsafe_allow_html=True,
)

ml, button, mr = st.columns([1, 1, 0.5])
with button:
    if st.button("Return to Home", use_container_width=False, type="primary"):
        st.cache_data.clear()
        st.switch_page("./app.py")
