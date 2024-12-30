import streamlit as st
import pickle
import pandas as pd

page_bg_img = '''
<style>
body {
background-image: url("https://raw.githubusercontent.com/Hariprasath1911/Medical-Prediction/main/12.png");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Load models
@st.cache_resource
def load_model(model_path):
    with open(model_path, 'rb') as file:
        return pickle.load(file)

# Load models
Kidney_model=load_model("https://github.com/Hariprasath1911/Medical-Prediction/blob/main/kidney.pkl")
liver_model = load_model('https://github.com/Hariprasath1911/Medical-Prediction/blob/main/model_liver.pkl')
parkinson_model = load_model('https://github.com/Hariprasath1911/Medical-Prediction/blob/main/parkinson.pkl')

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
    
    # User input
    age = st.number_input('Age', min_value=12)
    gender_select = st.selectbox('Gender', ['Male', 'Female'])
    gender_map={'Male':1, 'Female':0}
    gender=gender_map.get(gender_select)
    bilirubin = st.number_input('Total Bilirubin',min_value=0)
    Direct_Bilirubin=st.number_input('Direct_Bilirubin',min_value=0)
    alkaline_phosphotase = st.number_input('Alkaline Phosphotase',min_value=0)
    Alamine_Aminotransferase= st.number_input('Alamine_Aminotransferase',min_value=0)
    Aspartate_Aminotransferase=st.number_input('Aspartate_Aminotransferase',min_value=0)
    Total_Protiens=st.number_input('Total_Protiens',min_value=0)
    albumin = st.number_input('Albumin',min_value=0)
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
    
    # User input
    Fo = st.number_input('Enter average fundamental frequency of the voice (Fo-Hz)')
    Fhi = st.number_input('Enter maximum fundamental frequency of the voice')
    Flo = st.number_input('Enter minimum fundamental frequency of the voice')
    Jitter= st.number_input('Entter measure of variation in pitch (percentage)')
    Jitter_Abs=st.number_input('Enter absolute measure of pitch variation')
    RAP=st.number_input('Enter relative average perturbation (measure of voice signal frequency variation)')
    PPQ=st.number_input('Enter five-point period perturbation quotient')
    Jitter_DDP=st.number_input('Enter average absolute difference of differences between cycles')
    MDVP_Shimmer=st.number_input('Enter measure of amplitude variation')
    MDVP_Shimmer_dB=st.number_input('Enter amplitude variation measured in decibels')
    Shimmer_APQ3=st.number_input('Enter three-point amplitude perturbation quotient')
    Shimmer_APQ5=st.number_input('Enter five-point amplitude perturbation quotient')
    APQ=st.number_input('Enter amplitude perturbation quotient')
    Shimmer_DDA=st.number_input('Enter average absolute differences between consecutive amplitudes')
    NHR=st.number_input('Enter noise-to-harmonics ratio (an indicator of noise in the voice)')
    HNR=st.number_input('Enter harmonics-to-noise ratio (an indicator of tonal clarity in the voice)')
    RPDE=st.number_input('ENter recurrence period density entropy (nonlinear dynamical complexity measure)')
    DFA=st.number_input('Enter detrended fluctuation analysis (signal fractal scaling exponent)')
    spread1=st.number_input('Enter nonlinear measure of voice signal frequency')
    spread2=st.number_input('Enter nonlinear measure of voice signal amplitude')
    D2=st.number_input('Enter dynamical complexity measure')
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
