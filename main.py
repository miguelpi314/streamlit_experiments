import streamlit as st


def addition(first_number, second_number):
    return first_number + second_number


st.title('Add numbers')

n1 = st.number_input("First Number")
n2 = st.number_input("Second Number")

if st.button("Calculate"):
    st.write("Summation is: " + str(addition(n1, n2)))