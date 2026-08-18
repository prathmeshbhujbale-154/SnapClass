import streamlit as st
from src.database.db import enroll_subject_to_Student
from src.database.config import supabase

import time


@st.dialog("Enroll InSubject")
def enroll_dialog():
    st.write("Enter the subect code povided by teacher to enroll")
    join_code = st.text_input("subject_code", placeholder="CS101")

    if st.button("Enroll Now",type="primary", width="stretch"):
        if join_code:
            res = supabase.table("subjects").select("subject_id, name, subject_code").eq("subject_code", join_code).execute()
            if res.data:
                subject = res.data[0]
                student_id = st.session_state.student_data["student_id"]

                check= supabase.table("subject_students").select("*").eq("subject_id", subject["subject_id"]).eq("student_id", student_id).execute()
                if check.data:
                    st.warning("You are already enrolledin this program ")
                else:
                    enroll_subject_to_Student(student_id, subject["subject_id"])
                    st.success("Successfully Enrolled!")
                    time.sleep(1)
                    st.rerun()
        else:
            st.warning("Please Enter Subject Code")