import streamlit as st
import datetime
import time
st.header("Welcome To App")
g=st.button(label="Run")
tm=st.empty
i=0
col1,col2=st.columns(2)
with col1:
    st.write('Nifty')
    nf_ce=st.button(label="Nifty CE")
    nf_pe=st.button(label="Nifty PE")
with col2:
    st.write('Bank Nifty')
    bnf_ce=st.button(label="Bank Nifty CE")
    bnf_pe=st.button(label="Bank Nifty PE")
with st.empty():
    while True:
        i=i+1
        st.write(f"{i} ⏳ {datetime.datetime.now()}")
        time.sleep(1)
    st.write("✔️ 1 minute over!")
if g:
  st.write('hi')
  st.write(datetime.datetime.now())
    
  
