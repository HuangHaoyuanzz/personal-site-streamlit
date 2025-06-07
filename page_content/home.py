import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>Huang Haoyuan</h4>
        <p>Recent Master's Graduate in Marketing<br>
        Chinese University of Hong Kong<br>
        Wei Wah Centre, Sha Tin Centre Street, Sha Tin, Hong Kong<br>
        <a href="mailto:huanghy2025@163.com">huanghy2025@163.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "image.png")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        I am a Master's student in Marketing at the Chinese University of Hong Kong, with a solid background in Business Administration. My academic and professional focus lies in digital marketing, market research, and consumer behavior analysis, particularly with rich internship experience in sports marketing and gaming industry.

        My internship at Nike Sports (China) provided me with deep insights into sports marketing operations, including event data analysis, product marketing planning, and athlete social media management. At Shenzhen Saibu Innovation Technology, my experience in VR game market operations has given me extensive expertise in digital marketing, achieving significant results in influencer marketing, social media operations, and community management.

        I excel in data analysis, marketing strategy, and team collaboration, with strong English communication skills (IELTS 7.0) and solid computer proficiency. I look forward to applying my professional knowledge and practical experience to future career development and creating value for the team.
        """
    )

    st.markdown(
        """
        ### Skills
        - Marketing: Digital Marketing, Market Research, Brand Management, Sports Marketing
        - Data Analysis: Python, R Language, SPSS, Excel
        - Social Media: YouTube, TikTok, Instagram, X Platform Operations
        - Languages: English (IELTS 7.0), Chinese (Native)
        - Technical Skills: Microsoft Office, Python, R Language, C Language
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 