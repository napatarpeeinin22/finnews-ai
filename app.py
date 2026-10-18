
import streamlit as st
from transformers import pipeline

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="FinNews AI | Financial Intelligence",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+Thai:wght@400;500;600;700&display=swap');

:root {
    --bg: #080e1a;
    --panel: #111b2c;
    --panel2: #162238;
    --border: #26364e;
    --text: #f1f5f9;
    --muted: #94a3b8;
    --blue: #60a5fa;
    --green: #4ade80;
    --red: #fb7185;
}

.stApp {
    background:
        radial-gradient(ellipse at 10% 0%, #132744 0%, transparent 38%),
        radial-gradient(ellipse at 95% 20%, #101d35 0%, transparent 32%),
        var(--bg);
    color: var(--text);
    font-family: 'Inter', 'Noto Sans Thai', sans-serif;
}

html, body, [class*="css"] {
    font-family: 'Inter', 'Noto Sans Thai', sans-serif;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

[data-testid="stSidebar"] {
    background: #0b1322;
    border-right: 1px solid #26364e;
}

[data-testid="stSidebar"] > div {
    padding-top: 1.5rem;
}

h1, h2, h3, p, label {
    color: var(--text);
}

h1 {
    letter-spacing: -1.3px;
    font-weight: 800;
}

.stCaption, [data-testid="stCaptionContainer"] {
    color: var(--muted);
}

hr {
    border-color: var(--border);
}

div.stButton > button {
    width: 100%;
    min-height: 48px;
    border-radius: 11px;
    border: 1px solid #3b82f6;
    background: linear-gradient(135deg, #2563eb, #3b82f6);
    color: #ffffff;
    font-weight: 700;
    transition: all 0.2s ease;
}

div.stButton > button:hover {
    border-color: #93c5fd;
    background: linear-gradient(135deg, #1d4ed8, #2563eb);
    color: #ffffff;
    transform: translateY(-1px);
}

div.stButton > button:focus {
    color: #ffffff;
}

[data-testid="stTextArea"] textarea {
    background: #0c1525;
    color: #f1f5f9;
    border: 1px solid #30435e;
    border-radius: 12px;
    line-height: 1.7;
}

[data-testid="stTextArea"] textarea:focus {
    border-color: #60a5fa;
    box-shadow: 0 0 0 1px #60a5fa;
}

[data-testid="stSelectbox"] > div > div {
    background: #111b2c;
    border-color: #30435e;
    border-radius: 10px;
}

[data-testid="stMetric"] {
    background: linear-gradient(145deg, #142139, #101a2b);
    border: 1px solid #2b3c55;
    border-radius: 14px;
    padding: 17px 18px;
}

[data-testid="stMetricLabel"] {
    color: #a9bad0;
}

[data-testid="stMetricValue"] {
    color: #f8fafc;
}

[data-testid="stProgressBar"] > div {
    background: #26364e;
    border-radius: 20px;
}

[data-testid="stProgressBar"] [data-testid="stProgressBarFill"] {
    background: linear-gradient(90deg, #3b82f6, #60a5fa);
    border-radius: 20px;
}

[data-testid="stAlert"] {
    border-radius: 12px;
}

.fin-card {
    background: linear-gradient(145deg, #142139, #101827);
    border: 1px solid #2b3c55;
    border-radius: 18px;
    padding: 23px;
    margin: 8px 0 18px 0;
}

.hero {
    background: linear-gradient(120deg, #152947, #101827 68%);
    border: 1px solid #2c4565;
    border-radius: 22px;
    padding: 32px;
    margin-bottom: 25px;
    position: relative;
    overflow: hidden;
}

.hero-tag {
    display: inline-block;
    padding: 6px 11px;
    background: #183459;
    border: 1px solid #315986;
    border-radius: 30px;
    color: #93c5fd;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.1px;
    margin-bottom: 13px;
}

.hero-title {
    font-size: clamp(27px, 4vw, 42px);
    line-height: 1.2;
    font-weight: 800;
    letter-spacing: -1.2px;
    margin: 0 0 12px 0;
    color: #f8fafc;
}

.hero-desc {
    font-size: 15px;
    line-height: 1.8;
    color: #a9bad0;
    margin: 0;
    max-width: 650px;
}

.section-title {
    font-size: 20px;
    font-weight: 700;
    margin: 10px 0 4px 0;
    color: #f1f5f9;
}

.section-desc {
    color: #94a3b8;
    font-size: 13px;
    line-height: 1.7;
    margin-bottom: 16px;
}

.sentiment-card {
    border-radius: 14px;
    padding: 17px;
    border: 1px solid #2b3c55;
    background: #111b2c;
    min-height: 125px;
    margin-bottom: 10px;
}

.sentiment-name {
    font-size: 13px;
    color: #a9bad0;
    margin-bottom: 12px;
}

.sentiment-value {
    font-size: 25px;
    font-weight: 800;
    margin-bottom: 6px;
}

.sentiment-note {
    color: #94a3b8;
    font-size: 12px;
}

.result-banner {
    border: 1px solid #35577c;
    background: linear-gradient(120deg, #162943, #111b2c);
    border-radius: 16px;
    padding: 23px;
    margin: 12px 0 20px 0;
}

.footer {
    text-align: center;
    color: #64748b;
    font-size: 12px;
    padding: 20px 0 5px 0;
}

.small-label {
    color: #94a3b8;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.2px;
}

@media (max-width: 700px) {
    .hero {
        padding: 23px;
    }
    .fin-card {
        padding: 17px;
    }
}
</style>
""", unsafe_allow_html=True)


# =========================
# LOAD FINBERT
# =========================
@st.cache_resource(show_spinner=False)
def load_model():
    return pipeline(
        "text-classification",
        model="ProsusAI/finbert",
        device=-1
    )


# =========================
# CONSTANTS
# =========================
LABELS = {
    "positive": "ข่าวเชิงบวก",
    "negative": "ข่าวเชิงลบ",
    "neutral": "ข่าวเป็นกลาง"
}

COLORS = {
    "positive": "#4ade80",
    "negative": "#fb7185",
    "neutral": "#93c5fd"
}

EMOJIS = {
    "positive": "↗",
    "negative": "↘",
    "neutral": "—"
}

EXAMPLES = {
    "เลือกข่าวตัวอย่าง...": "",
    "ข่าวเชิงบวก": (
        "The company reported record revenue and "
        "stronger-than-expected profits. Investor "
        "confidence increased following the announcement."
    ),
    "ข่าวเชิงลบ": (
        "The company reported a significant decline in "
        "quarterly revenue and profits. Rising operating "
        "costs and weak consumer demand hurt its performance."
    ),
    "ข่าวเป็นกลาง": (
        "The company announced that its annual shareholder "
        "meeting will take place next month. The meeting "
        "will include a review of the company's annual report."
    )
}


# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.markdown(
        "<div style='font-size:27px;font-weight:800;color:#f8fafc'>"
        "📈 FinNews <span style='color:#60a5fa'>AI</span></div>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<div class='small-label'>FINANCIAL INTELLIGENCE</div>",
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 🧠 เกี่ยวกับระบบ")
    st.markdown(
        "<p style='font-size:13px;color:#a9bad0;line-height:1.8'>"
        "ระบบวิเคราะห์ความรู้สึกของข่าวการเงิน "
        "ด้วยโมเดลปัญญาประดิษฐ์ FinBERT"
        "</p>",
        unsafe_allow_html=True
    )

    st.markdown("### ประเภทการวิเคราะห์")
    st.markdown(
        "<div style='padding:10px 12px;background:#122b25;"
        "border:1px solid #285b46;border-radius:9px;margin-bottom:8px'>"
        "<span style='color:#4ade80;font-weight:700'>● Positive</span>"
        "<br><span style='color:#a9bad0;font-size:12px'>ข่าวเชิงบวก</span>"
        "</div>"
        "<div style='padding:10px 12px;background:#301b29;"
        "border:1px solid #663044;border-radius:9px;margin-bottom:8px'>"
        "<span style='color:#fb7185;font-weight:700'>● Negative</span>"
        "<br><span style='color:#a9bad0;font-size:12px'>ข่าวเชิงลบ</span>"
        "</div>"
        "<div style='padding:10px 12px;background:#172840;"
        "border:1px solid #304d70;border-radius:9px'>"
        "<span style='color:#93c5fd;font-weight:700'>● Neutral</span>"
        "<br><span style='color:#a9bad0;font-size:12px'>ข่าวเป็นกลาง</span>"
        "</div>",
        unsafe_allow_html=True
    )

    st.divider()
    st.markdown("### ⚙️ ข้อมูลระบบ")
    st.caption("Model: ProsusAI/finbert")
    st.caption("Framework: Hugging Face")
    st.caption("Interface: Streamlit")
    st.caption("Language: English news")

    st.divider()
    st.markdown(
        "<div style='font-size:11px;color:#64748b;line-height:1.7'>"
        "EDUCATIONAL PROJECT<br>"
        "AI-powered financial text analysis"
        "</div>",
        unsafe_allow_html=True
    )


# =========================
# HERO HEADER
# =========================
st.markdown("""
<div class="hero">
    <div class="hero-tag">✦ AI-POWERED FINANCIAL ANALYSIS</div>
    <div class="hero-title">Understand the Market.<br>
    One Headline at a Time.</div>
    <p class="hero-desc">
        วิเคราะห์ความรู้สึกของข่าวการเงินด้วย AI
        ช่วยจำแนกข้อความเป็นข่าวเชิงบวก เชิงลบ หรือเป็นกลาง
        พร้อมแสดงคะแนนการวิเคราะห์อย่างชัดเจน
    </p>
</div>
""", unsafe_allow_html=True)


# =========================
# INPUT SECTION
# =========================
st.markdown(
    "<div class='section-title'>📰 News Analyzer</div>"
    "<div class='section-desc'>"
    "ป้อนข่าวการเงินภาษาอังกฤษเพื่อเริ่มการวิเคราะห์"
    "</div>",
    unsafe_allow_html=True
)

with st.container(border=True):
    sample_choice = st.selectbox(
        "ทดลองใช้ข่าวตัวอย่าง",
        list(EXAMPLES.keys()),
        help="เลือกตัวอย่างเพื่อทดลองระบบ หรือพิมพ์ข่าวด้วยตนเอง"
    )

    if "news_input" not in st.session_state:
        st.session_state.news_input = ""

    if st.session_state.get("last_sample") != sample_choice:
        if sample_choice != "เลือกข่าวตัวอย่าง...":
            st.session_state.news_input = EXAMPLES[sample_choice]
        st.session_state.last_sample = sample_choice

    news = st.text_area(
        "ข้อความข่าว",
        key="news_input",
        height=190,
        placeholder=(
            "Example: The company reported strong earnings "
            "and revenue growth..."
        ),
        help="โมเดลนี้ออกแบบมาสำหรับวิเคราะห์ข้อความภาษาอังกฤษ"
    )

    st.caption(
        "TIP  เลือกข่าวตัวอย่างด้านบน หรือวางข่าวภาษาอังกฤษ "
        "ที่ต้องการวิเคราะห์ลงในช่องนี้"
    )

    analyze = st.button(
        "✦  ANALYZE NEWS",
        type="primary",
        use_container_width=True
    )


# =========================
# ANALYSIS
# =========================
if analyze:
    if not news.strip():
        st.warning("กรุณาป้อนข้อความข่าวก่อนเริ่มวิเคราะห์ครับ")
    else:
        try:
            with st.spinner(
                "กำลังวิเคราะห์ข่าวด้วย FinBERT... "
                "การใช้งานครั้งแรกอาจใช้เวลาโหลดโมเดล"
            ):
                model = load_model()
                results = model(news.strip(), top_k=None)

            best = max(results, key=lambda x: float(x["score"]))
            sentiment = best["label"].lower()
            confidence = float(best["score"])

            st.session_state.analysis_results = {
                "results": results,
                "sentiment": sentiment,
                "confidence": confidence
            }
            st.session_state.analysis_news = news.strip()

        except Exception as e:
            st.error("ไม่สามารถวิเคราะห์ข่าวได้")
            st.code(str(e))
            st.info(
                "ตรวจสอบการเชื่อมต่ออินเทอร์เน็ต "
                "และการติดตั้งไลบรารี หากเป็นการใช้งานครั้งแรก"
            )


# =========================
# RESULTS DASHBOARD
# =========================
if "analysis_results" in st.session_state:
    saved = st.session_state.analysis_results
    results = saved["results"]
    sentiment = saved["sentiment"]
    confidence = saved["confidence"]

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
