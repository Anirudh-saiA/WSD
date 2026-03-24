from nltk.corpus import wordnet as wn
from sentence_transformers import SentenceTransformer, util

# 🔥 Load model safely (CPU only)
model = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')


# 🔹 Get meanings from WordNet
def get_meanings(word):
    senses = wn.synsets(word)
    return [sense.definition() for sense in senses]


# 🔹 MAIN FUNCTION
def predict_sense(sentence, word):
    senses = wn.synsets(word)

    if not senses:
        return {
            "best": "No meanings found",
            "top3": [],
            "confidence": 0
        }

    meanings = get_meanings(word)

    # 🔹 Encode sentence + meanings
    sentence_embedding = model.encode(sentence, convert_to_tensor=True)
    meaning_embeddings = model.encode(meanings, convert_to_tensor=True)

    # 🔹 Compute similarity
    scores = util.cos_sim(sentence_embedding, meaning_embeddings)[0]
    scores_list = scores.tolist()

    # 🔹 Rank results
    ranked = sorted(
        zip(meanings, scores_list),
        key=lambda x: x[1],
        reverse=True
    )

    best_meaning = ranked[0][0]
    confidence = round(ranked[0][1], 2)

    top3 = [
        {"meaning": m, "score": round(s, 2)}
        for m, s in ranked[:3]
    ]

    return {
        "best": best_meaning,
        "top3": top3,
        "confidence": confidence
    }