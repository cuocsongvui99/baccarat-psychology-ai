import streamlit as st
import pandas as pd
from psychology_model import analyze_psychology, predict_next_move, win_rate_if_counter_trend
from utils import detect_trend_patterns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="Baccarat AI Max")

st.title("🎯 AI Phân Tích Tâm Lý Baccarat")

uploaded_file = st.file_uploader("📂 Tải file lịch sử bàn chơi (.csv)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    input_text = st.text_area("📝 Nhập kết quả bàn (P/B/T)", height=150, placeholder="VD: P, B, P, P, T, B,...")
    if input_text:
        data = [x.strip().upper() for x in input_text.split(',')]
        df = pd.DataFrame(data, columns=["Result"])

if 'df' in locals():
    history = df["Result"].tolist()
    trend_info = detect_trend_patterns(df)
    psychology = analyze_psychology(history, trend_info)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("🎭 Người chơi", psychology['player_type'], delta=psychology['player_score'])
        st.write("➡️ " + psychology['player_strategy'])
    with col2:
        st.metric("🧠 Nhà cái", psychology['dealer_type'], delta=psychology['dealer_score'])
        st.write("➡️ " + psychology['dealer_strategy'])

    st.subheader("📊 Biểu đồ Tâm Lý")
    fig, ax = plt.subplots()
    ax.plot(psychology['player_scores'], label='Người chơi')
    ax.plot(psychology['dealer_scores'], label='Nhà cái')
    ax.legend()
    st.pyplot(fig)

    st.subheader("🔮 Dự đoán ván tiếp theo")
    prediction, confidence = predict_next_move(history, trend_info)
    st.markdown(f"👉 **AI dự đoán:** `{prediction}` với độ tin cậy khoảng `{confidence * 100:.0f}%`")

    st.subheader("📉 Tỷ lệ thắng nếu phản cầu")
    rate = win_rate_if_counter_trend(history)
    st.markdown(f"🎲 **Tỷ lệ phản cầu thắng:** `{rate * 100:.1f}%`")
