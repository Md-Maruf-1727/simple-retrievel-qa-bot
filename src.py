#!/usr/bin/env python
# coding: utf-8

# In[246]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from datset.qa_data import ml_qa_data
import re


# In[247]:


questions = list(ml_qa_data.keys())


# In[248]:


def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = text.strip()

    return text.strip()


# In[249]:


cleaned_question = [preprocess(q) for q in questions]


# In[250]:


full_mean = {
    "ai": "artificial intelligence",
    "ml": "machine learning",
    "pca": "principal component analysis",
    "svm": "support vector machine",
    "knn": "k nearest neighbors",
    "f1": "f1 score",
    "l1": "lasso regularization",
    "l2": "ridge regularization",
    "xgboost": "extreme gradient boosting"
}

def use_full_mean(text):
    words = text.lower().split()
    expanded = []

    for w in words:
        if w in full_mean:
            expanded.append(full_mean[w])
        else:
            expanded.append(w)
    return " ".join(expanded)


# In[251]:


use_full_mean('ML')


# In[252]:


tfidf = TfidfVectorizer(encoding='utf-8', lowercase=True)


# In[253]:


vect_data = tfidf.fit_transform(cleaned_question)


# In[254]:


def get_faq_quetion(user_input: str, threshold = .4) -> str:

    query = preprocess(user_input.lower())
    query = use_full_mean(query)
    query_vec = tfidf.transform([query])
    similarity = cosine_similarity(query_vec, vect_data).flatten()
    q_match = np.argmax(similarity)

    score = similarity[q_match]
    print(f'score: {score}')

    if score > threshold:
        answer = questions[q_match]
        return ml_qa_data[answer]
    else:
        return "Please! Ask related Question!"


# In[255]:


get_faq_quetion("tell me about knn xgboost")

