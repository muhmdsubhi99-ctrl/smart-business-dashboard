import streamlit as st
import requests

# ==========================
# Config
# ==========================
API_URL = "https://smart-business-api.onrender.com"  # ضع رابط Render الجديد هنا

# ==========================
# Login
# ==========================
st.title("🔥 Smart Business SaaS Dashboard")

if "token" not in st.session_state:
    st.session_state.token = None

def login():
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        res = requests.post(f"{API_URL}/token", data={"username": email, "password": password})
        if res.status_code == 200:
            st.session_state.token = res.json()["access_token"]
            st.success("Logged in successfully!")
        else:
            st.error("Invalid credentials")

if not st.session_state.token:
    login()
else:
    st.success("✅ Logged in")
    headers = {"Authorization": f"Bearer {st.session_state.token}"}

    # ==========================
    # Dashboard Sections
    # ==========================
    st.subheader("Companies")
    companies = requests.get(f"{API_URL}/company/", headers=headers)
    st.write(companies.json() if companies.status_code==200 else "No companies found")

    st.subheader("Employees Compensation")
    employee_id = st.number_input("Employee ID", min_value=1)
    if st.button("Calculate Compensation"):
        res = requests.get(f"{API_URL}/compensation/{employee_id}", headers=headers)
        st.write(res.json() if res.status_code==200 else "Error calculating")

    st.subheader("Sales Analytics")
    company_id = st.number_input("Company ID for Sales", min_value=1)
    if st.button("Get Sales"):
        res = requests.get(f"{API_URL}/sales/{company_id}", headers=headers)
        st.write(res.json() if res.status_code==200 else "No sales found")
