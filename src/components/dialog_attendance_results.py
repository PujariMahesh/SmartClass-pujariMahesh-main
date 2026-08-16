import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase

from PIL import Image

from src.database.db import create_attendance



def show_attendance_results(df,logs):
    st.markdown(
            "<h8>Attendance Reports</h8>",
            unsafe_allow_html=True)

    st.markdown(
        "<h5>Please review attendance before conforming.</h5>",
        unsafe_allow_html=True)
    st.dataframe(df, hide_index=True, width='stretch')

    col1, col2=st.columns(2)

    with col1:
        if st.button('Discard',width='stretch'):
            st.session_state.voice_attendance_results = None
            st.session_state.attendance_image=[]
            st.rerun()

    with col2:
        if st.button('Confirm & Save', width='stretch',type='primary'):
            try:
                create_attendance(logs)
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
                            <span style="color:black; font-size:16px;">Attendance Taken ✅</span>
                            </div>
                            """,
                            unsafe_allow_html=True
                            )
                st.session_state.attendance_images = []
                st.session_state.voice_attendance_results= None
            except Exception as e:
                
                st.markdown(
                    f"""
                    <div style="
                        background-color: #fee2e2;
                        color: #991b1b;
                        padding: 12px 18px;
                        border-radius: 10px;
                        border: 1px solid #ef4444;
                        margin-top: 20px;
                        font-weight: 600;
                    ">
                        ❌ Sync failed!<br><br>
                        {str(e)}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

@st.dialog("Attendance Reports")
def attendance_result_dialog(df, logs):
    show_attendance_results(df, logs)

                









                
    