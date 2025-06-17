import streamlit as st
import random

st.set_page_config(page_title="풀 코디 추천기", page_icon="🧥", layout="centered")

# ----- 스타일 -----
st.markdown("""
    <style>
    .main-title {
        font-size: 42px;
        font-weight: bold;
        color: #2C3E50;
        text-align: center;
        margin-bottom: 30px;
    }
    .subtitle {
        font-size: 20px;
        color: #7F8C8D;
        text-align: center;
        margin-bottom: 25px;
    }
    .result-box {
        background-color: #fdfdfd;
        border-left: 6px solid #5DADE2;
        padding: 20px;
        font-size: 18px;
        color: #2C3E50;
        margin-top: 25px;
        border-radius: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# ----- 타이틀 -----
st.markdown('<div class="main-title">🧥 상황별 디테일 코디 추천기</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">상의, 하의, 가방, 모자, 액세서리까지 랜덤으로 풀코디 추천!</div>', unsafe_allow_html=True)

# ----- 데이터 -----
colors = ["화이트", "블랙", "베이지", "네이비", "카키", "그레이", "하늘색", "버건디", "브라운", "올리브", "핑크"]

outfit_data = {
    "남자": {
        "상의": ["셔츠", "반팔 티셔츠", "맨투맨", "니트", "후드티"],
        "하의": ["슬랙스", "청바지", "조거팬츠", "반바지", "면바지"],
        "가방": ["백팩", "크로스백", "토트백"],
        "모자": ["볼캡", "비니", "버킷햇"],
        "액세서리": ["시계", "팔찌", "목걸이", "없음"]
    },
    "여자": {
        "상의": ["블라우스", "크롭티", "니트", "셔츠", "티셔츠"],
        "하의": ["스커트", "청바지", "와이드팬츠", "레깅스", "반바지"],
        "가방": ["크로스백", "숄더백", "클러치"],
        "모자": ["버킷햇", "볼캡", "베레모"],
        "액세서리": ["귀걸이", "목걸이", "반지", "없음"]
    }
}

situation_tags = ["데이트", "운동", "출근", "여행", "파티", "비오는 날"]

# ----- 사용자 선택 -----
gender = st.radio("👤 성별을 선택하세요:", options=["남자", "여자"], horizontal=True)
situation = st.selectbox("📌 상황을 선택하세요:", situation_tags)

# ----- 추천 로직 -----
if st.button("✨ 풀코디 추천 받기"):
    top = random.choice(outfit_data[gender]["상의"])
    top_color = random.choice(colors)

    bottom = random.choice(outfit_data[gender]["하의"])
    bottom_color = random.choice(colors)

    bag = random.choice(outfit_data[gender]["가방"])
    bag_color = random.choice(colors)

    hat = random.choice(outfit_data[gender]["모자"])
    hat_color = random.choice(colors)

    accessory = random.choice(outfit_data[gender]["액세서리"])

    st.markdown(f"""
        <div class="result-box">
        <h4>📍 [{gender}] {situation} 코디 추천</h4>
        👕 상의: <strong>{top}</strong> ({top_color})<br>
        👖 하의: <strong>{bottom}</strong> ({bottom_color})<br>
        🎒 가방: <strong>{bag}</strong> ({bag_color})<br>
        🧢 모자: <strong>{hat}</strong> ({hat_color})<br>
        💍 액세서리: <strong>{accessory}</strong>
        </div>
    """, unsafe_allow_html=True)
