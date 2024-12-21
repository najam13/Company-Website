import streamlit as st
#
# with st.container():
# st.header("Contact us")

with st.container():
    st.header("Contact Us")
    st.write("For inquiries or support, please contact us.")

with st.container():
    email_address = st.text_input("Enter your email address")

# Optional: Add a button to submit the email address
if st.button("Submit"):
    if email_address:
        st.success("Email address submitted!")
    else:
        st.warning("Please enter your email address.")
