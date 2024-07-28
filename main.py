import streamlit as st

st.title("This is the first website :sparkling_heart:")

st.write("hello")

text = st.text_input("Nhap ten cua ban: ")
buton = st.button("Print")
if buton:
  st.write("Hello", text)

st.progress(20)
