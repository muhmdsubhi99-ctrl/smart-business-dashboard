import streamlit as st
import requests
import os
from dotenv import load_dotenv  # هذه لتحميل المتغيرات من ملف .env

# تحميل المتغيرات من .env
load_dotenv()

# قراءة الرابط من المتغير BACKEND_URL
BACKEND_URL = os.getenv("BACKEND_URL", "https://smart-business-backend-j9ki.onrender.com")
import streamlit as st
import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
API_URL = os.getenv("API_URL")

st.set_page_config(page_title="Smart Business SaaS", layout="wide")
st.title("Smart Business SaaS Dashboard 🔥")

# =========================
# Companies
# =========================
st.header("Companies")

if st.button("Load Companies"):
    res = requests.get(f"{API_URL}/company/")
    data = res.json()
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.info("No companies found")

st.subheader("Add Company")
company_name = st.text_input("Company Name")
if st.button("Create Company"):
    if company_name:
        res = requests.post(
            f"{API_URL}/company/",
            params={"name": company_name}
        )
        st.success(res.json())

# =========================
# Employees
# =========================
st.header("Employees")

if st.button("Load Employees"):
    res = requests.get(f"{API_URL}/employee/")
    data = res.json()
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.info("No employees found")

st.subheader("Add Employee")
emp_name = st.text_input("Employee Name")
emp_company = st.number_input("Company ID", min_value=1)
emp_salary = st.number_input("Salary", min_value=0.0)

if st.button("Create Employee"):
    res = requests.post(
        f"{API_URL}/employee/",
        params={
            "name": emp_name,
            "company_id": emp_company,
            "salary": emp_salary
        }
    )
    st.success(res.json())

# =========================
# Sales
# =========================
st.header("Sales")

if st.button("Load Sales"):
    res = requests.get(f"{API_URL}/sale/")
    data = res.json()
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.info("No sales found")

st.subheader("Add Sale")
sale_company = st.number_input("Company ID for Sale", min_value=1)
sale_amount = st.number_input("Amount", min_value=0.0)

if st.button("Create Sale"):
    res = requests.post(
        f"{API_URL}/sale/",
        params={
            "company_id": sale_company,
            "amount": sale_amount
        }
    )
    st.success(res.json())

# =========================
# Smart Compensation
# =========================
st.header("Compensation Engine 💰")
comp_id = st.number_input("Employee ID", min_value=1)

if st.button("Calculate Bonus"):
    res = requests.get(f"{API_URL}/compensation/{comp_id}")
    st.json(res.json())
