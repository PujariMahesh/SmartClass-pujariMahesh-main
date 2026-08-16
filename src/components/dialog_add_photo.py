import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase

from PIL import Image




@st.dialog("Add Classroom Photos")
def add_photos_dialog():
    st.write('Add classroom photos to scan for attendance')


    if 'photo_tab' not in st.session_state:
        st.session_state.photo_tab='camera'
    t1, t2=st.columns(2)

    with t1:
        type_camera="primary" if st.session_state.photo_tab=='camera'else 'tertiary'
        if st.button('Camera',type=type_camera,width='stretch'):
            st.session_state.photo_tab='camera'

    with t2:
        type_upload="primary" if st.session_state.photo_tab=='upload' else 'tertiary'
        if st.button('Upload photos',type=type_upload,width='stretch'):
            st.session_state.photo_tab='upload'

    if st.session_state.photo_tab=='camera':
        
        st.markdown(
            "<h5>Take a snap</h5>",
            unsafe_allow_html=True)
        cam_photo=st.camera_input("",label_visibility='collapsed',key='dialog_cam')
        if cam_photo:
            st.session_state.attendance_images.append(Image.open(cam_photo))
            st.markdown(
                         """
                         <div style="
                          position: fixed;
                          top: 20px;
                          right: 20px;
                          background-color: #f0f0f0;
                          padding: 10px 20px;
                          border-radius: 8px;
                          box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
                          z-index: 1000;
                         ">
                          <span style="color:black; font-size:16px;">Photo Captured</span>
                     </div>
                         """,
             unsafe_allow_html=True
                             )
            import time
            time.sleep(1)
            st.rerun()

    if st.session_state.photo_tab=='upload':
        uploaded_files = st.file_uploader('choose image files', type=['jpg','png','jpeg'],accept_multiple_files=True,key='dialog_upload')

        if uploaded_files:
            for f in uploaded_files:
                st.session_state.attendance_images.append(Image.open(f))
            st.markdown(
                            """
                            <div style="
                            position: fixed;
                            top: 20px;
                            right: 20px;
                            background-color: #f0f0f0;
                            padding: 10px 20px;
                            border-radius: 8px;
                            box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
                            z-index: 1000;
                            ">
                            <span style="color:black; font-size:16px;">Photo Uploaded Sucessfully✅</span>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
            import time                               
            time.sleep(2)
            st.rerun()
            st.divider()
            if st.button('Done', type='primary',width='stretch'):
                st.rerun()

            