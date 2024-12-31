import streamlit as st
import pickle
import pandas as pd

page_bg_img = '''
<style>
body {
background-image: url("12.png");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
@st.cache_resource

# Load models
def load_model(model_path):
    with open(model_path, 'rb') as file:
        return pickle.load(file)

# Load models
Kidney_model = load_model("kidney.pkl")
liver_model = load_model("model_liver.pkl")
parkinson_model = load_model("parkinson.pkl")

# App title
st.title('Medical Condition Prediction App')
st.sidebar.write('Select parameters and click Predict to see the results.')

# Sidebar for condition selection
condition = st.sidebar.selectbox('Select Medical Condition', ['Kidney Disease','Liver Disease', 'Parkinson Disease'])

if condition == 'Kidney Disease':
    st.header('Kidney Disease Prediction')
    
    # User input
    age = st.number_input('Enter your age', min_value=12)
    bp = st.number_input('Enter blood pressure (in mmHg)',min_value=0)
    sg = st.number_input('Enter specific gravity of urine',min_value=0)
    al= st.number_input('Enter albumin levels in urine',min_value=0)
    su=st.number_input('Enter sugar levels in urine',min_value=0)
    rbc_select=st.selectbox('Select Red blood cells-status',['Normal','Abnormal'])
    rbc_map={'Normal':1,'Abnormal':0}
    rbc=rbc_map.get(rbc_select)
    pc_select=st.selectbox('Select pus cell count-status',['Normal','Abnormal'])
    pc_map={'Normal':1,'Abnormal':0}
    pc=pc_map.get(pc_select)
    pcc_select=st.selectbox('Select pus cell clumps-status',['Not present','Present'])
    pcc_map={'Present':1,'Not present':0}
    pcc=pcc_map.get(pcc_select)
    ba_select=st.selectbox('Select bacteria presence-status',['Not present','Present'])
    ba_map={'Present':1,'Not present':0}
    ba=ba_map.get(ba_select)
    bgr= st.number_input('Enter blood glucose random levels',min_value=0)
    bu= st.number_input('Enter blood urea levels',min_value=0)
    sc= st.number_input('Enter serum creatinine levels',min_value=0)
    sod= st.number_input('Enter sodium levels',min_value=0)
    pot= st.number_input('Enter potassium levels',min_value=0)
    hemo= st.number_input('Enter hemoglobin levels',min_value=0)
    pcv= st.number_input('Enter packed cell volume',min_value=0)
    wc= st.number_input('Enter white blood cell count',min_value=0)
    rc= st.number_input('Enter Red blood cell count.',min_value=0)
    htn_select=st.selectbox('Select hypertension-status',['No','Yes'])
    htn_map={'Yes':1,'No':0}
    htn=htn_map.get(htn_select)
    dm_select=st.selectbox('Select diabetes mellitus-status',['No','Yes'])
    dm_map={'Yes':1,'No':0}
    dm=dm_map.get(dm_select)
    cad_select=st.selectbox('Select coronary artery disease-status',['No','Yes'])
    cad_map={'Yes':1,'No':0}
    cad=cad_map.get(cad_select)
    appet_select=st.selectbox('Select appetite-status',['Good','Poor'])
    appet_map={'Poor':1,'Good':0}
    appet=appet_map.get(appet_select)
    pe_select=st.selectbox('Select pedal edema-status',['No','Yes'])
    pe_map={'Yes':1,'No':0}
    pe=pe_map.get(pe_select)
    ane_select=st.selectbox('Select anemia-status',['No','Yes'])
    ane_map={'Yes':1,'No':0}
    ane=ane_map.get(ane_select)

    
    if st.button('Predict'):
        data={
            "age":age,"bp":bp,"sg":sg,"al":al,"su":su,"rbc":rbc,"pc":pc,"pcc":pcc,"ba":ba,"bgr":bgr,"bu":bu,"sc":sc,
            "sod":sod,"pot":pot,"hemo":hemo,"pcv":pcv,"wc":wc,"rc":rc,"htn":htn,"dm":dm,"cad":cad,"appet":appet,"pe":pe,"ane":ane
            }
        input_data = pd.DataFrame([data])
        prediction = Kidney_model.predict(input_data)
        st.write('Prediction:', 'Positive-Chronic Kidney Disease' if prediction[0] == 1 else 'Negative-Chronic Kidney Disease')

elif condition == 'Liver Disease':
    st.header('Liver Disease Prediction')
    col1,col2,col3,col4 = st.columns(4)
    col5,col6,col7 = st.columns(3)
    col8,col9,col10 = st.columns(3)
    
    # User input
    with col1:
        age = st.number_input('Age', min_value=12)
    with col2:
        gender_select = st.selectbox('Gender', ['Male', 'Female'])
        gender_map={'Male':1, 'Female':0}
        gender=gender_map.get(gender_select)
    with col3:
        bilirubin = st.number_input('Total Bilirubin',min_value=0)
    with col4:
        Direct_Bilirubin=st.number_input('Direct_Bilirubin',min_value=0)
    with col5:
        alkaline_phosphotase = st.number_input('Alkaline Phosphotase',min_value=0)
    with col6:
        Alamine_Aminotransferase= st.number_input('Alamine_Aminotransferase',min_value=0)
    with col7:
        Aspartate_Aminotransferase=st.number_input('Aspartate_Aminotransferase',min_value=0)
    with col8:
        Total_Protiens=st.number_input('Total_Protiens',min_value=0)
    with col9:
        albumin = st.number_input('Albumin',min_value=0)
    with col10:
        Albumin_and_Globulin_Ratio=st.number_input('Albumin_and_Globulin_Ratio',min_value=0)
    
    if st.button('Predict'):
        data={
            "Age":age,"Gender":gender,"Total_Bilirubin":bilirubin,"Direct_Bilirubin":Direct_Bilirubin,
            "Alkaline_Phosphotase":alkaline_phosphotase,"Alamine_Aminotransferase":Alamine_Aminotransferase,
            "Aspartate_Aminotransferase":Aspartate_Aminotransferase,"Total_Protiens":Total_Protiens,
            "Albumin":albumin,"Albumin_and_Globulin_Ratio":Albumin_and_Globulin_Ratio
            }
        input_data = pd.DataFrame([data])
        prediction = liver_model.predict(input_data)
        st.write('Prediction:', 'Positive' if prediction[0] == 1 else 'Negative')

elif condition == 'Parkinson Disease':
    st.header('Parkinson Disease Prediction')
    c1,c2,c3=st.columns(3)
    c4,c5,c6=st.columns(3)
    c7,c8,c9=st.columns(3)
    c10,c11,c12=st.columns(3)
    c13,c14,c15=st.columns(3)
    c16,c17=st.columns(2)
    c18,c19,c20=st.columns(3)
    c21,c22=st.columns(2)
    
    
    # User input
    with c1:
        Fo = st.number_input('Enter average fundamental frequency of the voice (Fo-Hz)')
    with c2:
        Fhi = st.number_input('Enter maximum fundamental frequency of the voice')
    with c3:
        Flo = st.number_input('Enter minimum fundamental frequency of the voice')
    with c4:
        Jitter= st.number_input('Entter measure of variation in pitch (percentage)')
    with c5:
        Jitter_Abs=st.number_input('Enter absolute measure of pitch variation')
    with c6:
        RAP=st.number_input('Enter relative average perturbation (measure of voice signal frequency variation)')
    with c7:
        PPQ=st.number_input('Enter five-point period perturbation quotient')
    with c8:
        Jitter_DDP=st.number_input('Enter average absolute difference of differences between cycles')
    with c9:
        MDVP_Shimmer=st.number_input('Enter measure of amplitude variation')
    with c10:
        MDVP_Shimmer_dB=st.number_input('Enter amplitude variation measured in decibels')
    with c11:
        Shimmer_APQ3=st.number_input('Enter three-point amplitude perturbation quotient')
    with c12:
        Shimmer_APQ5=st.number_input('Enter five-point amplitude perturbation quotient')
    with c13:
        APQ=st.number_input('Enter amplitude perturbation quotient')
    with c14:
        Shimmer_DDA=st.number_input('Enter average absolute differences between consecutive amplitudes')
    with c15:
        NHR=st.number_input('Enter noise-to-harmonics ratio (an indicator of noise in the voice)')
    with c16:
        HNR=st.number_input('Enter harmonics-to-noise ratio (an indicator of tonal clarity in the voice)')
    with c17:
        RPDE=st.number_input('ENter recurrence period density entropy (nonlinear dynamical complexity measure)')
    with c18:
        DFA=st.number_input('Enter detrended fluctuation analysis (signal fractal scaling exponent)')
    with c19:
        spread1=st.number_input('Enter nonlinear measure of voice signal frequency')
    with c20:
        spread2=st.number_input('Enter nonlinear measure of voice signal amplitude')
    with c21:
        D2=st.number_input('Enter dynamical complexity measure')
    with c22:
        PPE=st.number_input('Enter pitch period entropy (variation in pitch)')      
    
    if st.button('Predict'):
        #data={
            #"MDVP:Fo(Hz)":MDVP:Fo(Hz),"MDVP:Fhi(Hz)":MDVP:Fhi(Hz),"MDVP:Flo(Hz)":MDVP:Flo(Hz),"MDVP:Jitter(%)":MDVP:Jitter(%),
            #"MDVP:Jitter(Abs)":MDVP:Jitter(Abs),"MDVP:RAP":MDVP:RAP,"MDVP:PPQ":MDVP:PPQ,"Jitter:DDP":Jitter:DDP,"MDVP:Shimmer":MDVP:Shimmer,
            #"MDVP:Shimmer(dB)":MDVP:Shimmer(dB),"Shimmer:APQ3":Shimmer:APQ3,"Shimmer:APQ5":Shimmer:APQ5,"MDVP:APQ":MDVP:APQ,
            #"Shimmer:DDA":Shimmer:DDA,"NHR":NHR,"HNR":HNR,"RPDE":RPDE,"DFA":DFA,"spread1":spread1,"spread2":spread2,"D2":D2,"PPE":PPE
        #}
        #input_data= pd.DataFrame([data])
        input_data = pd.DataFrame([[Fo, Fhi,Flo,Jitter,Jitter_Abs,RAP,PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]],
                                  columns=['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)','MDVP:Flo(Hz)','MDVP:Jitter(%)','MDVP:Jitter(Abs)','MDVP:RAP','MDVP:PPQ','Jitter:DDP','MDVP:Shimmer','MDVP:Shimmer(dB)','Shimmer:APQ3','Shimmer:APQ5','MDVP:APQ','Shimmer:DDA','NHR','HNR','RPDE','DFA','spread1','spread2','D2','PPE'])
        prediction = parkinson_model.predict(input_data)
        st.write('Prediction:', 'Positive' if prediction[0] == 1 else 'Negative')


# Run with: streamlit run app.py
