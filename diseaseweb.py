
import streamlit as st
import pickle as pk


def heart():
    #loading the model
    model_heart = pk.load(open('Heart_pre.pkl', 'rb'))
    st.title("HEART DISEASE PREDICTION")
    st.image('heart1.jfif')
    #-------
    col1,col2=st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)
    col7, col8 = st.columns(2)
    col9, col10 = st.columns(2)
    col11, col12 = st.columns(2)
    col13, col14 = st.columns(2)
    #-------
    #name
    with col1:
       name=st.text_input("ENTER YOUR NAME",key=1)

    #age
    with col2:
        age=st.number_input("Age",min_value=18,step=1)

    #sex
    with col3:
       s=("Male","Female")
       op1=list(range(len(s)))
       sex=st.selectbox("Gender",op1,format_func=lambda x:s[x])

    #chest pain
    with col4:
       c=("NO","Less","Medium","high")
       op2=list(range(len(c)))
       chest=st.selectbox("Chest Pain",op2,format_func=lambda x:c[x])


    #resting blood pressure
    with col5:
      b=st.number_input("Resting Blood Pressure",min_value=90)

    #serum cholestrol level
    with col6:
      se=st.number_input("Serum Cholestrol Level mg/dl",min_value=120)

    # fbs
    with col7:
      f=("<=120 mg/dl",">120 mg/dl")
      op4=list(range(len(f)))
      fbs=st.selectbox("Fasting Blood Sugar",op4,format_func=lambda x:f[x])

    #resting electro cardiographic res
    with col8:
      rest=st.number_input("Resting Electrocardiograph",min_value=0,max_value=2)

    #maximum heat rate achived
    with col9:
       h=st.number_input("Maximum Heart Rate Achieved",min_value=65,step=1)

    #exag
    with col10:
      e=("No","Yes")
      op5=list(range(len(e)))
      exer=st.selectbox("Exercise Induced Agina",op5,format_func=lambda x:e[x])

    #old peak
    with col11:
       old=st.number_input("ST segment",value=0)

    #slope
    with col12:
       slope=st.number_input("Slope of ST segment",min_value=0,max_value=2,step=1)

    #ca
    with col13:
      ves=st.number_input("Number of major vessels",min_value=0,max_value=4,step=1)

    #thal
    with col14:
      t=("normal","fixed defect","reversable defect","other defect")
      op6=list(range(len(t)))
      thal=st.selectbox("Defect",op6,format_func=lambda x:t[x])

    if st.button("SUBMIT"):
        lis = [[age, sex, chest, b, se, fbs, rest, h, exer, old, slope, ves, thal]]
        prediction = model_heart.predict(lis)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans==0:
            st.success("Hello"+name+" || "
                   "You are Alright!!!")
        else:
            st.error("Hello"+name+" || "
                   "Don't painc You get Heart Disease"
                    "Follow the Doctor's Prescription")


