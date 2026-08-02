import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

from src.database.db import check_teacher_exist,create_teacher, teacher_login

def teacher_screen():

    style_background_dashboard()
    style_base_layout()


    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif "teacher_login_type" not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()


def teacher_dashboard():
    teacher_data = st.session_state.teacher_data

    st.header(f"""Welcome, {teacher_data['name']} """ )
def login_teacher(username,password):
    if not username or not password :
        return False 

    teacher = teacher_login(username, password)

    if teacher:
        st.session_state.user_role = "teacher"
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True

    return False


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
        if st.button("Login",icon=":material/passkey:", type="secondary", key="loginbtn", shortcut="control+enter",width="stretch"):
            if login_teacher(teacher_username, teacher_pass):
                st.toast("welcome  back!",icon="✋") 
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid Username or password")
    with btc2:
        if st.button("Register",icon=":material/passkey:", type="primary", key="registerbtn",width="stretch"):
            st.session_state.teacher_login_type = "register"

    footer_dashboard()

def register_teacher(teacher_username,teacher_name,teacher_pass,teacher_confirm_pass):
        if not teacher_username or not teacher_name or not teacher_pass or not teacher_confirm_pass:
            return False, "all fields are required"
        if check_teacher_exist(teacher_username):
            return False, "Username already taken"
        if  teacher_pass != teacher_confirm_pass:
            return False, "password doen't match"

        try: 
            create_teacher(teacher_username, teacher_pass, teacher_name)
            return True, "Successfully Created! login Now"
        except Exception as e:
            return False, "unexpected error!"
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
        if st.button("Register now",icon=":material/passkey:", type="primary", key="registerbtn",width="stretch"):
            success, message =register_teacher(teacher_username,teacher_name,teacher_pass,teacher_confirm_pass)
            if success:
                st.success(message)
                import time
                time.sleep(1)
                st.session_state.teacher_login_type = "login"
                st.rerun()
            else:
                st.error(message)


    with btc2:
        if st.button("Login Instead",icon=":material/passkey:", type="secondary", key="loginbtn", shortcut="control+enter",width="stretch"):
            st.session_state.teacher_login_type = 'login'

    footer_dashboard()

