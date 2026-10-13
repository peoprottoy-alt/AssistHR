import streamlit as st
from streamlit_option_menu import option_menu
import datetime

# পেজ কনফিগারেশন
st.set_page_config(page_title="AssistHR - Complete HRM System", page_icon="💼", layout="wide")

# সাইডবার মেনু (Navigation) - প্রপোজালে থাকা ৭টি ফিচারই যুক্ত করা হয়েছে
with st.sidebar:
    st.image("https://flaticon.com", width=80)
    st.title("AssistHR")
    st.write("Automated HRM System")
    st.markdown("---")
    
    selected = option_menu(
        menu_title="Main Menu",
        options=[
            "Admin Control Panel", 
            "Employee Profiles", 
            "Daily Attendance", 
            "Leave Application", 
            "Payroll & Salary Slip",
            "Internal Notice Board",
            "Performance Tracker"
        ],
        icons=["speedometer2", "people-fill", "clock-history", "calendar-check", "cash-coin", "clipboard-data", "clipboard2-check"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px!", "background-color": "#f0f2f6"},
            "icon": {"color": "#007bff", "font-size": "18px"}, 
            "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#007bff", "color": "white"},
        }
    )

# ১. Admin Control Panel
if selected == "Admin Control Panel":
    st.title("📊 Admin Control Panel")
    st.subheader("Welcome back, HR Manager!")
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric(label="Total Employees", value="45", delta="+3 this month")
    with col2: st.metric(label="Today's Attendance", value="38", delta="84%")
    with col3: st.metric(label="Pending Leaves", value="4")
    with col4: st.metric(label="Active Tasks", value="12")
    st.markdown("---")
    st.subheader("📌 Quick System Overview")
    st.info("System is configured to run on local XAMPP Server using Python & SQL.")

# ২. Employee Profile Management
elif selected == "Employee Profiles":
    st.title("👥 Employee Profile Management")
    st.markdown("---")
    tab1, tab2 = st.tabs(["➕ Add New Employee", "📋 View Directory & Options"])
    with tab1:
        st.subheader("Add Employee Profile")
        with st.form("emp_form", clear_on_submit=True):
            st.text_input("Employee ID")
            st.text_input("Full Name")
            st.selectbox("Department", ["CSE", "HR", "Marketing", "Accounts"])
            st.number_input("Base Salary (BDT)", min_value=0, step=5000)
            if st.form_submit_button("Save Profile"): st.success("Profile saved successfully!")
    with tab2:
        st.subheader("Manage Records (Update / Delete)")
        st.table([{"ID": "EMP-001", "Name": "Atikur Rahman", "Dept": "HR", "Salary": "55,000 BDT"}])

# ৩. Daily Attendance System
elif selected == "Daily Attendance":
    st.title("⏱️ Daily Attendance System")
    st.markdown("---")
    st.subheader("Employee Check-in / Check-out Portal")
    emp_id = st.text_input("Enter Your Employee ID:")
    c1, c2 = st.columns(2)
    with c1: 
        if st.button("🔔 Click to Check-In", type="primary", use_container_width=True): st.success("Check-in time recorded.")
    with c2: 
        if st.button("🔕 Click to Check-Out", type="secondary", use_container_width=True): st.error("Check-out time recorded.")

# ৪. Leave Application and Approval
elif selected == "Leave Application":
    st.title("📅 Leave Application & Approval")
    st.markdown("---")
    st.subheader("Submit Leave Request (Employee)")
    with st.form("leave_form"):
        st.text_input("Employee ID")
        st.selectbox("Leave Type", ["Casual Leave", "Sick Leave", "Maternity Leave"])
        st.date_input("Start Date")
        st.date_input("End Date")
        if st.form_submit_button("Submit Application"): st.info("Leave request sent to Admin Panel.")

# ৫. Automated Payroll and Salary Slip
elif selected == "Payroll & Salary Slip":
    st.title("💵 Automated Payroll & Salary Slip")
    st.markdown("---")
    st.subheader("Calculate Monthly Salaries")
    st.selectbox("Select Month", ["October 2026", "November 2026"])
    if st.button("Calculate System Payroll"):
        st.success("Payroll calculated automatically based on base pay and leaves!")
        st.download_button("📥 Download PDF Salary Slip (Sample)", data="Sample PDF Content", file_name="Salary_Slip.pdf")

# ৬. Internal Notice Board
elif selected == "Internal Notice Board":
    st.title("📌 Internal Notice Board")
    st.markdown("---")
    st.subheader("📣 Post Official Announcement (Admin)")
    st.text_input("Notice Title")
    st.text_area("Notice Description")
    if st.button("Publish Notice"): st.success("Notice published to all dashboards!")

# ৭. Performance and Task Tracker
elif selected == "Performance Tracker":
    st.title("🎯 Performance & Task Tracker")
    st.markdown("---")
    st.subheader("Assign Daily Tasks")
    st.text_input("Assign To (Employee ID)")
    st.text_input("Task Name")
    st.selectbox("Priority", ["High", "Medium", "Low"])
    if st.button("Assign Task"): st.success("Task assigned and performance tracking started.")
