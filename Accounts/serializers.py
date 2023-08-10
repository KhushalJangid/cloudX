from .models import User,Student

def studentSerializer(st):
    data = {
    "rollno":st.rollno,
    "batch":st.batch,
    "f_name":st.f_name,
    "f_phone":st.f_phone, 
    "m_name":st.m_name,
    "m_phone":st.m_phone,
    "gender":st.gender ,
    "dob":st.dob.strftime("%Y-%m-%d"),
    "address":st.address 
    }
    return data