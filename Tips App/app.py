import joblib
import streamlit as st
st.set_page_config(page_title="My Tip Prediction Model",page_icon="💰")
st.title("Machine Learning Model Deployment")
st.write("""My **Tip Prediction** Model vs **Total Bill**""")
mymodel=joblib.load('tips.pkl')
exp=st.sidebar.slider("Bill (in $),1.00,50,6.00")
tip=mymodel.predict([[exp]])
st.write(f"Bill- ",exp)
st.write(f"Tip- ",round(float(tip))) 