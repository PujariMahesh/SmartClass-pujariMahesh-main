import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.components.subject_card import subject_card
from src.database.db import check_teacher_exists, create_teacher, teacher_login,get_teacher_subjects, get_attendance_for_teacher
from src.components.dialog_create_subject import create_subject_dialog
from src.components.dialog_share_subject import share_subject_dialog
from src.components.dialog_add_photo import add_photos_dialog
from src.pipelines.face_pipeline import predict_attendance
import numpy as np

from src.components.dialog_attendance_results import attendance_result_dialog
from datetime import datetime
from src.database.config import supabase
import pandas as pd

from src.components.dialog_voice_attendance import voice_attendance_dialog
def teacher_screen():
   
     style_base_layout()
     style_background_dashboard()
    
     if "teacher_data" in st.session_state:
          teacher_dashboard()
     elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=="login":
          teacher_screen_login()
     elif st.session_state.teacher_login_type=="register":
          teacher_screen_register()



def teacher_dashboard():
     teacher_data=st.session_state.teacher_data
     c1,c2=st.columns(2,vertical_alignment='center',gap='xxlarge')
     with c1:
              header_dashboard()
     with c2:
               if st.button("Logout",type='secondary',key='loginbackbtn',shortcut="control+backspace"):
                    st.session_state['is_logged_in']=False
                    del st.session_state.teacher_data
                    st.rerun()

     st.markdown(
             f"<h3 style='color:blue;'>👋Welcome!,{teacher_data['name']}</h3>",
             unsafe_allow_html=True
         )
     st.space()
     if "current_teacher_tab" not in st.session_state:
          st.session_state.current_teacher_tab='take_attendance'


     tab1,tab2,tab3=st.columns(3)



     with tab1:
         type1="tertiary" if st.session_state.current_teacher_tab=='take_attendance' else "primary"
         if st.button('Take Attendance',type=type1,width='stretch',icon=':material/ar_on_you:'):
          st.session_state.current_teacher_tab='take_attendance'
          st.rerun()
     with tab2:
          type2="tertiary" if st.session_state.current_teacher_tab=='manage_subjects' else "primary"
    
          if st.button('Manage Subjects',type=type2,width='stretch',icon=':material/book_ribbon:'):
               st.session_state.current_teacher_tab='manage_subjects'
               st.rerun()
     with tab3:
          type3="tertiary" if st.session_state.current_teacher_tab=='attendance_records' else "primary"

          if st.button('Attendance Records',type=type3,width='stretch',icon=':material/cards_stack:'):
               st.session_state.current_teacher_tab='attendance_records'
               st.rerun()
     st.divider()
     if st.session_state.current_teacher_tab=="take_attendance":
          teacher_tab_take_attendance()
     if st.session_state.current_teacher_tab=="manage_subjects":
               teacher_tab_manage_subjects()
     if st.session_state.current_teacher_tab=="attendance_records":
                    teacher_tab_attendance_records()
          

     footer_dashboard()  



