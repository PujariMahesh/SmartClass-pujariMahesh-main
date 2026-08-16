import streamlit as st



def style_background_home():
    

    st.markdown("""
        <style>
                .stApp {
                background-color: #010E21;
         }    
        </style>    
                
         """,
          unsafe_allow_html=True)
    


    
def style_background_dashboard():
    

    st.markdown("""
        <style>
                .stApp {
                background-color: #EAF4FF !important;
                }    
        </style>    
                
         """,
          unsafe_allow_html=True)
    

def style_base_layout():
    

    st.markdown("""
        <style>
                
            @import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&family=Titan+One&display=swap');
                
            @import url('https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200..1000;1,200..1000&display=swap');
                
                /*hide top bar of streamlit*/
                MainMenu, footer, header{
                visibility: hidden;
                
                }

                .block-container{
                padding-top:1.5rem !important;
                }

                h1{
                    font-family:"Titan One", sans-serif !important;
                    font-size:4.5rem !important;
                    line-height:0.1 !important;
                    margin-bottom:0rem !important;
                    font-weight: 500 !important;
                    font-style: normal !important;
                    color: #FFFFFF !important;
                    }
                h2{
                    font-family: "Nunito", sans-serif !important;
                    font-size:1.5rem !important;
                    font-optical-sizing: auto !important;
                    line-height:0.1 !important;
                    font-weight: 500 !important;
                    font-style: normal !important;
                    color: #D6E4F0 !important;
                    }
                h3{
                    font-family:"Titan One", sans-serif !important;
                    font-size:1.4rem !important;
                    line-height:1 !important;
                    margin-bottom:0rem !important;
                    font-weight: 500 !important;
                    font-style: normal !important;
                    color: #070791 !important;
                    
                }
                h4{
                    font-family:"Titan One", sans-serif !important;
                    font-size:1.4rem !important;
                    line-height:1 !important;
                    margin-bottom:0rem !important;
                    font-weight: 500 !important;
                    font-style: normal !important;
                    color: #070791 !important;
                    text-align:center !important;
                }
                h5{
                    font-family: "Nunito", sans-serif !important;
                    font-size:0.8rem !important;
                    line-height:0.1 !important;
                    font-weight: 800 !important;
                    font-style: normal !important;
                    color: #000000 !important;
                    margin-bottom: 0px !important;
                }
                h6{
                    font-family: "Nunito", sans-serif !important;
                    font-size:0.8rem !important;
                    line-height:0.1 !important;
                    font-weight: 800 !important;
                    font-style: normal !important;
                    color: #000000 !important;
                    margin-bottom: 0px !important;
                }
                h7{
                    font-family: "Nunito", sans-serif !important;
                    font-size:1.5rem !important;
                    font-optical-sizing: auto !important;
                    line-height:0.1 !important;
                    font-weight: 500 !important;
                    font-style: normal !important;
                    color:#070791 !important;
                    }
                h8{
                    font-family: "Nunito", sans-serif !important;
                    font-size:1.4rem !important;
                    line-height:0.1 !important;
                    font-weight: 800 !important;
                    font-style: normal !important;
                    color: #000000 !important;
                    margin-bottom: 0px !important;
                    }
                
                p{
                    font-family: "Nunito", sans-serif !important;
                    font-size:0.8rem !important;
                    line-height:0.1 !important;
                    font-weight: 800 !important;
                    font-style: normal !important;
                    color: #FFFFFF !important;
                }
                
                
                
    
                div.stButton > button[kind="primary"] {
                    border-radius: 3.5rem !important;
                    background-color: #2196F3 !important; /* Blue */
                    color: #FFFFFF !important;
                    padding: 10px 20px !important;
                    font-size: 5px !important; 
                    border:2px solid #000000 !important;
                    transition: transform 0.25s ease-in-out !important;
                }
                div.stButton > button:hover[kind="primary"] {
                    transform: scale(1.05) !important;
                box-shadow: 0px 6px 10px rgba(0,0,0,0.3);
                    }

                    
                div.stButton > button[kind="secondary"] {
                                       border-radius: 3.5rem !important;
                                       background-color: #2196F3 !important; /* Blue */
                                       color: #FFFFFF !important;
                                       padding: 10px 20px !important;
                                       font-size: 5px !important; 
                                       border:2px solid #000000 !important;
                                       transition: transform 0.25s ease-in-out !important;
                                   }
                                   div.stButton > button:hover[kind="secondary"] {
                                       transform: scale(1.05) !important;
                                   box-shadow: 0px 6px 10px rgba(0,0,0,0.3);
                                       } 

                div.stButton > button[kind="tertiary"] {
                                    border-radius: 3.5rem !important;
                                    background-color: #D6E450 !important; /* Blue */
                                    color: #000000 !important;
                                    padding: 10px 20px !important;
                                    font-size: 5px !important; 
                                    border:2px solid #000000 !important;
                                    transition: transform 0.25s ease-in-out !important;
                                }
                                div.stButton > button:hover[kind="tertiary"] {
                                    transform: scale(1.05) !important;
                                box-shadow: 0px 6px 10px rgba(0,0,0,0.3);
                                    }

                

                </style>
         """,
          unsafe_allow_html=True)
    