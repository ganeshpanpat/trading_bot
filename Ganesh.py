import streamlit as st
import datetime
import time
st.header("Welcome To App")
g=st.button(label="Run")
tm=st.empty
with st.empty():
    for seconds in range(10):
        st.write(f"⏳ {datetime.datetime.now()}")
        time.sleep(1)
    st.write("✔️ 1 minute over!")
if g:
  st.write('hi')
  st.write(datetime.datetime.now())
    
  
