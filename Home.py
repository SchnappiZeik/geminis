import streamlit as st
    
st.set_page_config(
    page_title="Geminappi",
    page_icon="👋",
)


st.sidebar.success("Select a demo above.")
st.write("# Welcome to Gemini Streamlit! 👋")



st.markdown(
'''    
    周家聪是个卤蛋 demo
'''
)

if "key" not in st.session_state:
    st.session_state.key = NONE
    
key = st.sidebar.text_input("Your key", type="password")
if not key:
    st.info("Please add your key to continue.")
    st.stop()
else:
    st.session_state.key=key
