from src.add import addition
from src.sub import subtraction
from src.div import divide
from src.mul import multiplication
from src.mod import modulo
import streamlit as st

st.title("Calculator")

a = st.number_input("Enter the First Number : ", value=0)
b = st.number_input("Enter the Second Number : ", value=0)

option = st.selectbox(
    "Enter the Mathematical Operation you want to perform",
    ("Addition", "Subtraction" , "Divide" ,"Multiplication","Modulo"),
)

if st.button("Calculate"):
    if option == "Addition":
        result = addition(a, b)
    elif option == "Subtraction":
        result = subtraction(a, b)
    elif option == "Divide":
        result = divide(a,b)
    elif option == "Multiplication":
        result= multiplication(a,b) 
    else :
        result = modulo(a,b)
        
    st.write(f"Result : {result}")