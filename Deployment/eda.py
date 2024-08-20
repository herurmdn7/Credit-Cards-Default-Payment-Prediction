import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

def run():

    # membuat judul
    st.title('Credit Card Payment Prediction')

    # membuat subheader
    st.subheader('Analisa Dataset Credit Card Default Payment')

    #image
    image = Image.open('cc.jpg')
    st.image(image, caption = 'Are you worthy enough to use our credit card?')

    # deskripsi
    st.write('Page ini dibuat oleh Heru')
    st.write('HCK - 018')
    st.write('Bertujuan untuk melakukan prediksi payment credit card')

    # # bold
    st.write('## Exploratory Data Analysis (EDA)')

    # buat garis
    st.markdown('---')

    # show dataframe
    df1 = pd.read_csv('P1G5_Set_1_Heru.csv')
    st.dataframe(df1)

    # buat garis
    st.markdown('---')

    # EDA 1
    st.write('#### Average Credit Limit by Gender')
    # Average credit limit by gender
    avgCreditGender = df1.groupby('sex')['limit_balance'].mean().sort_values(ascending=False).reset_index()
    # urutan
    urutanGender = {1: 'male', 2: 'female'}
    # apply urutan
    avgCreditGender['sex'] = avgCreditGender['sex'].map(urutanGender)
    fig = px.pie(avgCreditGender, names="sex", 
                values="limit_balance", 
                title="Credit limit by Gender",
                hover_data=["limit_balance"], 
                )
    st.plotly_chart(fig)
    # Deskripsi
    st.write('- Female memiliki rata rata limit balance tertinggi dengan jumlah 166237.513873')
    st.write('- Male memiliki rata rata limit balance terendah dengan jumlah 158925.19346')

    # buat garis
    st.markdown('---')

    # EDA 2
    st.write('#### Average Credit Limit by Education Level')
    avgCreditEdu = df1.groupby('education_level')['limit_balance'].mean().sort_values(ascending=False).reset_index()
    # urutan
    urutanEdu = {0: 'others', 1: 'graduate school', 2: 'university', 3: 'high school', 4: 'others 1', 5: 'others 2', 6: 'others 3'}
    # apply urutan
    avgCreditEdu['education_level'] = avgCreditEdu['education_level'].map(urutanEdu)
    fig2 = px.bar(avgCreditEdu, x='education_level', y='limit_balance', orientation='v',text_auto='.2s')
    st.plotly_chart(fig2)
    # Deskripsi
    st.write('- others 1 dan graduate school memiliki nilai rata rata limit balance paling tinggi diantara education level yang lain.')
    st.write('- rata rata nilai limit balance untuk lulusan highschool memiliki nilai paling rendah diantara graduate school dan university.')

    # buat garis
    st.markdown('---')

    # EDA 3
    st.write('#### Total Marital Status')
    totalMarital = df1['marital_status'].value_counts().reset_index()
    # urutan
    urutanMarital = {0: 'others', 1: 'married', 2: 'single', 3: 'divorce'}
    # apply urutan
    totalMarital['marital_status'] = totalMarital['marital_status'].map(urutanMarital)
    fig3 = px.bar(totalMarital, x='marital_status', y='count', orientation='v',text_auto='.2s')
    st.plotly_chart(fig3)
    # Deskripsi
    st.write('- Terdapat sebesar 1.594 customer yang berstatus single.')
    st.write('- Terdapat sebesar 1.332 customer yang berstatus married.')
    st.write('- Terdapat sebesar 35 customer yang berstatus divorced.')
    st.write('- Terdapat sebesar 4 customer yang berstatus tidak diketahui.')

    # buat garis
    st.markdown('---')

    # EDA 4 
    st.write('#### Average Education Level by Age')
    # Median age by education level
    avgAgeEdu = df1.groupby('education_level')['age'].median().sort_values(ascending=False).reset_index()
    # urutan
    urutanEdu = {0: 'others', 1: 'graduate school', 2: 'university', 3: 'high school', 4: 'others 1', 5: 'others 2', 6: 'others 3'}
    # apply urutan
    avgAgeEdu['education_level'] = avgAgeEdu['education_level'].map(urutanEdu)
    fig4 = px.bar(avgAgeEdu, x='education_level', y='age', orientation='v',text_auto='.2s')
    st.plotly_chart(fig4)
    # Deskripsi
    st.write('- Education level berstatus high school memiliki rata rata berumur 41 tahun.')
    st.write('- Education level berstatus university memiliki rata rata berumur 33 tahun.')
    st.write('- Education level berstatus graduate school memiliki rata rata berumur 32 tahun.')
    st.write('- untuk education level lainnya memiliki rata rata umur yang beragam.')

    # buat garis
    st.markdown('---')

    # EDA 5 
    st.write('#### Total Payment Amounts by Education level')
    totalPaymentEdu = df1.groupby('education_level')[['pay_amt_1', 'pay_amt_2', 'pay_amt_3', 'pay_amt_4', 'pay_amt_5', 'pay_amt_6']].sum().reset_index()
    totalPaymentEdu['Total Payment'] = totalPaymentEdu[['pay_amt_1', 'pay_amt_2', 'pay_amt_3', 'pay_amt_4', 'pay_amt_5', 'pay_amt_6']].sum(axis=1)
    # Melt the dataframe for easier plotting
    totalPaymentEdu2 = totalPaymentEdu.melt(id_vars='education_level', value_vars=['pay_amt_1', 'pay_amt_2', 'pay_amt_3', 'pay_amt_4', 'pay_amt_5', 'pay_amt_6'],
                                                var_name='Payment Month', value_name='Total payment')
    # apply urutan
    totalPaymentEdu2['education_level'] = totalPaymentEdu2['education_level'].map(urutanEdu)
    # Create the bar chart
    fig5 = px.bar(totalPaymentEdu2, x='education_level', y='Total payment', color='Payment Month',
                title='Total Payment Amounts by Education Level', labels={'education_level': 'Education Level', 'Total Payment': 'Total Payment Amount'})
    st.plotly_chart(fig5)
    # Deskripsi
    st.write('- Education Level 1 ( graduate school ) cenderung memiliki total payment yang lebih tinggi dibandingkan lainnya.')
    st.write('- Education level 3 ( high school ) memiliki total payment yang paling rendah diantara lulusan graduate school dan university.')

    # buat garis
    st.markdown('---')

    # EDA 6 
    st.write('#### Totals of Default Payment by Education Level')
    # Count of defaults by education level
    defaultEdu = df1.groupby('education_level')['default_payment_next_month'].sum().reset_index()
    # urutan
    defaultEdu['education_level'] = defaultEdu['education_level'].map(urutanEdu)
    fig6 = px.bar(defaultEdu, x='education_level', y='default_payment_next_month', orientation='v',text_auto='.2s')
    st.plotly_chart(fig6)
    # Deskripsi
    st.write('- berdasarkan dataset, lulusan university memiliki data gagal bayar yang paling besar diantara lainnya.')
    st.write('- untuk lulusan high school dan graduated school memiliki nilai data gagal bayar yang tidak jauh beda.')

    # buat garis
    st.markdown('---')

    # EDA 7
    st.write('#### Totals of Default Payment by Marital Status')
    # Count of defaults by marital status
    defaultMarital = df1.groupby('marital_status')['default_payment_next_month'].sum().reset_index()
    # apply urutan
    defaultMarital['marital_status'] = defaultMarital['marital_status'].map(urutanMarital)
    fig7 = px.bar(defaultMarital, x='marital_status', y='default_payment_next_month', orientation='v',text_auto='.2s')
    st.plotly_chart(fig7)
    # Deskripsi
    st.write('- Berdasarkan dataset, customer berstatus single memiliki nilai gagal bayar yang tinggi diikuti dengan customer yang berstatus married.')

if __name__ == '__main__':
    run()
    