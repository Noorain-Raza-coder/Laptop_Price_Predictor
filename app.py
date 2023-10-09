import streamlit as st
import pickle
import pandas as pd
import numpy as np



model = pickle.load(open('model.pkl','rb'))
data = pd.read_pickle('df.pkl')
df = pd.DataFrame(data)

st.header(':orange[Laptop Price Predictor]')
st.divider()
# st.title("Laptop Price Predictor")
st.write('Creator : :orange[Noorain Raza] :sunglasses:')


Company = st.selectbox('Company',(df['Company'].unique()))
LaptopType = st.selectbox('Laptop Type',(df['LaptopType'].unique()))
Inches = st.number_input('Size (in inches)')
Processor = st.selectbox('Processor',(df['Processor'].unique()))
Ram = st.selectbox('RAM (in GB)',(df['Ram'].unique()))
Gpu = st.selectbox('Gpu',(df['Gpu'].unique()))
OpSys = st.selectbox('Operating System (OS)',(df['OpSys'].unique()))
Weight = st.number_input('Weight (in Kg)')
SSD = st.selectbox('SSD (in GB)',([0,128,256,512,1024]))
HDD = st.selectbox('HDD (in GB)',([0,512,1024,2048]))
Touchscreen = st.selectbox('Taouchscreen',(['Yes','No']))
IPS_Panel = st.selectbox('IPS Pannel',(['Yes','No']))
resolution = st.selectbox('Screen Resolution',(['1388 x 768','1920 x 1080','2560 x 1440','3840 x 2160','5120 x 2880']))

if st.button("Predict", type="primary",use_container_width= True):
    # st.write('Laptop price is: ',str(prediction))

## function to convert yes or no to 0 or 1
    def cat_convert(str):
        if str == 'Yes':
            return 1
        else:
            return 0


    ## memory column
    Memory = SSD + HDD

    ## For hybrid column
    if SSD != 0:
        SSD_cat = 1
    else:
        SSD_cat = 0

    if HDD != 0:
        HDD_cat = 1
    else:
        HDD_cat = 0

    Hybrid = (SSD_cat and HDD_cat)

    Touchscreen =  cat_convert(Touchscreen)
    IPS_Panel =  cat_convert(IPS_Panel)

    res = resolution.split('x')
    X_res = int(res[0])
    Y_res = int(res[1])
    ppi = (((X_res**2) + (Y_res**2))**0.5) / Inches

    input_data = np.array([Company,LaptopType,Inches,Processor,Ram,Gpu,OpSys,Weight,SSD_cat,HDD_cat,Hybrid,Memory,Touchscreen,IPS_Panel,ppi])
    data = input_data.reshape(1,15)
    pred = model.predict(data)
    prediction = np.exp(pred)
    st.title(':orange[Laptop price is:   ]' + str(round(prediction[0])))
    st.balloons()


