import streamlit as st

st.header('Paycheck Calculator')
calc, config = st.columns([.7,.3])
with config: 
    st.write('How much do you want to save for each? ') 
    with st.container():
        tax_rate=st.text_input("Taxes", value=0, placeholder="10%")
        trate = float(tax_rate) / 100
        rent_rate=st.text_input("Rent", value=0, placeholder="5%")
        rrate = float(rent_rate) / 100
        car_rate=st.text_input("Car ", value=0, placeholder="1%")
        crate = float(car_rate) / 100

with calc:
    st.write('How much is your paycheck? ')
    paycheck = st.text_input('PAYCHECK', value=0, label_visibility='hidden', placeholder='1200.13')
   
    tax = float(paycheck) * trate
    rent = float(paycheck) * rrate
    car = float(paycheck) * crate

   
    with st.container(border=True):
        st.text_input("Taxes", value='${:,.2f}'.format(tax) )
        st.text_input("Rent", value='${:,.2f}'.format(rent))
        st.text_input("Car", value='${:,.2f}'.format(car))
    totalToSave = tax + rent + car

    st.write("Total to Save: " + '${:,.2f}'.format(totalToSave))
    net = float(paycheck) - float(totalToSave)
    st.write("Net to Spend: " + '${:,.2f}'.format(net))