def teacher_tab_take_attendance():
     teacher_id=st.session_state.teacher_data['teacher_id']
     st.markdown(
                  f"<h8 style='color:blue;'>Take AI Attendance</h8>",
                  unsafe_allow_html=True
              )
     if 'attendance_images'not in st.session_state:
          st.session_state.attendance_images=[]

     subjects=get_teacher_subjects(teacher_id)
     if not subjects:
          st.warning("you haven't created any subjects yet! Please create one to begin!")
          return
     subject_options={f"{s['name']}-{s['subject_code']}":s['subject_id'] for s in subjects}
     col1, col2 = st.columns([3,1])

     with col1:
          with col1:

                    st.markdown(
        "<h5 style='color:#1E3A8A;'>Select Subject</h5>",
        unsafe_allow_html=True
    )

     selected_subject_label = st.selectbox(
        "Select Subject",
        options=list(subject_options.keys()),
        label_visibility="collapsed"
    )

     selected_subject_id = subject_options[selected_subject_label]
     with col2:
               if st.button('Add Photos',type='primary',icon=':material/photo_prints:',width='stretch'):
                    add_photos_dialog()
               selected_subject_id = subject_options[selected_subject_label]
               
     st.divider()
     if st.session_state.attendance_images:
          st.markdown(
                            f"<h8 style='color:blue;'>Added Photos</h8>",
                            unsafe_allow_html=True
                        )
          gallery_cols=st.columns(4)


          for idx, img in enumerate(st.session_state.attendance_images):
               with gallery_cols[idx % 4]:
                    st.image(img,width='stretch',caption=f'photo{idx+1}')
               has_photos = bool(st.session_state.attendance_images)

          c1,c2,c3=st.columns(3)

          with c1:
               if st.button('Clear all photos', width='stretch',type='tertiary',icon=':material/delete:', disabled= not has_photos):
                    st.session_state.attendance_images=[]
                    st.rerun()

          with c2:
               if st.button('Run Face Analysis',width='stretch',type='secondary',icon=':material/analytics:',disabled=not has_photos):
                     with st.spinner('Deep Scanning classroom photos...'):
                         all_detected_id={}

                         for idx, img in enumerate(st.session_state.attendance_images):
                              img_np = np.array(img.convert('RGB'))
                              detected,_, _=predict_attendance(img_np)



                              if detected:
                                   for sid in detected.keys():
                                        student_id = int(sid)

                                        all_detected_id.setdefault(student_id,[]).append(f"Photo{idx+1}")                    
                         enrolled_res = supabase.table('subject_students').select("*,students(*)").eq('subject_id',selected_subject_id).execute()
                         enrolled_students = enrolled_res.data


                         if not enrolled_students:
                              st.warning('No students enrolled in this course')
                         else:
                              results,attendance_to_log=[],[]

                              current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                              for node in enrolled_students:
                                   student = node['students']
                                   source = all_detected_id.get(int(student['student_id']),[])
                                   is_present= len(source) > 0
                                   results.append({
                                        "Name":student['name'],
                                        "ID":student['student_id'],
                                        "Source":", ".join(source) if is_present else"_",
                                        "Status": "✅ present" if is_present else "❌ Absent"
                                   })
                                   attendance_to_log.append({
                                        'student_id':student['student_id'],
                                        'subject_id':selected_subject_id,
                                        'timestamp':current_timestamp,
                                        'is_present':bool(is_present)
                                   })

                         attendance_result_dialog(pd.DataFrame(results), attendance_to_log)

          with c3:
               if st.button('Use Voice Attendance', type='primary',width='stretch', icon=':material/mic:'):
                    voice_attendance_dialog(selected_subject_id)



def teacher_tab_manage_subjects():

    teacher_id = st.session_state.teacher_data["teacher_id"]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            "<h3 style='color:#1E3A8A;'>📚 Manage Subjects</h3>",
            unsafe_allow_html=True,
        )

    with col2:
        if st.button("Create New Subject", width="stretch"):
            create_subject_dialog(teacher_id)

    subjects = get_teacher_subjects(teacher_id)

    if not subjects:
        st.warning("No subjects found. Create one above.")
        return

    for sub in subjects:

        stats = [
            ("👨‍🎓", "Students", sub["total_students"]),
            ("📚", "Classes", sub["total_classes"]),
        ]

        def share_btn(sub=sub):
            if st.button(
                "Share Code",
                key=f"share_{sub['subject_code']}",
                icon=":material/share:",
            ):
                share_subject_dialog(
                    sub["name"],
                    sub["subject_code"],
                )

        subject_card(
            name=sub["name"],
            code=sub["subject_code"],
            section=sub["section"],
            stats=stats,
            footer_callback=share_btn,
        )
    


def teacher_tab_attendance_records():
     st.markdown(
                    f"<h8 style='color:blue;'>Attendance Records</h8>",
                    unsafe_allow_html=True
               )

     teacher_id= st.session_state.teacher_data['teacher_id']

     records = get_attendance_for_teacher(teacher_id)

     if not records:
          return
     data=[]

     for r in records:
          ts=r.get('timestamp')

          data.append({
               "ts_group":ts.split(".")[0] if ts else None,
               "Time":datetime.fromisoformat(ts).strftime("%Y-%m_%d %I:%M %p") if ts else "N'A",
               "Subject":r['subjects']['name'],
               "Subject Code":r['subjects']['subject_code'],
               "is_present":bool(r.get('is_present',False))
          })

     df = pd.DataFrame(data)


     summary = (
          df.groupby(['ts_group', 'Time','Subject','Subject Code'])
          .agg(
               present_count=('is_present','sum'),
               total_count=('is_present','count')
          ).reset_index()

          )
     summary['Attendance Stats']=(
          "✅" + summary['present_count'].astype(str)+"/"
          + summary['total_count'].astype(str)+'Students'
     )

     display_df = (summary.sort_values(by='ts_group' ,ascending=False)
                    [['Time','Subject','Subject Code','Attendance Stats']]
                    )

     st.dataframe(display_df,width='stretch',hide_index=True)
     
