# ContextSense AI  
### Real-Time Word Sense Disambiguation using BERT

## 📌 Overview

ContextSense AI is a real-time NLP application that performs **Word Sense Disambiguation (WSD)** — identifying the correct meaning of an ambiguous word based on its context in a sentence.

This system leverages **WordNet** for lexical knowledge and **BERT-based sentence embeddings** for semantic understanding, providing accurate and explainable results.

---

## 🎯 Problem Statement

Many words in natural language have multiple meanings. For example:

- **bank**
  - Financial institution
  - River side

Traditional systems struggle to determine the correct meaning without context.

---

## 💡 Solution

This project uses:

- **WordNet** → to retrieve all possible meanings  
- **BERT (Sentence Transformers)** → to understand context  
- **Cosine Similarity** → to select the most relevant meaning  

---

## ⚙️ Tech Stack

- Python  
- NLTK (WordNet)  
- Sentence Transformers (BERT)  
- PyTorch  
- FastAPI (Backend)  
- Streamlit (Frontend)  

---

## 🧠 How It Works

1. User inputs:
   - Sentence
   - Target ambiguous word

2. System retrieves meanings using WordNet

3. BERT converts:
   - Sentence → embedding  
   - Meanings → embeddings  

4. Cosine similarity is computed

5. Meanings are ranked based on similarity

6. Output:
   - Best meaning  
   - Confidence score  
   - Top 3 meanings  

---

## 🏗 Architecture
User Input (Streamlit UI)
↓
FastAPI Backend
↓
BERT Model (Sentence Transformers)
↓
WordNet Meanings
↓
Cosine Similarity
↓
Output (Best Meaning + Scores)

## 📐 Formula Used

**Cosine Similarity:**
## 📐 Formula Used
cos(θ) = (A · B) / (||A|| × ||B||)


Where:
- A = sentence embedding  
- B = meaning embedding  

---

## 🚀 Features

- Real-time prediction  
- BERT-based semantic understanding  
- Confidence score output  
- Top 3 meaning suggestions  
- Clean and interactive UI  
- Explainable AI approach  

---

## 🧪 Example

**Input:**
Sentence: The fisherman was looking for bass near the river
Word: bass

**Output:**
Best Meaning: Fish
Confidence: 0.82


---

## ⚠️ Limitations

- Requires sufficient context  
- Depends on WordNet definitions  
- Not fine-tuned for domain-specific tasks  

---

## 🔮 Future Improvements

- Fine-tune BERT on WSD datasets  
- Add multilingual support  
- Improve UI/UX  
- Deploy as a web service  

---

2. Install Dependencies
pip install -r requirements.txt

4. Download NLTK Data
import nltk
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
▶️ Run the Project
Start Backend
cd backend
python -m uvicorn main:app
Start Frontend
cd frontend
python -m streamlit run app.py
🌐 API Endpoint
POST /predict
Request:
{
  "sentence": "He deposited money in the bank",
  "word": "bank"
}
Response:
{
  "best": "financial institution",
  "confidence": 0.89,
  "top3": [...]
}
📊 Applications
Chatbots
Search engines
Machine translation
Voice assistants
👨‍💻 Author
Your Name
⭐ Acknowledgements
WordNet (NLTK)
Sentence Transformers
Hugging Face

---

# 🚀 BONUS (IMPORTANT)

👉 Also create `requirements.txt`:

```txt
fastapi
uvicorn
streamlit
nltk
sentence-transformers
torch
scikit-learn
