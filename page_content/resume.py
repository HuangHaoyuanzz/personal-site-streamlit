import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "Resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="Huang_Haoyuan_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Huang Haoyuan")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** huanghy2025@163.com
    - **Phone:** +86 13347357290
    - **Address:** Wei Wah Centre, Sha Tin Centre Street, Sha Tin, Hong Kong
    - **WeChat:** hhhhhh0401
    """)

    st.header("Education")
    st.markdown("""
    **Master of Science in Marketing**
    - The Chinese University of Hong Kong, Aug 2024 – Oct 2025
    - Main courses: Marketing Management, Market Research, Consumer Behavior, Digital Marketing, Big Data Strategy, Market Analysis

    **Bachelor of Business Administration in Business Administration**
    - Sun Yat-sen University, Sep 2020 – Jun 2024, GPA: 3.6/4.0
    - Main courses: Principles of Management, Principles of Marketing, Service Management, Global Marketing, Big Data and Business Intelligence
    """)

    st.header("Internship Experience")
    st.markdown("""
    **VR Game Marketing & Operations Intern**
    - Shenzhen Saibu Innovation Technology Co., Ltd. | May 2025 – Present
    - Influencer marketing: Cooperated with over 100 influencers via email, social media, and paid platforms, resulting in videos with tens of thousands of views and reaching over a million fans, significantly improving conversion rates.
    - Social media operations: Managed official accounts on YouTube, TikTok, Instagram, and X, participated in content creation and promotion, increasing watch time by 500% and follower growth by 125%.
    - Community operations: Managed the Discord player community, organized daily activities, and improved player retention and conversion rates.

    **Sports Marketing Intern**
    - Nike Sports (China) Co., Ltd. | July 2023 – January 2024
    - Match data analysis: Collected and organized information from 200+ Chinese Super League matches, maintained SOP system data, produced 10+ competitor analysis reports, and maintained client relationships.
    - Marketing campaign planning: Participated in new season jersey design and launch, communicated with team managers, gathered fan needs, and provided feedback to the design department.
    - Social media support: Supported dozens of contracted athletes with social media content and tracked hundreds of players' equipment usage.
    - Product support: Developed club season equipment support plans and assisted with order and delivery.

    **HR Intern**
    - Guangzhou Pearl River Kayserburg Piano Co., Ltd. | July 2022 – August 2022
    - Employee information management: Organized contracts for 200+ employees and completed digital archiving.
    - Employee welfare support: Collected feedback from frontline workers and wrote reports to optimize the production line environment.
    """)

    st.header("Project & Extracurricular Experience")
    st.markdown("""
    **Sports Department Member, Student Union**
    - School of Management, Sun Yat-sen University | Oct 2020 – Jun 2022
    - Organized and operated a college football event, attracting over 100 students; assisted in planning two university/college sports meetings.

    **Summer Social Practice Member**
    - School of Management, Sun Yat-sen University | July 2021
    - Conducted a five-day field research in rural Hunan, interviewed local residents, analyzed rural economic challenges, and reported findings to local officials and experts.
    """)

    st.header("Skills")
    st.markdown("""
    - Marketing: Digital Marketing, Market Research, Brand Management, Sports Marketing
    - Data Analysis: Python, R Language, SPSS, Excel
    - Social Media: YouTube, TikTok, Instagram, X Platform Operations
    - Languages: English (IELTS 7.0), Chinese (Native)
    - Technical Skills: Microsoft Office, Python, R Language, C Language
    """)

    st.markdown("---") 