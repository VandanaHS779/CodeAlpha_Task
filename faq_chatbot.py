import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Load English model
nlp = spacy.load("en_core_web_sm")

# FAQ database
faq_data = {
    "What is your return policy?": "You can return any item within 30 days of purchase.",
    "How long does delivery take?": "Delivery usually takes 3 to 5 business days.",
    "Do you ship internationally?": "Yes, we ship to most countries worldwide.",
    "How can I contact customer service?": "You can reach our customer support at support@example.com.",
    "What payment methods do you accept?": "We accept credit cards, debit cards, and PayPal.",
    "Can I cancel my order?": "Yes, you can cancel your order within 24 hours of placing it."
}

questions = list(faq_data.keys())
answers = list(faq_data.values())

def preprocess(text):
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

preprocessed_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(preprocessed_questions)

def get_best_match(user_input):
    user_input_processed = preprocess(user_input)
    user_vec = vectorizer.transform([user_input_processed])
    similarity = cosine_similarity(user_vec, X)
    best_match_index = similarity.argmax()
    score = similarity[0, best_match_index]
    if score < 0.3:
        return "Sorry, I couldn't understand your question."
    return answers[best_match_index]

st.title("🤖 FAQ Chatbot")
st.write("Ask me any question about our services!")

user_query = st.text_input("Your Question:")
if user_query:
    response = get_best_match(user_query)
    st.markdown(f"**Chatbot:** {response}")
