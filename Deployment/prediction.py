import streamlit as st
import pickle
import json
import pandas as pd
import numpy as np

# Load Models
with open('model.pkl', 'rb') as file:
  modelsvc = pickle.load(file)

def run():
  # membuat judul
  st.title('Credit Form')
  # buat garis
  st.markdown('---')
  with st.form('Credit Form'):
    # limit balance
    limitBalance = st.slider('Limit Balance', min_value=0, max_value=1000000, value=200000)
    # field age
    sex = st.slider('Sex', min_value=1, value= 1, max_value=2, help='1 = Male, 2 = Female')
    # field edu
    edu = st.slider('Education Level', min_value=0,max_value=6,value=1, help='1 = Graduate School, 2 = University, 3 = High School, 0,4,5,6 = Others' )
    # field marital
    marital = st.slider('Marital Status', min_value=0, max_value=3,value=1, help='1 = Married, 2 = Single, 3 = Divorce, 0 = Others')
    # field age
    age = st.number_input('Age', min_value=16, value= 25, max_value=60)
    # field pay 0
    pay0 = st.slider('Repayment Status September', min_value=-2, max_value=9, value=-1, help='-2= No consumption, -1=pay duly,0= The use of revolving credit,  1=payment delay for one month, 2=payment delay for two months, -> 8=payment delay for eight months, 9=payment delay for nine months and above')
    # field pay 2
    pay2 = st.slider('Repayment Status August', min_value=-2, max_value=9, value=-1, help='-2= No consumption, -1=pay duly,0= The use of revolving credit,  1=payment delay for one month, 2=payment delay for two months, -> 8=payment delay for eight months, 9=payment delay for nine months and above')
    # field pay 3
    pay3 = st.slider('Repayment Status July', min_value=-2, max_value=9, value=-1, help='-2= No consumption, -1=pay duly,0= The use of revolving credit,  1=payment delay for one month, 2=payment delay for two months, -> 8=payment delay for eight months, 9=payment delay for nine months and above')
    # field pay 4
    pay4 = st.slider('Repayment Status June', min_value=-2, max_value=9, value=-1, help='-2= No consumption, -1=pay duly,0= The use of revolving credit,  1=payment delay for one month, 2=payment delay for two months, -> 8=payment delay for eight months, 9=payment delay for nine months and above')
    # field pay 5
    pay5 = st.slider('Repayment Status May', min_value=-2, max_value=9, value=-1, help='-2= No consumption, -1=pay duly,0= The use of revolving credit,  1=payment delay for one month, 2=payment delay for two months, -> 8=payment delay for eight months, 9=payment delay for nine months and above')
    # field pay 6
    pay6 = st.slider('Repayment Status April', min_value=-2, max_value=9, value=-1, help='-2= No consumption, -1=pay duly,0= The use of revolving credit,  1=payment delay for one month, 2=payment delay for two months, -> 8=payment delay for eight months, 9=payment delay for nine months and above')
    # field billamt 1
    bill1 = st.number_input('Bill Amount Statement in September', min_value=0, value= 10000, max_value=1000000)
    # field billamt 2
    bill2 = st.number_input('Bill Amount Statement in August', min_value=0, value= 10000, max_value=1000000)
    # field billamt 3
    bill3 = st.number_input('Bill Amount Statement in July', min_value=0, value= 10000, max_value=1000000)
    # field billamt 4
    bill4 = st.number_input('Bill Amount Statement in June', min_value=0, value= 10000, max_value=1000000)
    # field billamt 5
    bill5 = st.number_input('Bill Amount Statement in May', min_value=0, value= 10000, max_value=1000000)
    # field billamt 6
    bill6 = st.number_input('Bill Amount Statement in April', min_value=0, value= 10000, max_value=1000000)
    # field pay 1
    payamnt1 = st.number_input('Amount of previous payment in September', min_value=0, value= 10000, max_value=1000000)
    # field pay 2
    payamnt2 = st.number_input('Amount of previous payment in August', min_value=0, value= 10000, max_value=1000000)
    # field pay 3
    payamnt3 = st.number_input('Amount of previous payment in July', min_value=0, value= 10000, max_value=1000000)
    # field pay 4
    payamnt4 = st.number_input('Amount of previous payment in June', min_value=0, value= 10000, max_value=1000000)
    # field pay 5
    payamnt5 = st.number_input('Amount of previous payment in May', min_value=0, value= 10000, max_value=1000000)
    # field pay 6
    payamnt6 = st.number_input('Amount of previous payment in April', min_value=0, value= 10000, max_value=1000000)
    # garis
    st.markdown('---')

    # submit button
    submitted = st.form_submit_button('Predict')
  data_inf = {'limit_balance': limitBalance,
    'sex': sex,
    'education_level': edu,
    'marital_status': marital,
    'age': age,
    'pay_0': pay0,
    'pay_2': pay2,
    'pay_3': pay3,
    'pay_4': pay4,
    'pay_5': pay5,
    'pay_6': pay6,
    'bill_amt_1': bill1,
    'bill_amt_2': bill2,
    'bill_amt_3': bill3,
    'bill_amt_4': bill4,
    'bill_amt_5': bill5,
    'bill_amt_6': bill6,
    'pay_amt_1': payamnt1,
    'pay_amt_2': payamnt2,
    'pay_amt_3': payamnt3,
    'pay_amt_4': payamnt4,
    'pay_amt_5': payamnt5,
    'pay_amt_6': payamnt6,}
  data_inf = pd.DataFrame([data_inf])
  st.dataframe(data_inf)

  if submitted:
    predictions = modelsvc.predict(data_inf)
    # buat garis
    st.markdown('---')
    st.write('### Default Payment Next Month: ', str(int(predictions)))
  # buat garis
  st.markdown('---')


if __name__ == '__main__':
  run()
  