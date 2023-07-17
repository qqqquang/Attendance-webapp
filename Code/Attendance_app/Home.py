import streamlit as st


st.set_page_config(page_title = 'Attendance System', layout = 'wide')
st.header('Attendance System using Fast Face Recognition')

with st.spinner('Loading Models and Connecting to Redis database ...'):
    import face_rec


st.success('Model loads successfully')
st.success('Redis db successfully connected')

