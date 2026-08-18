import streamlit as st

def header_home():
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("logo1.jpg",width=600)

    st.markdown(
        """
        <div class="header-container">
            <h1>SMART CLASS</h1>
        </div>

        <style>
        .header-container {
            text-align: center;
            margin-top: 10px;
        }
        .header-container h1 {
            font-size: clamp(1.5rem, 5vw, 3rem); /* scales with screen width */
            color: #2E86C1;
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
