import streamlit as st
import time
import random
import matplotlib.pyplot as plt
from matplotlib import font_manager
import streamlit as st

st.title("🎈 My new app")
st.write(
    "학생들이 일상에서 접할 수 있는 확률 게임을 직접 시뮬레이션하고, 이론적 확률과 비교해볼 수 있습니다."
)
import os
font_path = "fonts/NanumGothic-Regular.ttf"
nanum_font = None
if os.path.exists(font_path):
    try:
        nanum_font = font_manager.FontProperties(fname=font_path)
        plt.rcParams['font.family'] = nanum_font.get_name()
        # 실제 폰트 이름이 NanumGothic인지 확인
        font_name = nanum_font.get_name()
        if "Nanum" not in font_name:
            st.warning(f"폰트 파일이 올바른 NanumGothic 폰트가 아닙니다. 실제 폰트 이름: {font_name}")
    except Exception as e:
        st.error(f"폰트 파일을 불러오는 중 오류 발생: {e}")
else:
    st.warning(f"폰트 파일을 찾을 수 없습니다: {font_path}. 한글이 깨질 수 있습니다.")

game = st.selectbox("게임을 선택하세요", ["동전 던지기", "주사위 굴리기"])
trials = st.slider("실험 횟수", min_value=10, max_value=1000, value=100, step=10)

if game == "동전 던지기":
    st.subheader("동전 던지기 시뮬레이션")
    st.subheader("동전 던지기 시뮬레이션")
    results = [random.choice(["앞면", "뒷면"]) for _ in range(trials)]
    heads = results.count("앞면")
    tails = results.count("뒷면")
    exp_heads = heads / trials
    exp_tails = tails / trials
    theo_heads = 0.5
    theo_tails = 0.5

    st.write(f"앞면: {heads}번 ({exp_heads:.2f}) / 이론적 확률: {theo_heads}")
    st.write(f"뒷면: {tails}번 ({exp_tails:.2f}) / 이론적 확률: {theo_tails}")

    fig, ax = plt.subplots()
    ax.bar(["앞면", "뒷면"], [exp_heads, exp_tails], label="실험적 확률", alpha=0.7)
    ax.bar(["앞면", "뒷면"], [theo_heads, theo_tails], label="이론적 확률", alpha=0.3)
    ax.set_ylim(0, 1)
    leg = ax.legend()
    if nanum_font:
        ax.set_title(ax.get_title(), fontproperties=nanum_font)
        ax.set_xlabel(ax.get_xlabel(), fontproperties=nanum_font)
        ax.set_ylabel(ax.get_ylabel(), fontproperties=nanum_font)
        for label in ax.get_xticklabels():
            label.set_fontproperties(nanum_font)
        for label in ax.get_yticklabels():
            label.set_fontproperties(nanum_font)
        for text in leg.get_texts():
            text.set_fontproperties(nanum_font)
    st.pyplot(fig)

elif game == "주사위 굴리기":
    st.subheader("주사위 굴리기 시뮬레이션")
    st.subheader("주사위 굴리기 시뮬레이션")
    results = [random.randint(1, 6) for _ in range(trials)]
    exp_probs = [results.count(i) / trials for i in range(1, 7)]
    theo_prob = 1/6

    for i in range(1, 7):
        st.write(f"{i}번: {results.count(i)}번 ({exp_probs[i-1]:.2f}) / 이론적 확률: {theo_prob:.2f}")

    fig, ax = plt.subplots()
    ax.bar(range(1, 7), exp_probs, label="실험적 확률", alpha=0.7)
    ax.bar(range(1, 7), [theo_prob]*6, label="이론적 확률", alpha=0.3)
    ax.set_ylim(0, 1)
    ax.set_xticks(range(1, 7))
    leg = ax.legend()
    if nanum_font:
        ax.set_title(ax.get_title(), fontproperties=nanum_font)
        ax.set_xlabel(ax.get_xlabel(), fontproperties=nanum_font)
        ax.set_ylabel(ax.get_ylabel(), fontproperties=nanum_font)
        for label in ax.get_xticklabels():
            label.set_fontproperties(nanum_font)
        for label in ax.get_yticklabels():
            label.set_fontproperties(nanum_font)
        for text in leg.get_texts():
            text.set_fontproperties(nanum_font)
    st.pyplot(fig)
