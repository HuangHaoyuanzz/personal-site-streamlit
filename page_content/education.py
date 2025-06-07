import streamlit as st

def education_page():
    st.markdown("## Education")
    
    st.markdown("""
    ### Master of Science in Marketing
    **The Chinese University of Hong Kong** | *Aug 2024 – Oct 2025*
    - Main courses: Marketing Management, Market Research, Consumer Behavior, Digital Marketing, Big Data Strategy, Market Analysis
    """)
    
    st.markdown("""
    ### Bachelor of Business Administration in Business Administration
    **Sun Yat-sen University** | *Sep 2020 – Jun 2024* | GPA: 3.6/4.0
    - Main courses: Principles of Management, Principles of Marketing, Service Management, Global Marketing, Big Data and Business Intelligence
    """)
    
    st.markdown("---")
    
    st.markdown("## Certifications")
    
    cert1, cert2, cert3 = st.columns(3)
    
    with cert1:
        st.markdown("""
        ### AWS Certified Data Analytics - Specialty
        **Amazon Web Services** | *March 2022*
        
        Demonstrated expertise in designing, building, securing, and maintaining analytics solutions on AWS.
        """)
        
    with cert2:
        st.markdown("""
        ### TensorFlow Developer Certificate
        **Google** | *January 2022*
        
        Validated ability to develop deep learning models using TensorFlow.
        """)
        
    with cert3:
        st.markdown("""
        ### Microsoft Certified: Azure Data Scientist Associate
        **Microsoft** | *November 2021*
        
        Demonstrated expertise in using Azure services to train, evaluate, and deploy machine learning models.
        """)
    
    st.markdown("---")
    
    st.markdown("## Academic Projects")
    
    st.markdown("""
    ### Sentiment Analysis of Product Reviews
    - Developed a deep learning model to analyze customer reviews and predict sentiment
    - Achieved 92% accuracy using BERT and fine-tuning techniques
    - Implemented the model as a web application using Flask
    
    ### Image Classification for Medical Diagnosis
    - Created a convolutional neural network to classify medical images
    - Worked with a dataset of X-ray images to detect pneumonia
    - Achieved 88% accuracy and deployed the model on a cloud platform
    """)
    
    st.markdown("---") 