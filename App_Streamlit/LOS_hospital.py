import pandas as pd
import numpy as np
import sklearn
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie


# Loading Datasets
#df1 = pd.read_csv("df_for_streamlit.csv")

df1 = pd.read_csv("App_Streamlit/df_for_streamlit.csv")

df1['age'] = df1['age'].astype(int)



menu=st.sidebar.radio("Menu",["Home", "Hospital Length of Stay Calculator", "Useful Recommendations", "About Me"])

if menu == "Home":

    st.markdown(
        "<h1 style='text-align: center;  color: #003100;'>Welcome to Your Hospital Length of Stay Prediction App!</h1>",
        unsafe_allow_html=True)
    st.sidebar.markdown("</div>", unsafe_allow_html=True)
    st.image("App_Streamlit/image.jpg", width=400, use_column_width=True)
    st.markdown("<p style='margin-top: 20px;'></p>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top: 20px;'></p>", unsafe_allow_html=True)
    st.write(
        "<p style='text-align: justify;'>Preparing for a surgery can be an anxious time, but we're here to help you better understand what to expect during your hospital stay! Our prediction app is designed to estimate whether your hospital stay will be short, medium, or prolonged based on specific input parameters.</p>",
            unsafe_allow_html=True)
    st.markdown("<p style='margin-top: 20px;'></p>", unsafe_allow_html=True)
    st.write(
        "<p style='text-align: justify;'>To find out the estimated length of your hospital stay, simply click on the 'Hospital Length of Stay Calculator' option in the side menu and follow the instructions!",
            unsafe_allow_html=True)
    st.markdown("<p style='margin-top: 20px;'></p>", unsafe_allow_html=True)
    st.write(
        "<p style='text-align: justify;'>In addition to the length of stay prediction, we also have a 'Recommendations' section in the side menu. Here, you can find helpful pre and post-surgery recommendations to ensure a smoother and more comfortable recovery!",
            unsafe_allow_html=True)
    st.markdown("<p style='margin-top: 20px;'></p>", unsafe_allow_html=True)
    st.write(
        "<p style='text-align: justify;'>Thank you for using our Hospital Length of Stay Prediction App. Wishing you a smooth and successful surgery and a speedy recovery!",
            unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


if menu == "Hospital Length of Stay Calculator":

    st.image("App_Streamlit/imag2.jpg", width=200, use_column_width=True)
    st.markdown("<p style='margin-top: 20px;'></p>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top: 20px;'></p>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #004b00'>Calculator</h2>",
                unsafe_allow_html=True)
    st.markdown("<p style='margin-top: 20px;'></p>", unsafe_allow_html=True)
    st.write("Now, we'll guide you through a few questions to gather the necessary details. Rest assured, your privacy is of utmost importance to us, and all your information will be treated with the strictest confidentiality.")
    st.markdown("<p style='margin-top: 20px;'></p>", unsafe_allow_html=True)
    st.write(
        "<p style='text-align: justify;'>Remember, our predictions are based on statistical analysis, and every patient's journey is unique. Your medical team will be there to support you throughout your recovery process.",
        unsafe_allow_html=True)
    st.markdown("<p style='margin-top: 20px;'></p>", unsafe_allow_html=True)


    X = df1.drop("LOS", axis=1)
    y = df1["LOS"]

    # getting categoricals from X to encode

    catego = X[["sex", 'emergency_op', 'operation_type', 'hypertension', 'diabetes']]

    #encoding categoricals

    encoder_X = OrdinalEncoder()
    categ_encod = encoder_X.fit_transform(catego)
    categ_encod = pd.DataFrame(categ_encod, columns=catego.columns)

    X[["sex", 'emergency_op', 'operation_type', 'hypertension', 'diabetes']] = categ_encod[
        ["sex", 'emergency_op', 'operation_type', 'hypertension', 'diabetes']]

    # encoding y

    encoder_y = OrdinalEncoder()
    y_enc = encoder_y.fit_transform(y.values.reshape(-1, 1))
    y = pd.DataFrame(y_enc)

    # X-y split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

    # training model
    model = RandomForestClassifier(criterion='entropy', max_samples=0.8,
                                   min_samples_leaf=10, min_samples_split=4,
                                   n_estimators=120)
    model.fit(X_train, y_train)


    #function to get user input parameters
    def user_input_parameter():
        age = st.number_input("Insert your Age", 0, 100)
        sex = st.selectbox("Sex", ('M', 'F'))
        height = st.slider("Insert your height (cm)", 40.0, 200.0)
        weight = st.slider("Insert your weight (Kg)", 4.0, 200.0)
        emergency_op = st.selectbox("Is your surgery planned?", ("Yes", "No"))
        operation_type = st.selectbox("Type of Surgery", ("Colorectal", "Biliary/Pancreas", "Stomach", "Breast", "Transplantation", "Vascular", "Hepatic", "Thyroid", "Others"))
        hypertension = st.selectbox("Are you Hypertensive?", ("Yes", "No"))
        diabetes = st.selectbox("Are you Diabetic?", ("Yes", "No"))

        data = {"age": age,
                "sex": sex,
              "height": height,
              "weight": weight,
              "emergency_op": emergency_op,
              "operation_type": operation_type,
              "hypertension": hypertension,
              "diabetes": diabetes
        }

        features_df = pd.DataFrame(data, index=[0])
        return features_df

    df_inputs = user_input_parameter()

    #getting categoricals from user input

    df_inputs_categ = df_inputs[['sex', 'emergency_op', 'operation_type', 'hypertension', 'diabetes']]

    #encode categ inputs from user
    df_inputs_encod = encoder_X.transform(df_inputs_categ)
    df_inputs_encod = pd.DataFrame(df_inputs_encod, columns=df_inputs_categ.columns)
    df_inputs[["sex", 'emergency_op', 'operation_type', 'hypertension', 'diabetes']] = df_inputs_encod[
        ["sex", 'emergency_op', 'operation_type', 'hypertension', 'diabetes']]


    if st.button("Show me my predicted Hospital Length"):
        # Perform the prediction and get the result
        predictions = model.predict(df_inputs)

        if predictions[0] == 0:
            st.success("Your Estimated Length in Hospital is: Medium")
        elif predictions[0] == 1:
            st.success("Your Estimated Length in Hospital is: Prolonged")
        elif predictions[0] == 2:
            st.success("Your Estimated Length in Hospital is: Short")
        else:
            st.success("Error")


    # get the Lottie animation
    url = requests.get("https://lottie.host/cc1a9d4b-d35a-4352-b616-8ff03fce6fb5/iTSXqPDEEc.json")
    url_json = dict()
    if url.status_code == 200:
        url_json = url.json()
    else:
        print("Error in URL")
    st.markdown("</div>", unsafe_allow_html=True)

    st_lottie(url_json, height=200, width=200)


if menu == "Useful Recommendations":
    st.image("App_Streamlit/imag3.jpg", width=200, use_column_width=True)
    st.markdown("<p style='margin-top: 20px;'></p>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top: 20px;'></p>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #004b00'>Surgical Patient Recommendations</h2>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top: 20px;'></p>", unsafe_allow_html=True)
    st.subheader("Pre-Surgery Recommendations:")
    before_surgery_recommendations = [
        "Maintain a healthy weight.",
        "Follow pre-surgery fasting instructions provided by your doctor.",
        "Avoid eating heavy meals the night before the surgery.",
        "Stay hydrated, but follow any specific fluid intake guidelines from your doctor.",
        "Notify your doctor about any medications you are currently taking.",
        "Stop taking blood-thinning medications as advised by your doctor.",
        "Get a good night's sleep before the surgery.",
    ]

    for recommendation in before_surgery_recommendations:
        st.write("- " + recommendation)

    after_surgery_recommendations = [
        "Follow post-surgery care instructions provided by your medical team.",
        "Take prescribed medications as scheduled.",
        "Engage in gentle exercises or physical therapy as advised by your doctor.",
        "Keep the surgical site clean and dry.",
        "Monitor for any signs of infection or complications and report them to your doctor.",
        "Eat a balanced diet to support healing.",
        "Stay hydrated and drink plenty of fluids.",
        "Avoid heavy lifting or strenuous activities until cleared by your doctor.",
        "Attend all follow-up appointments with your medical team."
    ]
    st.markdown("<p style='margin-top: 20px;'></p>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top: 20px;'></p>", unsafe_allow_html=True)
    st.subheader("Post-Surgery Recommendations:")
    for recommendation in after_surgery_recommendations:
        st.write("- " + recommendation)

    # get the Lottie animation
    url = requests.get("https://lottie.host/9deeb4e3-85cd-43c0-afdf-00058925badc/hSRUtkpjdy.json")
    url_json = dict()
    if url.status_code == 200:
        url_json = url.json()
    else:
        print("Error in URL")
    st.markdown("</div>", unsafe_allow_html=True)

    st_lottie(url_json, height=500, width=500)


if menu == "About Me":
    st.image("App_Streamlit/imag5.jpg", width=50, use_column_width=True)
    st.subheader("About Me")
    st.write(
        "<p style='text-align: justify;'>Hi! I am Sandra, a data enthusiast with a background in Healthcare. Currently, I am a student at Ironhack School, Data Analytics Bootcamp.</p>",
        unsafe_allow_html=True)

    st.subheader("Passion for Data Science")
    st.write(
        "<p style='text-align: justify;'>From reading books regarding Big Data and learning more about how AI can improve Healthcare, I became fascinated with Data Science! My constant thirst for knowledge led me to enroll in a Data Analytics Course.</p>",
        unsafe_allow_html=True)

    st.subheader("Course Project")
    st.write(
        "<p style='text-align: justify;'>This application is part of my final course project, 'Predicting Hospital Length of Stay of General Surgical Patients.' The main goal was to develop a supervised classification machine learning model that estimates the length of stay for patients scheduled for General Surgery Procedures.</p>",
        unsafe_allow_html=True)

    st.subheader("Interests and Hobbies")
    st.write(
        "<p style='text-align: justify;'>Apart from my Data Science interest, I have many hobbies, including Yoga and Weightlifting!</p>",
        unsafe_allow_html=True)

    st.subheader("Hope You Enjoy the App!")
    st.write(
        "<p style='text-align: justify;'>I hope you find this app helpful and informative. Feel free to explore the different features and try out the Hospital Length of Stay Calculator.</p>",
        unsafe_allow_html=True)

    st.subheader("Contact Details")
    st.write(
        "<p style='text-align: justify;'>If you have any questions or want to connect, you can reach out to me:</p>",
        unsafe_allow_html=True)
    st.write("Email: sandra_cris_cunha@hotmail.com")
    st.write("GitHub: https://github.com/sandraccris")
    st.write("LinkedIn: www.linkedin.com/in/sandra-cunha-a553a41b6/")
    st.write("Portfolio: https://troopl.com/sandra_cris_cunha")


st.sidebar.markdown("</div>", unsafe_allow_html=True)
st.sidebar.markdown("</div>", unsafe_allow_html=True)
st.sidebar.markdown("</div>", unsafe_allow_html=True)
st.sidebar.markdown("</div>", unsafe_allow_html=True)
st.sidebar.markdown("</div>", unsafe_allow_html=True)
st.sidebar.markdown("</div>", unsafe_allow_html=True)
st.sidebar.markdown("</div>", unsafe_allow_html=True)
st.sidebar.markdown("</div>", unsafe_allow_html=True)
st.sidebar.markdown("</div>", unsafe_allow_html=True)
st.sidebar.markdown("</div>", unsafe_allow_html=True)
st.sidebar.markdown("</div>", unsafe_allow_html=True)
st.sidebar.markdown("</div>", unsafe_allow_html=True)
st.sidebar.markdown("</div>", unsafe_allow_html=True)
st.sidebar.markdown("</div>", unsafe_allow_html=True)

st.sidebar.image("App_Streamlit/imaggif.gif", width=250)