def parkinsons():

    model_parkinson=pk.load(open('Parkinsons.pkl','rb'))
    st.title('PARKINSON\'s PREDICTION')
    st.image('parkinson.jfif')
    # -------
    col1, col2,col3 = st.columns(3)
    col4, col5,col6 = st.columns(3)
    col7, col8,col9 = st.columns(3)
    col10, col11,col12 = st.columns(3)
    col13, col14,col15 = st.columns(3)
    col16, col17,col18 = st.columns(3)
    col19, col20,col21 = st.columns(3)
    col22,col23=st.columns(2)
    # -------
    #name
    with col1:
        name = st.text_input("ENTER YOUR NAME",key=2)

    #MDVP:Fo(Hz) - Average vocal fundamental frequency
    with col2:
        avg_vocal = st.number_input("AVG VOCAL FREQ", min_value=85.0, max_value=265.0,step=0.001,format="%.3f")

    #MDVP:Fhi(Hz) - Maximum vocal fundamental frequency
    with col3:
        max_vocal = st.number_input("MAX VOCAL FREQ", min_value=98.0, max_value=595.0,step=0.001,format="%.3f")

    #MDVP:Flo(Hz) - Minimum vocal fundamental frequency
    with col4:
        min_vocal = st.number_input("MIN VOCAL FREQ", min_value=65.0, max_value=240.0,step=0.001,format="%.3f")

    #MDVP: Jitter( %)
    with col5:
        jitter1 = st.number_input("JITTER(%) VOCAL FREQ", min_value=0.0, max_value=2.0,step=0.00001,format="%.5f")

    #MDVP:Jitter(Abs)
    with col6:
        jitter2=st.number_input("JITTER(Abs) VOCAL FREQ", min_value=0.0, max_value=1.0,step=0.00001,format="%.5f")

    #MDVP:RAP
    with col7:
        rap=st.number_input("RAP", min_value=0.0, max_value=1.0,step=0.00001,format="%.5f")

    #MDVP:PPQ
    with col8:
        ppq=st.number_input("PPQ", min_value=0.0, max_value=1.0,step=0.00001,format="%.5f")

    #Jitter:DDP
    with col9:
        ddp=st.number_input("DDP", min_value=0.0, max_value=1.0,step=0.00001,format="%.5f")

    #MDVP:Shimmer
    with col10:
        shimmer = st.number_input("SHIMMER", min_value=0.0, max_value=1.0,step=0.00001,format="%.5f")

    #MDVP:Shimmer(dB)
    with col11:
        shimmer_db = st.number_input("SHIMMER(db)", min_value=0.0, max_value=2.0,step=0.0001,format="%.4f")

    #Shimmer:APQ3
    with col12:
        shimmer_apq3 = st.number_input("SHIMMER(APQ3)", min_value=0.0, max_value=1.0,step=.00001,format="%.5f")

    #Shimmer:APQ5
    with col13:
        shimmer_apq5 = st.number_input("SHIMMER(APQ5)", min_value=0.0, max_value=1.0,step=.0001,format="%.4f")

    #MDVP:APQ
    with col14:
        mdvp_apq = st.number_input("MDVP(APQ)", min_value=0.0, max_value=2.0,step=.00001,format="%.5f")

    #Shimmer: DDA
    with col15:
        shimmer_dda = st.number_input("SHIMMER(DDA)", min_value=0.0, max_value=2.0,step=.00001,format="%.5f")

    #NHR,HNR - Two measures of ratio of noise to tonal components in the voice
    with col16:
        nhr = st.number_input("NHR", min_value=0.0, max_value=1.0,step=.00001,format="%.5f")
    with col17:
        hnr = st.number_input("HNR", min_value=5.0, max_value=35.0,step=0.01)

    #RPDE,D2 - Two nonlinear dynamical complexity measures
    with col18:
        rpde = st.number_input("RPDE", min_value=0.0, max_value=1.0,step=.00001,format="%.5f")
    with col19:
        d2 = st.number_input("D2", min_value=1.0, max_value=5.0,step=0.000001,format="%.6f")

    #DFA - Signal fractal scaling exponent
    with col20:
        dfa = st.number_input("DFA", min_value=0.0, max_value=1.0,step=.000001,format="%.6f")

    #spread1,spread2,PPE - Three nonlinear measures of fundamental frequency variation
    with col21:
        spread1 = st.number_input("SPREAD1", min_value=-7.0, max_value=-2.0,step=0.000001,format="%.6f")
    with col22:
        spread2 = st.number_input("SPREAD2", min_value=0.0, max_value=1.0,step=.000001,format="%.6f")
    with col23:
        ppe = st.number_input("PPE", min_value=0.0, max_value=1.0,step=0.000001,format="%.6f")

    if (st.button("SUBMIT")):
        lis = [[avg_vocal, max_vocal, min_vocal, jitter1, jitter2, rap, ppq, ddp,shimmer,shimmer_db,shimmer_apq3,shimmer_apq5,mdvp_apq,shimmer_dda,nhr,hnr,rpde,dfa,spread1,spread2,d2,ppe]]
        prediction = model_parkinson.predict(lis)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.success("Name: " + name)
            st.success("No Parkinson !!!")
        else:
            st.error("Name: " + name)
            st.error("You have Parkinson !!!")
            st.error("No Worry!!! Follow the Doctor's Prescription")

def diabetes():
        diabetes_model = pk.load(open('Diabetes_pre.pkl', 'rb'))
        st.title("DIABETES PREDICTION")
        st.image('diab.jfif')

        # -------
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)
        col5, col6 = st.columns(2)
        col7, col8 = st.columns(2)
        col9, col10 = st.columns(2)
        #----

        # name
        with col1:
          name = st.text_input("Enter your name",key=3)

        # Id number
        with col2:
          id = st.text_input("Patient ID Number")

        # Pregnencies
        with col3:
          pr = st.number_input("Enter Pregnencies", value=0)

        # Glucose
        with col4:
          gl = st.number_input("Enter Glucose Level")

        # bp
        with col5:
          bp = st.number_input("Enter Blood Pressure")

        # skinthickness
        with col6:
          sk = st.number_input("Enter Skin Thickness")

        # insulin
        with col7:
          ins = st.number_input("Enter Insulin Level")

        # bmi
        with col8:
          Bmi = st.number_input("Enter BMI")

        # dpf
        with col9:
          dpf = st.number_input("Enter Diabetes Pedigree Function")

        # Age
        with col10:
          age = st.number_input("Enter Your Age")
        if (st.button("SUBMIT")):
            lis = [[pr, gl, bp, sk, ins, Bmi, dpf, age]]
            prediction = diabetes_model.predict(lis)
            lc = [str(i) for i in prediction]
            ans = int("".join(lc))
            if ans == 0:
                st.success("Name: " + name)
                st.success("ID: " + id)
                st.success("No Diabetes !!!")
            else:
                st.error("Name: " + name)
                st.error("ID: " + id)
                st.error("You have Diabetes !!!")
                st.error("No Worry!!! Follow the Doctor's Prescription")


option=st.sidebar.radio('DISEASE PREDICTION SYSTEM',['Heart disease','Parkinsons disease','Diabetes disease'])
if option=='Heart disease':
    heart()
if option=='Parkinsons disease':
    parkinsons()
if option=='Diabetes disease':
    diabetes()
