import streamlit as st
import random

st.set_page_config(page_title="랜덤 코디 추천기", page_icon="👕", layout="centered")

# 스타일 설정 (Markdown + HTML)
st.markdown("""
    <style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        color: #2C3E50;
        text-align: center;
        margin-bottom: 30px;
    }
    .subtitle {
        font-size: 20px;
        color: #34495E;
        text-align: center;
        margin-bottom: 20px;
    }
    .result-box {
        background-color: #f9f9f9;
        border-left: 5px solid #5DADE2;
        padding: 20px;
        font-size: 22px;
        color: #2C3E50;
        margin-top: 20px;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# 타이틀
st.markdown('<div class="main-title">👗 상황별 랜덤 코디 추천기</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">오늘 뭐 입지? 고민하지 말고 랜덤으로 추천 받아보세요!</div>', unsafe_allow_html=True)

# 코디 데이터
clothing_options = {
    "남자": {
        "데이트": ["셔츠 + 슬랙스", "니트 + 청바지", "자켓 + 면바지", "맨투맨 + 조거팬츠"],
        "운동": ["반팔티 + 반바지", "트레이닝복 세트", "민소매 + 운동 반바지"],
        "출근": ["정장 셔츠 + 슬랙스", "자켓 + 셔츠 + 구두", "니트 + 면바지"],
        "여행": ["후드 + 조거팬츠", "반팔 + 청바지", "셔츠 + 반바지"],
        "파티": ["블레이저 + 셔츠", "셔츠 + 슬랙스 + 로퍼", "깔끔한 니트 + 치노팬츠"],
        "비오는 날": ["방수 재킷 + 슬랙스", "후드 + 운동화", "긴팔티 + 바람막이"]
    },
    "여자": {
        "데이트": ["원피스 + 가디건", "블라우스 + 치마", "니트 + 슬랙스", "셔츠 + 데님"],
        "운동": ["레깅스 + 크롭탑", "트레이닝 세트", "반팔 + 요가팬츠"],
        "출근": ["블라우스 + H라인 스커트", "자켓 + 원피스", "셔츠 + 슬랙스"],
        "여행": ["오버핏 티셔츠 + 반바지", "크롭티 + 와이드 팬츠", "원피스 + 운동화"],
        "파티": ["블랙 드레스", "크롭탑 + 스커트", "화려한 블라우스 + 팬츠"],
        "비오는 날": ["방수 자켓 + 스커트", "트렌치코트 + 부츠", "우비 + 장화"]
    }
}

# 성별 선택
gender = st.radio("👤 성별을 선택하세요:", options=["남자", "여자"], horizontal=True)

# 상황 선택
situation = st.selectbox("📌 상황을 선택하세요:", list(clothing_options[gender].keys()))

# 추천 버튼
if st.button("🎲 코디 추천 받기"):
    outfit = random.choice(clothing_options[gender][situation])
    st.markdown(f"""
        <div class="result-box">
            <strong>{gender}</strong>용 <strong>{situation}</strong> 상황에 추천 코디는<br><br>
            👉 <strong>{outfit}</strong>
        </div>
    """, unsafe_allow_html=True)
