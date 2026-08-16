import streamlit as st
from src.database.db import create_subject




@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter the details of new subject")
    st.markdown(
        "<h5>Subject Code</h5>",
        unsafe_allow_html=True)
    sub_id=st.text_input("",placeholder='CS101',label_visibility="collapsed")
    st.markdown(
            "<h5>Subject Name</h5>",
            unsafe_allow_html=True)
    sub_name=st.text_input("",placeholder='Introduction  to MachineLearning',label_visibility="collapsed")
    st.markdown(
                "<h5>Section</h5>",
                unsafe_allow_html=True)
    sub_section=st.text_input("",placeholder='A',label_visibility="collapsed")
        
    
    



    if st.button("Create Subject Now", type='primary',width='stretch'):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id,sub_name,sub_section,teacher_id)
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
                                <span style="color:black; font-size:16px;">Subject Created!sucessfully✅</span>
                                </div>
                                    """,
                                        unsafe_allow_html=True
                            )
                st.rerun()

            except Exception as e:
                st.error(f"Error:{str(e)}")
        else:
            st.warning("Please fill all the fields")                   
                                                
                