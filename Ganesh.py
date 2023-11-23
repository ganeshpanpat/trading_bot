import streamlit as st
import datetime
import time
st.header("Welcome To App")
g=st.button(label="Run")
tm=st.empty
i=0
with st.empty():
    while True:
        i=i+1
        st.write(f"{i} ⏳ {datetime.datetime.now()}")
        time.sleep(1)
    st.write("✔️ 1 minute over!")
if g:
  st.write('hi')
  st.write(datetime.datetime.now())
    
  
