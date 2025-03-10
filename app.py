import streamlit as st
import pickle
import pandas as pd
import base64

@st.cache_resource
# Load models
def load_model(model_path):
    with open(model_path, 'rb') as file:
        return pickle.load(file)
def set_background_image_local(image_path):
    with open(image_path, "rb") as file:
        data = file.read()
    base64_image = base64.b64encode(data).decode("utf-8")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{base64_image}");
            background-size: cover;
            background-position: fit;
            background-repeat: repeat;
            background-attachment: fixed;
        }}     
        </style>
        """,
        unsafe_allow_html=True
    )

set_background_image_local(r"12.png")

# Load models
Kidney_model = load_model("kidney.pkl")
liver_model = load_model("model_liver.pkl")
parkinson_model = load_model("parkinson.pkl")

# App title
st.sidebar.write('☰ Navigation')

# Sidebar for condition selection
condition = st.sidebar.selectbox('Select Tab 🔍', ['Home','Kidney Disease','Liver Disease', 'Parkinson Disease'])
if condition == 'Home':
    st.title("Health Prediction Application")
    st.subheader("Empowering Early Detection of Health Conditions")

# Introduction
    st.write("""
    Welcome to the **Health Prediction Application**! This tool is designed to provide insights and early detection of health conditions using machine learning models. 
    Simply input relevant medical data or upload patient records, and our models will predict the likelihood of specific health issues.
    """)

# Application features
    st.markdown("### Features:")
    st.write("""
    - **Liver Disease Prediction**: Analyze patient data to determine the likelihood of liver-related health issues.
    - **Kidney Disease Prediction**: Use medical test results to assess the risk of chronic kidney disease.
    - **Parkinson’s Disease Prediction**: Evaluate vocal and motor features to predict the presence of Parkinson’s disease.

    """)

# Navigation instructions
    st.markdown("### How to Use:")
    st.write("""
    1. Navigate to the specific health condition page using the tabs on the sidebar.
    2. Input the required medical data or upload a dataset.
    3. View the prediction results instantly, along with additional insights and visualizations.
    """)

# Add a call-to-action
    st.markdown("""
    #### Ready to get started? 
    Select a prediction model from the sidebar to see the application in action!
    """)

# Footer or credits
    st.info("Note: This application is intended for informational purposes only and should not be used as a substitute for professional medical advice.")


if condition == 'Kidney Disease':
    st.header('Kidney Disease Prediction')
    set_background_image_local(r"kid.jpg")
    tab1, tab2 = st.tabs(["Home", "Predict"])
    with tab1:
        st.markdown("""
        **Kidney Disease**
        , also known as renal disease, occurs when the kidneys lose their ability to filter waste
        and excess fluids from the blood. This condition can lead to chronic kidney disease (CKD), which may
        progress over time to kidney failure. Common causes include diabetes, high blood pressure, and
        infections. Early detection through tests like blood pressure, creatinine levels, and urine analysis is
        crucial for effective management.
        """)
    with tab2:
        a1,a2,a3=st.columns(3)
        a4,a5,a6=st.columns(3)
        a7,a8,a9=st.columns(3)
        a10,a11,a12=st.columns(3)
        a13,a14,a15=st.columns(3)
        a16,a17,a18=st.columns(3)
        a19,a20,a21=st.columns(3)
        a22,a23,a24=st.columns(3)
        # User input
        with a1:
            age = st.number_input('Enter your age', min_value=12)
        with a2:
            bp = st.number_input('Enter blood pressure (in mmHg)',min_value=0)
        with a3:
            sg = st.number_input('Enter specific gravity of urine',min_value=0)
        with a4:
            al= st.number_input('Enter albumin levels in urine',min_value=0)
        with a5:
            su=st.number_input('Enter sugar levels in urine',min_value=0)
        with a6:
            rbc_select=st.selectbox('Select Red blood cells-status',['Normal','Abnormal'])
            rbc_map={'Normal':1,'Abnormal':0}
            rbc=rbc_map.get(rbc_select)
        with a7:
            pc_select=st.selectbox('Select pus cell count-status',['Normal','Abnormal'])
            pc_map={'Normal':1,'Abnormal':0}
            pc=pc_map.get(pc_select)
        with a8:
            pcc_select=st.selectbox('Select pus cell clumps-status',['Not present','Present'])
            pcc_map={'Present':1,'Not present':0}
            pcc=pcc_map.get(pcc_select)
        with a9:
            ba_select=st.selectbox('Select bacteria presence-status',['Not present','Present'])
            ba_map={'Present':1,'Not present':0}
            ba=ba_map.get(ba_select)
        with a10:
            bgr= st.number_input('Enter blood glucose random levels',min_value=0)
        with a11:
            bu= st.number_input('Enter blood urea levels',min_value=0)
        with a12:
            sc= st.number_input('Enter serum creatinine levels',min_value=0)
        with a13:
            sod= st.number_input('Enter sodium levels',min_value=0)
        with a14:
            pot= st.number_input('Enter potassium levels',min_value=0)
        with a15:
            hemo= st.number_input('Enter hemoglobin levels',min_value=0)
        with a16:
            pcv= st.number_input('Enter packed cell volume',min_value=0)
        with a17:
            wc= st.number_input('Enter white blood cell count',min_value=0)
        with a18:
            rc= st.number_input('Enter Red blood cell count.',min_value=0)
        with a19:
            htn_select=st.selectbox('Select hypertension-status',['No','Yes'])
            htn_map={'Yes':1,'No':0}
            htn=htn_map.get(htn_select)
        with a20:
            dm_select=st.selectbox('Select diabetes mellitus-status',['No','Yes'])
            dm_map={'Yes':1,'No':0}
            dm=dm_map.get(dm_select)
        with a21:
            cad_select=st.selectbox('Select coronary artery disease-status',['No','Yes'])
            cad_map={'Yes':1,'No':0}
            cad=cad_map.get(cad_select)
        with a22:
            appet_select=st.selectbox('Select appetite-status',['Good','Poor'])
            appet_map={'Poor':1,'Good':0}
            appet=appet_map.get(appet_select)
        with a23:
            pe_select=st.selectbox('Select pedal edema-status',['No','Yes'])
            pe_map={'Yes':1,'No':0}
            pe=pe_map.get(pe_select)
        with a24:
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
            st.snow()('Prediction:', 'Positive-Chronic Kidney Disease' if prediction[0] == 1 else 'Negative-Chronic Kidney Disease')

elif condition == 'Liver Disease':
    st.header('Liver Disease Prediction')
    set_background_image_local(r"LIVER.jpg")
    tab1,tab2=st.tabs(["Home", "Predict"])
    with tab1:
        st.markdown("""
        **Liver Disease**
        encompasses a range of conditions that affect the liver's ability to function properly,
        including hepatitis, cirrhosis, and fatty liver disease. The liver plays a vital role in detoxification,
        metabolism, and digestion. Symptoms of liver disease include jaundice, fatigue, and abdominal pain.
        Early diagnosis using tests such as bilirubin levels, enzyme measurements, and imaging is essential to
        prevent severe complications.
        """)
    with tab2:
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
    set_background_image_local(r"par.png")
    tab1,tab2=st.tabs(["Home", "Predict"])
    with tab1:
        st.markdown("""
        **Parkinson’s Disease**
        is a progressive neurological disorder that affects movement and coordination. It
        is caused by the degeneration of dopamine-producing neurons in the brain. Symptoms include
        tremors, stiffness, slow movements, and balance issues. Although there is no cure, early diagnosis
        and treatments like medication, physical therapy, and lifestyle adjustments can help manage
        symptoms and improve quality of life.
        """)
    with tab2:
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
            input_data = pd.DataFrame([[Fo, Fhi,Flo,Jitter,Jitter_Abs,RAP,PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]],
                                  columns=['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)','MDVP:Flo(Hz)','MDVP:Jitter(%)','MDVP:Jitter(Abs)','MDVP:RAP','MDVP:PPQ','Jitter:DDP','MDVP:Shimmer','MDVP:Shimmer(dB)','Shimmer:APQ3','Shimmer:APQ5','MDVP:APQ','Shimmer:DDA','NHR','HNR','RPDE','DFA','spread1','spread2','D2','PPE'])
            prediction = parkinson_model.predict(input_data)
            st.write('Prediction:', 'Positive' if prediction[0] == 1 else 'Negative')
