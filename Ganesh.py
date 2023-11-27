import streamlit as st
import datetime
import time
import pandas as pd
import numpy as np
st.set_page_config(page_title='Algo App',layout= 'wide',initial_sidebar_state='expanded',)
if 'user_name' not in st.session_state or st.session_state['user_name']=='Guest':
    st.session_state['user_name']='Guest'
    st.session_state['login_time']='Guest'
    st.session_state['last_update']=datetime.datetime.now()-datetime.timedelta(minutes=5)
def get_dateframe():
    st.session['last_update']=datetime.datetime.now()
