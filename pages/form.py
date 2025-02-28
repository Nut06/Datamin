import streamlit as st

# Add Tailwind CSS and Font Awesome CDN
st.markdown(
    """
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        .stApp {
            background-color: #FFF6F1;
        }
        /* Override Streamlit's default padding */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
    </style>
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

nym_q = ["ไม่", "อาจจะ", "ใช่"]

# Update the title with Tailwind classes
st.markdown(
    """
    <div class='flex justify-center items-center'>
        <h1 class='text-4xl font-bold text-center text-blue-800 mb-10 p-4'>
            <i class="fas fa-brain" style="color: rgba(255, 0, 0, 0.41);"></i>
            เเบบสอบถามสุขภาพจิต
        </h1>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.container():
    # 1. ระยะเวลาการอยู่บ้าน
    st.markdown(
        """
        <div class='bg-white p-6 rounded-lg shadow-md mb-6'>
            <h3 class='text-xl font-semibold text-blue-700 mb-3'>
                <i class="fas fa-home text-blue-600 mr-2"></i>
                ระยะเวลาการอยู่บ้าน
            </h3>
            <p class='text-gray-700 mb-4'>โดยเฉลี่ยแล้ว ในช่วง 2 เดือนที่ผ่านมา คุณใช้เวลาอยู่บ้านนานแค่ไหน?</p>
        """,
        unsafe_allow_html=True,
    )
    days_indoors = st.selectbox(
        "", ["1-14 วัน", "15-30 วัน", "31-60 วัน", "มากกว่า 2 เดือน", "ออกไปข้างนอกทุกวัน"]
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # 2. การเปลี่ยนแปลงพฤติกรรม
    st.markdown(
        """
        <div class='bg-white p-6 rounded-lg shadow-md mb-6'>
            <h3 class='text-xl font-semibold text-blue-700 mb-3'>
                <i class="fas fa-sync-alt text-blue-600 mr-2"></i>
                 การเปลี่ยนแปลงพฤติกรรม
            </h3>
            <p class='text-gray-700 mb-4'>คุณสังเกตเห็นการเปลี่ยนแปลงในพฤติกรรมการใช้ชีวิตประจำวันของคุณหรือไม่?</p>
        """,
        unsafe_allow_html=True,
    )
    changes_habits = st.radio("", nym_q, key="changes_habits")
    st.markdown("</div>", unsafe_allow_html=True)

    # 3. อารมณ์แปรปรวน
    st.markdown(
        """
        <div class='bg-white p-6 rounded-lg shadow-md mb-6'>
            <h3 class='text-xl font-semibold text-blue-700 mb-3'>
                <i class="fas fa-chart-line text-blue-600 mr-2"></i>
                 อารมณ์แปรปรวน
            </h3>
            <p class='text-gray-700 mb-4'>คุณรู้สึกว่าอารมณ์ของคุณเปลี่ยนแปลงบ่อยและรุนแรงแค่ไหน?</p>
        """,
        unsafe_allow_html=True,
    )
    mood_swings = st.select_slider("", options=["น้อย", "ปานกลาง", "มาก"])
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
    <div class='bg-white p-6 rounded-lg shadow-md mb-6'>
        <h3 class='text-xl font-semibold text-blue-700 mb-3'>
            <i class="fas fa-history text-blue-600 mr-2"></i>
            ประวัติสุขภาพจิต
        </h3>
        <p class='text-gray-700 mb-4'>คุณเคยมีประวัติการรักษาหรือปรึกษาเกี่ยวกับปัญหาสุขภาพจิตหรือไม่?</p>
    """,
        unsafe_allow_html=True,
    )
    mental_health_history = st.radio("", nym_q, key="mental_health_history")
    st.markdown("</div>", unsafe_allow_html=True)

    # 4. ความอ่อนแอทางสังคม
    st.markdown(
        """
        <div class='bg-white p-6 rounded-lg shadow-md mb-6'>
            <h3 class='text-xl font-semibold text-blue-700 mb-3'>
                <i class="fas fa-users text-blue-600 mr-2"></i>
                 ความอ่อนแอทางสังคม
            </h3>
            <p class='text-gray-700 mb-4'>คุณรู้สึกว่าตัวเองหลีกเลี่ยงการเข้าสังคมหรือรู้สึกอ่อนแอเมื่อต้องเข้าสังคมหรือไม่?</p>
        """,
        unsafe_allow_html=True,
    )
    social_weakness = st.radio("", nym_q, key="social_weakness")
    st.markdown("</div>", unsafe_allow_html=True)

    # 5. ความสนใจในงาน
    st.markdown(
        """
        <div class='bg-white p-6 rounded-lg shadow-md mb-6'>
            <h3 class='text-xl font-semibold text-blue-700 mb-3'>
                <i class="fas fa-briefcase text-blue-600 mr-2"></i>
                 ความสนใจในงาน
            </h3>
            <p class='text-gray-700 mb-4'>คุณยังคงรู้สึกสนใจและมีสมาธิกับงานหรือกิจกรรมที่คุณทำอยู่หรือไม่?</p>
        """,
        unsafe_allow_html=True,
    )
    work_interest = st.radio("", ["ไม่", "อาจจะ", "ใช่"], key="work_interest")
    st.markdown("</div>", unsafe_allow_html=True)

    # 6. ความยากลำบากในการรับมือ
    st.markdown(
        """
        <div class='bg-white p-6 rounded-lg shadow-md mb-6'>
            <h3 class='text-xl font-semibold text-blue-700 mb-3'>
                <i class="fas fa-exclamation-circle text-blue-600 mr-2"></i>
                 ความยากลำบากในการรับมือ
            </h3>
        """,
        unsafe_allow_html=True,
    )
    coping_struggles = st.checkbox(
        "คุณรู้สึกว่าตัวเองมีปัญหาในการรับมือกับความเครียดหรือปัญหาในชีวิตประจำวันหรือไม่?",
        key="coping_struggles",
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # 7. อาชีพ
    st.markdown(
        """
        <div class='bg-white p-6 rounded-lg shadow-md mb-6'>
            <h3 class='text-xl font-semibold text-blue-700 mb-3'>
                <i class="fas fa-id-card text-blue-600 mr-2"></i>
                 อาชีพ
            </h3>
            <p class='text-gray-700 mb-4'>อาชีพปัจจุบันของคุณคืออะไร?</p>
        """,
        unsafe_allow_html=True,
    )
    occupation = st.selectbox(
        "",
        ["พนักงานบริษัท", "นักเรียน/นักศึกษา", "ธุรกิจส่วนตัว", "แม่บ้าน", "อื่นๆ (โปรดระบุ)"],
        key="occupation",
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
    <div class='mb-8'>
    </div>
    """,
        unsafe_allow_html=True,
    )

    ml, button, mr = st.columns([1, 1, 0.5])
    with button:
        if st.button("ส่งข้อมูล", use_container_width=False, type="primary"):
            st.session_state.form_data = {
                "days_indoors": days_indoors,
                "changes_habits": changes_habits,
                "mood_swings": mood_swings,
                "mental_health_history": mental_health_history,
                "social_weakness": social_weakness,
                "work_interest": work_interest,
                "coping_struggles": 1.0 if coping_struggles else 0.0,
                "occupation_Student": 1.0 if occupation == "นักเรียน/นักศึกษา" else 0.0,
            }
            st.switch_page("./pages/result.py")
