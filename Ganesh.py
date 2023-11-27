import streamlit as st
import datetime
import time
import pandas as pd
import numpy as np
st.set_page_config(page_title="Algo App",layout="wide",initial_sidebar_state="expanded", )
if "user_name" not in st.session_state or st.session_state['user_name']=="Guest":
    st.session_state["user_name"]="Guest"
    st.session_state['login_time']="Guest"
    st.session_state['last_update']=datetime.datetime.now()-datetime.timedelta(minutes=5)
def get_dataframe():
    st.session_state['last_update' ]=datetime.datetime.now()
    return pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))
def login():
    if user_name=="Ganesh" and password=="1234":
        st.session_state["user_name" ]=user_name
        st.session_state['login_ time']=datetime.datetime.now().time().replace(microsecond=0)
        st.success("Login")
        st.rerun()
if st.session_state['user_name']=='Guest':
    st.header(f'Login')
    user_name=st.selectbox(label='Select User:',options=['Ganesh','Kalyani','Akshay'])
    password=st.text_input(label='Password',type='password')
    login_btn=st.button(label='Login')
    if login_btn: login()
if st.session_state['user_name']!='Guest':
    st.header(f'Welcome {st.session_state["user_name"]}')
    st.write(f'Last Login {st.session_state["login_time"]}')
    def manual_buy(symbol,ce_pe,index_ltp):
        st.sucess(f'Buy {symbol} {ce_pe} {index_ltp} {datetime.datetime.now()}')
    with st.sidebar:
        st.write('NIFTY')
        col1,col2=st.columns(2)
        with col1: nf_ce=st.button(label='Nifty Ce')
        with col2: nf_pe=st.button(label='Nifty Pe')
        st.write('BANKNIFTY')
        col3,col4=st.columns(2)
        with col3: bnf_ce=st.button(label='BNF Nifty Ce')
        with col4: bnf_pe=st.button(label='BNF Nifty Pe')
        col5,col6=st.columns(2)
        with col5:
            lot_size=st.number_input(label='Lot Size',min_value=1,max_value=10,value=1)
            target=st.number_input(label='Target',min_value=5, max_value=20,value=5)
        with col6:
            target_type=st.selection(label='Target Type', options=['Points','Per Cent'],index=0)
            sl=st.number_input(label='Stop Loss',min_value=5, max_value=20,value=5)
        if nf_ce:manual_buy('Nifty','CE',19700)
        if nf_pe:manual_buy('Nifty','PE',19700)
        if bnf_ce:manual_buy('Bank Nifty','CE',43700)
        if bnf_ce:manual_buy('Bank Nifty','PE',43700)
    update_time=st.empty()
    my_df=st.empty()
    while True:
        current_time=datetime.datetime.now()
        last_run=st.session_state['last_update']
        next_run=st.session_state['last_update'].replace(microsecond=0,second=0)+datetime.timedelta(minutes=1)
        if current_time>next_time:
            my_df.table(get_dataframe())
            update_time.text(f'Last Update {st.session_state["last_update"]}')
        time.sleep(60-datetime.datetime.now().second)
