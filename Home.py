import streamlit as st

# Set page configuration
st.set_page_config(page_title='My first app', page_icon="🧊", layout='wide')

# Center-align the title
st.title('Mosaic Tool')
st.markdown("<h1 style='text-align: center;'>Hello eToro!</h1>", unsafe_allow_html=True)

# Center-align the GIF image
st.markdown(
    "<div style='display: flex; justify-content: center;'>"
    "<img src='https://media.giphy.com/media/3o6vXTpomeZEyxufGU/giphy.gif' alt='GIF Image'/>"
    "</div>",
    unsafe_allow_html=True
)
