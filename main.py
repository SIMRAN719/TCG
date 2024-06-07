import streamlit as st
from Application.testcases import get_summaryprompt, generate_test_cases

st.title('TCG (Test Case Generation)')

# uploaded_file = st.file_uploader('Upload a file', type=['pdf','docx','txt','png','jpg','jpeg','tiff','bmp','gif'])
uploaded_file = st.sidebar.file_uploader('Upload a file', type=['pdf','docx','txt'])
requirements = st.sidebar.text_input(placeholder='Enter your requirements here', key='requirements', label='Prompt')

if st.sidebar.button('Generate Test Cases'):
    # uploaded_file = st.file_uploader('Upload a file', type=['pdf','docx','txt','png','jpg','jpeg','tiff','bmp','gif'])
    # requirements = st.text_input(placeholder='Enter your requirements here', key='requirements')
    if uploaded_file:
        summary = get_summaryprompt(uploaded_file)
        test_cases = generate_test_cases(summary)
        st.write(test_cases)
    elif requirements:
        test_cases = generate_test_cases(requirements)
        # st.write(requirements)
        # st.write('-------------------------------')
        st.write(test_cases)

