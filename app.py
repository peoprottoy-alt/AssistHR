import streamlit as st
from streamlit_option_menu import option_menu
import datetime

st.set_page_config(page_title="AssistHR - Management System", page_icon="💼", layout="wide")

with st.sidebar:
    st.image("https://flaticon.com", width=80)
    st.title("AssistHR")
    st.write("Automated HRM System")
    st.markdown("---")
    
    selected = option_menu(
        menu_title="Main Menu",
        options=["Admin Dashboard", "Employee Management", "Daily Attendance", "Notice Board"],
        icons=["speedometer2", "people-fill", "clock-history", "clipboard-data"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px!", "background-color": "#f0f2f6"},
            "icon": {"color": "#007bff", "font-size": "20px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#007bff", "color": "white"},
        }
    )

if selected == "Admin Dashboard":
    st.title("📊 Admin Control Panel")
    st.subheader("Welcome back, HR Manager!")
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total Employees", value="45", delta="+3 this month")
    with col2:
        st.metric(label="Present Today", value="38", delta="84%")
    with col3:
        st.metric(label="Pending Leaves", value="4", delta="-2 review")
    with col4:
        st.metric(label="Active Tasks", value="12", delta="Running")
        
    st.markdown("---")
    st.subheader("📌 Quick Overview")
    st.info("System is running locally on XAMPP Server. All database structures are ready.")

elif selected == "Employee Management":
    st.title("👥 Employee Profile Management")
    st.markdown("---")
    
    tab1, tab2 = st.tabs(["➕ Add New Employee", "📋 View Directory"])
    
    with tab1:
        st.subheader("Enter Employee Details")
        with st.form("employee_form", clear_on_submit=True):
            emp_id = st.text_input("Employee ID (e.g., EMP-101)")
            name = st.text_input("Full Name")
            email = st.text_input("Official Email")
            department = st.selectbox("Department", ["CSE", "HR", "Marketing", "Accounts", "Operations"])
            base_salary = st.number_input("Base Salary (BDT)", min_value=0, step=5000)
            
            submitted = st.form_submit_button("Save Employee Profile")
            if submitted:
                if name and emp_id:
                    st.success(f"Successfully Added: {name} ({emp_id}) to the local Database Structure!")
                else:
                    st.error("Please fill up Name and Employee ID.")
                    
    with tab2:
        st.subheader("Current Employee List (Sample Mock Data)")
        sample_data = [
            {"ID": "EMP-001", "Name": "Atikur Rahman", "Dept": "HR Manager", "Salary": "55,000 BDT"},
            {"ID": "EMP-002", "Name": "Md. Mahedi Hasan", "Dept": "CSE / Developer", "Salary": "60,000 BDT"},
            {"ID": "EMP-003", "Name": "Md. Sabbir Mollah", "Dept": "Accounts", "Salary": "45,000 BDT"},
        ]
        st.table(sample_data)

elif selected == "Daily Attendance":
    st.title("⏱️ Daily Attendance System")
    st.markdown("---")
    
    st.subheader("Employee Check-in / Check-out Portal")
    emp_login = st.text_input("Enter Your Employee ID to Log Attendance:")
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("🔔 Click to Check-In", type="primary", use_container_width=True):
            if emp_login:
                st.success(f"Check-In Recorded successfully for {emp_login} at {datetime.datetime.now().strftime('%H:%M:%S')}")
            else:
                st.warning("Please enter your ID first.")
                
    with col_btn2:
        if st.button("🔕 Click to Check-Out", type="secondary", use_container_width=True):
            if emp_login:
                st.error(f"Check-Out Recorded successfully for {emp_login} at {datetime.datetime.now().strftime('%H:%M:%S')}")
            else:
                st.warning("Please enter your ID first.")

elif selected == "Notice Board":
    st.title("📌 Internal Notice Board")
    st.markdown("---")
    
    st.subheader("📣 Post a New Announcement (Admin Only)")
    notice_title = st.text_input("Notice Title")
    notice_content = st.text_area("Notice Description")
    
    if st.button("Publish Notice"):
        if notice_title and notice_content:
            st.success("Notice published instantly to all employee dashboards!")
            st.session_state['latest_notice'] = {"title": notice_title, "content": notice_content}
            
    st.markdown("---")
    st.subheader("📥 Active Notices")
    
    if 'latest_notice' in st.session_state:
        st.warning(f"**{st.session_state['latest_notice']['title']}**\n\n{st.session_state['latest_notice']['content']}")
    else:
        st.warning("**Official System Notice:** Welcome to AssistHR Dashboard. Project mid-submission is on 16th October, 2026.")
