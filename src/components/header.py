import streamlit as st

def header_home():
    
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("logo1.jpg",use_column_width=True)
    
    
    st.markdown("""
        
            <div>
                <h1 style='text-align:center;'>SMART CLASS</h1>              
            </div>

                """,
                unsafe_allow_html=True)
    
    st.markdown(
        """
        <style>
        .header-container {
            text-align: center;
            margin-top:10px;
        }
        .header-container h1 {
            font-size:clamp(1.5rem, 5vm,3rem);   /* scales with screen width */
            color: #2E86C1;   /* optional styling */
            margin:0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )








def header_dashboard():
    col4,col5,col6=st.columns([1,1,1])
    with col4:
        st.image("logo2.jpg",width=100)
    with col5:
        st.markdown(f"""
            <div style="display:flex; align-items:center">
                <h3 style='text-align:left;color:#010E21'>SMART<br/>CLASS</h3>
            </div>
                    """, unsafe_allow_html=True)
