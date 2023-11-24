import streamlit as st
import datetime
import time
import yfinance as yf
def get_stock_ltp(symbol):
    dt=yf.Ticker(symbol)
    ltp=round(dt.get_fast_info()['lastPrice'],2)
    chng=round(ltp-dt.get_fast_info()['regularMarketPreviousClose'],2)
    return (f'{symbol} LTP {ltp} {chng}')
with st.sidebar:
    st.write(f'{datetime.datetime.now()}')
    st.write(get_stock_ltp('^NSEI'))
    st.write(get_stock_ltp('^NSEBABK'))
st.header("Welcome To App")
g=st.button(label="Run")
tm=st.empty
global i
i=0
st.write('Nifty')
nf_ce=st.button(label="Nifty CE")
nf_pe=st.button(label="Nifty PE")
st.write('Bank Nifty')
bnf_ce=st.button(label="Bank Nifty CE")
bnf_pe=st.button(label="Bank Nifty PE")
if nf_ce:
    st.write('Nifty Ce Call Buy')
with st.empty():
    while True:
        i=i+1
        st.write(f"{i} ⏳ {datetime.datetime.now()}")
        time.sleep(1)
    st.write("✔️ 1 minute over!")
if g:
  st.write('hi')
  st.write(datetime.datetime.now())
    
  
