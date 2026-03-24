import streamlit as st
import requests

# 🔹 Page config
st.set_page_config(
    page_title="ContextSense AI",
    layout="centered"
)

# 🔥 FULL CLEAN LIGHT THEME + REMOVE BLUE
st.markdown("""
    <style>

    /* Force light background */
    html, body, .stApp {
        background-color: #F5F5F5 !important;
        color: #000000 !important;
    }

    /* Remove blue highlight (selection) */
    ::selection {
        background: #dddddd;
        color: #000000;
    }

    /* Fix labels */
    label {
        color: #000000 !important;
        background: none !important;
        font-weight: 500;
    }

    div[data-testid="stTextInput"] label,
    div[data-testid="stTextArea"] label {
        color: #000000 !important;
    }

    /* Title */
    .main-title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #000000;
        margin-bottom: 10px;
    }

    .sub-title {
        text-align: center;
        font-size: 18px;
        color: #444444;
        margin-bottom: 30px;
    }

    /* Inputs */
    textarea, input {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border-radius: 8px !important;
    }

    /* Button */
    .stButton>button {
        background-color: #000000;
        color: #FFFFFF;
        border-radius: 6px;
        padding: 8px 16px;
        border: none;
    }

    .stButton>button:hover {
        background-color: #333333;
    }

    /* Result box */
    .result-box {
        background-color: #FFF8C6;
        color: #000000;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #FFD700;
        margin-top: 20px;
    }

    .confidence {
        font-weight: bold;
        margin-top: 10px;
    }

    </style>
""", unsafe_allow_html=True)

# 🔹 Title
st.markdown('<div class="main-title">ContextSense AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Real-Time Word Sense Disambiguation</div>', unsafe_allow_html=True)

# 🔹 Inputs
sentence = st.text_area("Enter a sentence")
word = st.text_input("Enter the ambiguous word")

# 🔹 Highlight function
def highlight_word(sentence, word):
    return sentence.replace(word, f"**{word.upper()}**")

# 🔹 Button
if st.button("Analyze"):

    if not sentence or not word:
        st.warning("Please enter both fields")

    else:
        try:
            res = requests.post(
                "http://127.0.0.1:8000/predict",
                json={
                    "sentence": sentence,
                    "word": word
                }
            )

            data = res.json()

            # 🔹 Highlighted sentence
            st.markdown("### Highlighted Sentence")
            st.markdown(highlight_word(sentence, word))

            # 🔹 Result box
            st.markdown(f"""
                <div class="result-box">
                    <h4>Best Meaning</h4>
                    <p>{data['best']}</p>
                    <div class="confidence">Confidence: {data['confidence']}</div>
                </div>
            """, unsafe_allow_html=True)

            # 🔹 Top 3 meanings
            st.markdown("### Top 3 Meanings")
            for i, item in enumerate(data["top3"], 1):
                st.write(f"{i}. {item['meaning']} (score: {item['score']})")

        except Exception as e:
            st.error("Backend is not running")
            st.text(str(e))

# 🔹 Footer
st.markdown("---")
st.caption("ContextSense AI Project")