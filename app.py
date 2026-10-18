
    label = LABELS.get(sentiment, sentiment.title())
    color = COLORS.get(sentiment, "#93c5fd")
    emoji = EMOJIS.get(sentiment, "•")

    st.divider()

    st.markdown(
        "<div class='section-title'>📊 Analysis Dashboard</div>"
        "<div class='section-desc'>"
        "ผลการประมวลผลข้อความข่าวจากโมเดล FinBERT"
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="result-banner">
            <div class="small-label">PRIMARY SENTIMENT</div>
            <div style="display:flex;align-items:center;gap:14px;
            flex-wrap:wrap;margin-top:12px">
                <div style="font-size:34px;font-weight:800;color:{color}">
                    {emoji} {label}
                </div>
                <div style="background:#0b1525;border:1px solid #30435e;
                border-radius:30px;padding:7px 13px;color:{color};
                font-size:13px;font-weight:700">
                    {confidence:.2%} MODEL SCORE
                </div>
            </div>
            <div style="color:#a9bad0;font-size:13px;margin-top:12px;
            line-height:1.7">
                ประเภทที่มีคะแนนสูงที่สุดจากการประเมินของโมเดล
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Sentiment Breakdown")
    st.caption("เปรียบเทียบคะแนนที่โมเดลให้กับแต่ละประเภท")

    sorted_results = sorted(
        results,
        key=lambda item: float(item["score"]),
        reverse=True
    )

    cols = st.columns(3)

    for col, key in zip(
        cols,
        ["positive", "negative", "neutral"]
    ):
        item = next(
            (r for r in results if r["label"].lower() == key),
            None
        )

        with col:
            if item is not None:
                score = float(item["score"])
                col_color = COLORS[key]

                st.markdown(
                    f"""
                    <div class="sentiment-card">
                        <div class="sentiment-name">
                            {EMOJIS[key]} &nbsp; {key.upper()}
                        </div>
                        <div class="sentiment-value"
                        style="color:{col_color}">
                            {score:.2%}
                        </div>
                        <div class="sentiment-note">
                            {LABELS[key]}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.progress(score)
            else:
                st.info(f"{key.title()}: ไม่มีคะแนนจากโมเดล")

    with st.expander("ดูข้อความที่นำมาวิเคราะห์"):
        st.write(st.session_state.analysis_news)

    st.caption(
        "ข้อควรทราบ: คะแนนนี้เป็นคะแนนของโมเดลสำหรับการจำแนกข้อความ "
        "ไม่ใช่โอกาสที่ราคาหุ้นจะขึ้นหรือลง และไม่ใช่คำแนะนำการลงทุน"
    )


# =========================
# FOOTER
# =========================
st.markdown("""
<div class="footer">
    FINNEWS AI &nbsp;•&nbsp; FINANCIAL NEWS SENTIMENT ANALYSIS
    <br><br>
    Built with Python · Streamlit · FinBERT
    <br>
    Educational project — Not financial advice
</div>
""", unsafe_allow_html=True)
