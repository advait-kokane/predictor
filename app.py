import streamlit as st
import pandas as pd
import pickle

# --------------------------
# Load assets
# --------------------------
model = pickle.load(open('model.pkl', 'rb'))
encoders = pickle.load(open('encoders.pkl', 'rb'))
df = pd.read_csv('nashik data.csv')

st.set_page_config(page_title="College Predictor", page_icon="🚀")
st.title("College Admission Predictor 🚀")

# --------------------------
# Inputs
# --------------------------
with st.form("form"):
    branch = st.selectbox("Branch", sorted(df['Branch'].unique()))
    category = st.selectbox("Category", sorted(df['Category'].unique()))
    gender = st.selectbox("Gender", sorted(df['Gender'].unique()))
    region = st.selectbox("Region", sorted(df['Region'].unique()))
    tech = st.selectbox("Technical/Non-Technical", sorted(df['Technical/Non Technical'].unique()))
    marks = st.slider("Enter your Marks (%)", 0.0, 100.0, 70.0, 0.5)
    submitted = st.form_submit_button("🔍 Predict")

# --------------------------
# Prediction
# --------------------------
if submitted:
    filt = df[
        (df['Branch'] == branch) &
        (df['Category'] == category) &
        (df['Gender'] == gender) &
        (df['Region'] == region) &
        (df['Technical/Non Technical'] == tech)
    ]

    X_cols = list(model.feature_names_in_)
    possible = []

    for _, row in filt.iterrows():
        r = row.copy()
        r['Student_Marks'] = marks

        # encode categorical variables
        for col in ['Branch','Category','Gender','Region','Technical/Non Technical','College']:
            r[col] = encoders[col].transform([r[col]])[0]

        inp = r.reindex(X_cols).astype(float)
        if model.predict([inp])[0] == 1:
            cname = encoders['College'].inverse_transform([int(r['College'])])[0]
            possible.append(cname)

    if possible:
        st.success("🎯 Admission Possible in following Colleges:")
        for c in sorted(set(possible)):
            st.write(f"• **{c}**")
    else:
        st.error("❌ No colleges found!")
