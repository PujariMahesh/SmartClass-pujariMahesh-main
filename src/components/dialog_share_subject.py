import streamlit as st
import segno
import io


@st.dialog("🔗 Share Class")
def share_subject_dialog(subject_name, subject_code):

    app_domain = "snapclass-main.streamlit.app"
    join_url = f"{app_domain}/?join-code={subject_code}"

    # Generate QR Code
    qr = segno.make(join_url)
    buffer = io.BytesIO()
    qr.save(buffer, kind="png", scale=8, border=2)

    st.markdown(
        f"""
        <div style='text-align:center;margin-bottom:20px;'>
            <h8 style='color:#1E3A8A;margin-bottom:5px;'>📚 Subject:{subject_name}</h8>
            <p style='color:gray;font-size:16px;'>
                Share the class link or ask students to scan the QR Code.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([1, 1.1], vertical_alignment="center")

    # LEFT SIDE
    with left:

        st.markdown("#### 🌐 Class Link")
        st.text_input(
            "Class Link",
            value=join_url,
            disabled=True,
            label_visibility="collapsed",
        )

        st.markdown("#### 🔑 Join Code")
        st.text_input(
            "Join Code",
            value=subject_code,
            disabled=True,
            label_visibility="collapsed",
        )
        st.markdown("""
                <div style="
                margin-top:20px;
                font-size:18px;
                font-weight:600;
                line-height:1.6;
                ">
                📢 Share this link or join code with your students.
                </div>
                """, unsafe_allow_html=True)

    # RIGHT SIDE
    with right:

        st.markdown(
            "<h4 style='text-align:center;'>📱 Scan QR Code</h4>",
            unsafe_allow_html=True,
        )

        st.image(
            buffer.getvalue(),
            width=300,
        )


    st.divider()


    st.markdown("""
                <div style="
                margin-top:20px;
                font-size:18px;
                font-weight:600;
                line-height:1.6;
                ">
                💡 Students can join either by scanning the QR Code or by entering the Join Code.
                </div>
                """, unsafe_allow_html=True)


    