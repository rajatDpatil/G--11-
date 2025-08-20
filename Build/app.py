import streamlit as st
import joblib

vectorizer = joblib.load("vectorizer.jb")
model = joblib.load("lr_model.jb")

st.title("EchoTruth")
st.write("Enter your News or Article below to verify its authenticity. ")

news_input = st.text_area("News or Article:","")

if st.button("Verify"):
    if news_input.strip():
        transforme_input = vectorizer.transform([news_input])
        prediction = model.predict(transforme_input)

        if prediction[0] == 1:
            st.success("This news is Real!! ")
        else:
            st.error("This news is Fake!! ")
    else:
        st.warning("Please enter some text to verify ")
