import streamlit as st

def load_developers():

    st.title("Developers")

    col1,col2,col3,col4=st.columns(4)

    with col1:
        st.markdown(
            """
            <div style="text-align: center;">
                <h2>Sanskar</h2>
            
            </div>
            """,
            unsafe_allow_html=True
        )
        st.image("./sanskar.jpg")
        
        

    with col2:
        st.markdown(
            """
            <div style="text-align: center;">
                <h2>Vanshita</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        
        st.image("./sanskar.jpg")

    with col3:
        st.markdown(
            """
            <div style="text-align: center;">
                <h2>Abhishek</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    
        st.image("./sanskar.jpg")

    with col4:
        st.markdown(
            """
            <div style="text-align: center;">
                <h2>Devi</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        
        st.image("./sanskar.jpg")
