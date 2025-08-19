import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load saved model & encoders
model = pickle.load(open('model.pkl', 'rb'))
encoders = pickle.load(open('encoders.pkl', 'rb'))

# Load dataset
df = pd.read_csv("nashik data.csv")

st.title("College Admission Predictor 🚀")

# Dropdowns using existing values from dataset
branch = st.selectbox("Branch", sorted(df['Branch'].unique()))
category = st.selectbox("Category", sorted(df['Category'].unique()))
gender = st.selectbox("Gender", sorted(df['Gender'].unique()))
region = st.selectbox("Region", sorted(df['Region'].unique()))
tech = st.selectbox("Technical/Non-Technical", sorted(df['Technical/Non Technical'].unique()))
marks = st.slider("Enter your Marks (%)", min_value=0.0, max_value=100.0, value=70.0, step=0.5)

if st.button("Predict Possible Colleges"):

    # 1) Filter dataset based on user inputs
    filtered_df = df[
        (df['Branch'] == branch) &
        (df['Category'] == category) &
        (df['Gender'] == gender) &
        (df['Region'] == region) &
        (df['Technical/Non Technical'] == tech)
    ]

    possible_colleges = []

    # 2) use exactly same features used during training
    X_columns = list(model.feature_names_in_)

    for _, row in filtered_df.iterrows():
        row_data = row.copy()
        row_data['Student_Marks'] = marks

        # Encode ALL categorical columns as done during model training
        for col in ['Branch', 'Category', 'Gender', 'Region', 'Technical/Non Technical', 'College']:
            row_data[col] = encoders[col].transform([row_data[col]])[0]

        # Reindex according to training column order
        input_data = row_data.reindex(X_columns).astype(float)

        # Predict
        pred = model.predict([input_data])[0]

        if pred == 1:
            # decode college name back
            college_name = encoders['College'].inverse_transform([int(row_data['College'])])[0]
            possible_colleges.append(college_name)

    if possible_colleges:
        st.success("🎯 Admission Possible in Following Colleges:")
        for i, c in enumerate(sorted(set(possible_colleges)), start=1):
            st.write(f"{i}. {c}")
    else:
        st.error("❌ No colleges found!")


