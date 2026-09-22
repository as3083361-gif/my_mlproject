import streamlit as st



def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background:#5865F2!important;
                }
            

            .stApp div[data-testid="stColumn"]{
                background-color:#E0E3FF !important;
                padding:2.5rem !important;
                border-radius: 5rem !important;
            }    

        </style>

    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background:#E0E3FF!important;
                }

        </style>

    """, unsafe_allow_html=True)




def style_base_layout():
    st.markdown("""
        <style>
            
              @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Outfit:wght@100..900&display=swap');
              @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Outfit:wght@100..900&display=swap');  

              #MainMenu,footer,header {
                  visibility: hidden!important;

              }
              .block-container {
                  padding-top: 1.5rem!important;
              }



              h1 {
                 font-family: 'Climate Crisis', sans-serif!important;
                 font-size: 2rem!important;
                 line-height: 1.2!important;
                 margin-bottom: 0!important;  

              }
              h2 {
                 font-family: 'Climate Crisis', sans-serif!important;
                 font-size: 1.3rem!important;
                 line-height: 1.2!important;
                 margin-bottom: 0!important;

             }

              h3,h4,p{
                 font-family: 'Outfit', sans-serif!important;
              }
              button[kind="primary"] {
                 border-radius: 1.5rem!important;
                 background: #EB459E!important;
                 color: white!important;
                 padding: 10px 20px!important;
                 border: none!important;
                 transition: background-color 0.25s ease-in-out!important;
              }
              button[kind="secondary"] {
                 border-radius: 1.5rem!important;
                 background: #EB459E!important;
                 color: white!important;
                 padding: 10px 20px!important;
                 border: none!important;
                transition: background-color 0.25s ease-in-out!important;
              }
              button[kind="tertiary"] {
                 border-radius: 1.5rem!important;
                 background: #EB459E!important;
                 color: white!important;
                 padding: 10px 20px!important;
                 border: none!important;
                 transition: background-color 0.25s ease-in-out!important;  
              }
              button:hover {
                    transition: scale(1.05);
                } 

        </style>
    
    """, unsafe_allow_html=True)