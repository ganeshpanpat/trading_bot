import streamlit as st
import datetime
st.header("Welcome To App")
g=st.button(label="Run")
if g:
  st.write('hi')
  st.write(datetime.datetime.now())
  
