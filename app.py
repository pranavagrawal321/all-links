import streamlit as st
from st_functions import st_button, load_css

st.set_page_config(page_title="Links", layout="wide")

load_css()

st.markdown(
    """
    <style>
    body {
        background-color: #FFFFFF;  /* Set the background color to white */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>
    .title {
        text-align: center;
        font-weight: bold;
        color: black;
    }
    .image-container {
        display: flex;
        justify-content: center;
    }
    .info{
        background-color: #e8f2fc;
        text-align: center;
        padding: 20px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title" style="margin-top: 0; padding-top: 0" full_width=True>Pranav Agrawal</h1>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="image-container" full_width=True><img '
    'src="https://cdn-icons-png.flaticon.com/128/2609/2609282.png"></div>',
    unsafe_allow_html=True)

st.write("")

st.markdown(
    '<p class="info" style="color: #3c4280;" full_width=True>Developer, Interested in Data Science & Machine '
    'Learning</p>',
    unsafe_allow_html=True)

st.write("")

link_url = "https://github.com/pranavagrawal321"
image_url = "https://cdn-icons-png.flaticon.com/128/2609/2609282.png"

st_button("linkedin", "https://www.linkedin.com/in/pranavagrawal321/", "LinkedIn", 20)
st_button("github", "https://github.com/pranavagrawal321", "Github", 20)
st_button("leetcode", "https://leetcode.com/pranavagrawal321/", "Leetcode", 20)
st_button("hackerrank", "https://hackerrank.com/pranavagrawal321/", "Hackerrank", 20)
st_button("codechef", "https://codechef.com/pranavagrawal321/", "Codechef", 20)
st_button("codeforces", "https://codeforces.com/profile/_pranavagrawal", "Codeforces", 20)
st_button("contact", "pranavagrawal321@gmail.com", "Contact", 20)
