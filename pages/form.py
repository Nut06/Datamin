import streamlit as st

# Set page config - Assuming 'icon' is set elsewhere in your session state setup
if 'icon' not in st.session_state:
    st.session_state.icon = "🧠" # Default icon if not set

st.set_page_config(page_icon=st.session_state.icon)

# Add Tailwind CSS and Font Awesome CDN
st.markdown(
    """
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        .stApp {
            background-color: #FFF6F1; /* Light beige background */
        }
        /* Override Streamlit's default padding */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        /* Style for the cards */
        .form-card {
            background-color: white;
            padding: 1.5rem; /* 24px */
            border-radius: 0.5rem; /* 8px */
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            margin-bottom: 1.5rem; /* 24px */
        }
        .form-title {
            font-size: 1.25rem; /* 20px */
            font-weight: 600; /* semibold */
            color: #2563EB; /* blue-700 */
            margin-bottom: 0.75rem; /* 12px */
        }
         .form-question {
            color: #4B5563; /* gray-700 */
            margin-bottom: 1rem; /* 16px */
         }
         .main-title-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 2.5rem; /* 40px */
            padding: 1rem; /* 16px */
         }
         .main-title {
            font-size: 2.25rem; /* 36px, text-4xl */
            font-weight: 700; /* bold */
            text-align: center;
            color: #1E40AF; /* blue-800 */
         }
         .main-title i {
             color: rgba(255, 0, 0, 0.41); /* Keep the specific brain icon color */
             margin-right: 0.75rem; /* Add some space between icon and text */
         }
    </style>
    """,
    unsafe_allow_html=True,
)

# Options for Yes/No/Maybe questions
yes_no_maybe_options = ["No", "Maybe", "Yes"]

# Update the title with Tailwind classes (using custom classes for clarity)
st.markdown(
    """
    <div class='main-title-container'>
        <h1 class='main-title'>
            <i class="fas fa-brain"></i>
            Mental Health Questionnaire
        </h1>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.container():
    # 1. Time Spent at Home
    st.markdown(
        """
        <div class='form-card'>
            <h3 class='form-title'>
                <i class="fas fa-home text-blue-600 mr-2"></i>
                Time Spent at Home
            </h3>
            <p class='form-question'>On average, how much time have you spent at home over the past 2 months?</p>
        """,
        unsafe_allow_html=True,
    )
    days_indoors = st.selectbox(
        "Select time spent at home:", # Added label for accessibility
        [
            "1-14 days",
            "15-30 days",
            "31-60 days",
            "More than 2 months",
            "I go out every day",
        ],
        label_visibility="collapsed" # Hide label visually but keep for screen readers
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # 2. Behavioral Changes
    st.markdown(
        """
        <div class='form-card'>
            <h3 class='form-title'>
                <i class="fas fa-sync-alt text-blue-600 mr-2"></i>
                 	Behavioral Changes
            </h3>
            <p class='form-question'>Have you noticed changes in your daily behavior or routine?</p>
        """,
        unsafe_allow_html=True,
    )
    changes_habits = st.radio(
        "Select behavioral changes:", # Added label
        yes_no_maybe_options,
        key="changes_habits",
        label_visibility="collapsed" # Hide label
        )
    st.markdown("</div>", unsafe_allow_html=True)

    # 3. Mood Swings
    st.markdown(
        """
        <div class='form-card'>
            <h3 class='form-title'>
                <i class="fas fa-chart-line text-blue-600 mr-2"></i>
                 	Mood Swings
            </h3>
            <p class='form-question'>How often and intensely do you experience mood swings?</p>
        """,
        unsafe_allow_html=True,
    )
    mood_swings = st.select_slider(
        "Select mood swing intensity:", # Added label
        options=["Low", "Moderate", "High"],
        label_visibility="collapsed" # Hide label
        )
    st.markdown("</div>", unsafe_allow_html=True)

    # 4. Mental Health History
    st.markdown(
        """
    <div class='form-card'>
        <h3 class='form-title'>
            <i class="fas fa-history text-blue-600 mr-2"></i>
            Mental Health History
        </h3>
        <p class='form-question'>Do you have a history of treatment for mental health issues?</p>
    """,
        unsafe_allow_html=True,
    )
    mental_health_history = st.radio(
        "Select mental health history:", # Added label
        yes_no_maybe_options,
        key="mental_health_history",
        label_visibility="collapsed" # Hide label
        )
    st.markdown("</div>", unsafe_allow_html=True)

    # 5. Social Interaction Difficulty
    st.markdown(
        """
        <div class='form-card'>
            <h3 class='form-title'>
                <i class="fas fa-users text-blue-600 mr-2"></i>
                 Social Interaction Difficulty
            </h3>
            <p class='form-question'>Do you tend to avoid social interactions or feel uneasy during them?</p>
        """,
        unsafe_allow_html=True,
    )
    social_weakness = st.radio(
        "Select social interaction difficulty:", # Added label
        yes_no_maybe_options,
        key="social_weakness",
        label_visibility="collapsed" # Hide label
        )
    st.markdown("</div>", unsafe_allow_html=True)

    # 6. Interest in Work/Activities
    st.markdown(
        """
        <div class='form-card'>
            <h3 class='form-title'>
                <i class="fas fa-briefcase text-blue-600 mr-2"></i>
                 Interest in Work/Activities
            </h3>
            <p class='form-question'>Do you still feel interested and focused on your work or the activities you usually do?</p>
        """,
        unsafe_allow_html=True,
    )
    work_interest = st.radio(
        "Select interest in work/activities:", # Added label
        yes_no_maybe_options, # Use the translated list
        key="work_interest",
        label_visibility="collapsed" # Hide label
        )
    st.markdown("</div>", unsafe_allow_html=True)

    # 7. Coping Struggles
    st.markdown(
        """
        <div class='form-card'>
            <h3 class='form-title'>
                <i class="fas fa-exclamation-circle text-blue-600 mr-2"></i>
                 Coping Struggles
            </h3>
        """,
        unsafe_allow_html=True,
    )
    coping_struggles = st.checkbox(
        "Do you feel you have trouble coping with stress or daily problems?",
        key="coping_struggles",
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # 8. Occupation
    st.markdown(
        """
        <div class='form-card'>
            <h3 class='form-title'>
                <i class="fas fa-id-card text-blue-600 mr-2"></i>
                 Occupation
            </h3>
            <p class='form-question'>What is your current occupation?</p>
        """,
        unsafe_allow_html=True,
    )
    occupation = st.selectbox(
        "Select occupation:", # Added label
        ["Employee", "Student", "Self-employed", "Homemaker", "Other"], # Translated options
        key="occupation",
        label_visibility="collapsed" # Hide label
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # Add some space before the button
    st.markdown(
        """
    <div class='mb-8'>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Submit Button - Centered using columns
    ml, button_col, mr = st.columns([1, 1, 1]) # Adjust column ratios for centering if needed
    with button_col:
        submit_button = st.button("Submit", use_container_width=True, type="primary")

    if submit_button:
        # Store data in session state
        st.session_state.form_data = {
            "days_indoors": days_indoors,
            "changes_habits": changes_habits,
            "mood_swings": mood_swings,
            "mental_health_history": mental_health_history,
            "social_weakness": social_weakness,
            "work_interest": work_interest,
            "coping_struggles": 1.0 if coping_struggles else 0.0,
            # IMPORTANT: Update the occupation check to use the English value
            "occupation_Student": 1.0 if occupation == "Student" else 0.0,
        }
        # Navigate to the results page
        st.switch_page("./pages/result.py")

