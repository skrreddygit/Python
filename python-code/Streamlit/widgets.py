import streamlit as st
import pandas as pd

st.title("Streamlit text Input")
name = st.text_input("Enter Your name:")
if name:
    st.write(f"Hello {name}")

age = st.slider("Select your age:",0,100,0)
st.write(f"Your Age: {age}")


options = ["java","Python","C++","Nodejs"]
choice = st.selectbox("Choose your favourite language:",options)
st.write(f"You selected {choice}")

data = {
    "Name" : ["John","Jane","jake","jill"],
    "Age" : [28,24,35,40],
    "City" : ["New York", "Los Angeles", "Chicago","houston"]
}

df = pd.DataFrame(data)

df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)


