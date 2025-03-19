# Sem-05-Fake-News-Detection-using-AI

### **Fake News Detection Using Fine-Tuned BERT**  

This project focuses on detecting fake news using a **fine-tuned BERT (Bidirectional Encoder Representations from Transformers) model**. The model is trained on a labeled dataset of news articles to classify them as either **real or fake** based on their textual content.  

---

## **Project Components**  

### **1. `fake-news-detection-using-fine-tune-bert.ipynb`**  
This Jupyter Notebook contains the **core model training and fine-tuning** process. It includes:  
- **Data Preprocessing:** Cleaning and tokenizing text data.  
- **Fine-Tuning BERT:** Training the BERT model on labeled news articles.  
- **Evaluation Metrics:** Assessing the model’s accuracy, precision, recall, and F1-score.  

---

### **2. `app.py`**  
This is a **Flask web application** that provides a user-friendly interface for predicting whether a news article is real or fake. It includes:  
- A **web form** where users can input news articles.  
- Backend logic to **preprocess the input and make predictions** using the trained BERT model.  

---

### **3. `index.html`**  
The **frontend template** for the Flask web app. It includes:  
- A simple input form for users to enter news text.  
- A submit button to check if the news is real or fake.  
- Display of the prediction result.  

---

### **4. `test (1).csv` & `evaluation.csv`**  
These CSV files contain **sample news data** used for testing and evaluating the model.  
- **`test (1).csv`** - Contains test cases to validate predictions.  
- **`evaluation.csv`** - Stores performance metrics and model evaluation results.  

---

## **How It Works**  
1. The user enters a **news article** on the web app.  
2. The text is **processed and tokenized** using the BERT tokenizer.  
3. The **fine-tuned BERT model** classifies the article as **real or fake**.  
4. The **result is displayed** on the web app.  

---

## **Key Features**  
✅ **Fine-tuned BERT model for high accuracy**  
✅ **Flask-based web app for real-time predictions**  
✅ **User-friendly interface with an input form**  
✅ **Dataset included for testing and evaluation**  

---

💡 **This project helps combat misinformation by providing an AI-powered tool for detecting fake news!** 
