import streamlit as st

# create a header text for the app
st.header(" Create a button")

# action depending on button text
if st.button("Say Hello"):
    # print text messages using st.write
    st.write('Why Hello there!! :) ')
else:
    st.write("Goodbye :(")