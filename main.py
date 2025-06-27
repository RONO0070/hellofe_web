import streamlit as st

name = st.text_input("ENTER YOUR NAME :")
fname = st.text_input("ENTER YOUR FATHER NAME :")

classdate = st.selectbox("ENTER YOUR CLASS :" , (1,2,3,4,5,6,7,8,9))

button = st.button("OK")

if button :
    st.markdown(f"""
    NAME : {name} ||
    FATHER NAME :  {fname} ||
    CLASS : {classdate}""")
