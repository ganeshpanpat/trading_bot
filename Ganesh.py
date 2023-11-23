import streamlit as st
import datetime
import time
st.header("Welcome To App")
g=st.button(label="Run")
tm=st.empty
if g:
  st.write('hi')
  st.write(datetime.datetime.now())
  for i in range(0,10):
    tm.text=datetime.datetime.now()
    time.sleep(1)
    
  