def login_teacher(username,password):
     if not username or not password:
          return False
     teachers=teacher_login(username,password)
     if teachers:
          st.session_state.user_role='teacher'
          st.session_state.teacher_data=teachers
          st.session_state.is_logged_in=True
          return True
def teacher_screen_login():
     

     c1,c2=st.columns(2,vertical_alignment='center',gap='xxlarge')
     with c1:
         header_dashboard()
     with c2:
          if st.button("Go back to Home",type='secondary',key='loginbackbtn',shortcut="control+backspace"):
               st.session_state['login_type']=None
               st.rerun()

     st.markdown(f"""
            <div style="display:flex; align-items:center">
                <h4 style='text-align:'center';color:#010E21'>Login Using Password</h4>
            </div>
                    """, unsafe_allow_html=True)
     st.space()
     st.space()
     st.markdown(
    "<h5>Enter Username</h5>",
    unsafe_allow_html=True)
     teacher_username=st.text_input("",placeholder='Eg:@Mahivarma06',label_visibility="collapsed")
     st.markdown(
    "<h5>Enter Password</h5>",
    unsafe_allow_html=True)
     teacher_password=st.text_input("", placeholder='Password',type='password',label_visibility="collapsed")
     st.divider()
     btnc1,btnc2=st.columns(2)
     with btnc1:
          if st.button("Login",type='secondary',icon=':material/passkey:',width='stretch'):
               if login_teacher(teacher_username, teacher_password):
                    #st.toast("Welcome back!", icon="👋")
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
                              <span style="color:black; font-size:16px;">👋 Welcome back!</span>
                         </div>
                         """,
                         unsafe_allow_html=True
                         )
                    import time
                    time.sleep(1)
                    st.rerun()
               else:
                    st.error("Invalid username and password combo")
     with btnc2:
         if st.button("Register",type='primary',icon=':material/passkey:',width='stretch'):
              st.session_state.teacher_login_type='register'    
 
     footer_dashboard()



def register_teacher(teacher_username,teacher_name,teacher_pass,teacher_pass_confirm):
     if not teacher_username.strip() or not teacher_name.strip() or not teacher_pass.strip():
          return False,"All Fields are Required!" 
     if check_teacher_exists(teacher_username):
          return False, "Username Already Taken"
     if teacher_pass !=teacher_pass_confirm:
          return False, "Password doesn't match"
     
     try:
          create_teacher(teacher_username,teacher_pass,teacher_name)
          return True,"Sucessfully Created! Login Now" 
     except Exception as e:
          return False,"Unexpected Error!"
     




def teacher_screen_register():

     c1,c2=st.columns(2,vertical_alignment='center',gap='xxlarge')
     with c1:
         header_dashboard()
     with c2:
         if st.button("Go back to Home",type='secondary',key='loginbackbtn',shortcut="control+backspace"):
               st.session_state['login_type']=None
               st.rerun()


     st.markdown(f"""
            <div style="display:flex; align-items:center">
                <h4 style='text-align:left;color:#010E21'>Register Your Teacher Profile</h4>
            </div>
                    """, unsafe_allow_html=True)
     st.space()
     st.space()
     st.markdown(
    "<h5>Enter Name</h5>",
    unsafe_allow_html=True)
     teacher_name=st.text_input("",placeholder='Eg:Maheshvarma',label_visibility="collapsed")
     st.markdown(
    "<h5>Enter Username</h5>",
    unsafe_allow_html=True)
     teacher_username=st.text_input("",placeholder='Eg:@Mahivarma06',label_visibility="collapsed")
     st.markdown(
    "<h5>Enter Password</h5>",
    unsafe_allow_html=True)
     teacher_password=st.text_input("", placeholder='Password',type='password',label_visibility="collapsed")
     st.markdown(
    "<h5>Confirm Password</h5>",
    unsafe_allow_html=True)
     teacher_password_confirm=st.text_input("", placeholder='Re Enter Password',type='password',label_visibility="collapsed")

     st.divider()
     btnc1,btnc2=st.columns(2)
     with btnc1:
          if st.button("Register Now",type='secondary',icon=':material/passkey:',width='stretch'):
               success, message = register_teacher(teacher_username,teacher_name,teacher_password, teacher_password_confirm)   
               if success:
                    st.success(message)
                    import time
                    time.sleep(2)
                    st.session_state.teacher_login_type="login"
                    st.rerun()
               else:
                    st.error(message)

     with btnc2:
          if st.button("Login Instead",type='primary',icon=':material/passkey:',width='stretch'):     
               st.session_state.teacher_login_type='login'
     footer_dashboard()
    