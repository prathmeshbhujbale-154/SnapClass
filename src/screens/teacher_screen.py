import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard


def teacher_screen():

    style_background_dashboard()
    style_base_layout()

    
    if "teacher_login_type" not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()

def teacher_screen_login():
    c1,c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("go back to Home", type="secondary", key="loginbackbtn", shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.rerun()


    st.header("Login using password", text_alignment="center")
    st.space()
    st.space()
    teacher_username = st.text_input("Enter username", placeholder="username")

    teacher_pass = st.text_input("Enter password", type="password", placeholder="password" )

    st.divider()

    btc1, btc2 = st.columns(2)
    with btc1:
        st.button("Login",icon=":material/passkey:", type="secondary", key="loginbtn", shortcut="control+enter",width="stretch")
    with btc2:
        if st.button("Register",icon=":material/passkey:", type="primary", key="registerbtn",width="stretch"):
            st.session_state.teacher_login_type = "register"

    footer_dashboard()



def teacher_screen_register():
    c1,c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("go back to Home", type="secondary", key="loginbackbtn", shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.rerun()

    st.header("Register your profile", text_alignment="center")

    st.space()
    st.space()
    teacher_username = st.text_input("Enter username", placeholder="username")

    teacher_name = st.text_input("Enter name", placeholder="name")

    teacher_pass = st.text_input("Enter password", type="password", placeholder="password" )

    teacher_confirm_pass = st.text_input("confirm password",type="password", placeholder="confirm your password")
    st.divider()

    btc1, btc2 = st.columns(2)
    with btc1:
        st.button("Register",icon=":material/passkey:", type="primary", key="registerbtn",width="stretch")

    with btc2:
        if st.button("Login Instead",icon=":material/passkey:", type="secondary", key="loginbtn", shortcut="control+enter",width="stretch"):
            st.session_state.teacher_login_type = 'login'

    footer_dashboard()

