import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('model.pkl','rb'))
encoders = pickle.load(open('encoders.pkl','rb'))
df = pd.read_csv("nashik data.csv")

st.set_page_config(page_title="College Predictor", page_icon="🚀")

st.markdown("""
<style>
body { backdrop-filter: blur(7px); background: rgba(255,255,255,0.4); }
.glass {
  background: rgba(255,255,255,0.25);
  border: 1px solid rgba(255,255,255,0.18);
  box-shadow: 0 8px 32px rgba(0,0,0,0.37);
  border-radius:15px;
  padding:1.5rem; margin-bottom:1.5rem;
}
</style>""",unsafe_allow_html=True)

if st.checkbox("🌙 Dark Mode"):
    st.markdown("<style>body{background:#111;color:white;}</style>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>College Admission Predictor 🚀</h1>", unsafe_allow_html=True)

st.markdown("<div class='glass'>", unsafe_allow_html=True)
branch = st.selectbox("Branch", sorted(df['Branch'].unique()))
category = st.selectbox("Category", sorted(df['Category'].unique()))
gender = st.selectbox("Gender", sorted(df['Gender'].unique()))
region = st.selectbox("Region", sorted(df['Region'].unique()))
tech = st.selectbox("Technical/Non-Technical", sorted(df['Technical/Non Technical'].unique()))
marks = st.slider("Enter your Marks (%)", 0.0, 100.0, 70.0, 0.5)
go = st.button("🔍 Predict")
st.markdown("</div>", unsafe_allow_html=True)

if go:
    filt = df[(df['Branch']==branch)&(df['Category']==category)&(df['Gender']==gender)&
              (df['Region']==region)&(df['Technical/Non Technical']==tech)]
    X_cols = list(model.feature_names_in_)
    possible=[]
    for _,row in filt.iterrows():
        r=row.copy(); r['Student_Marks']=marks
        for c in ['Branch','Category','Gender','Region','Technical/Non Technical','College']:
            r[c]=encoders[c].transform([r[c]])[0]
        inp=r.reindex(X_cols).astype(float)
        if model.predict([inp])[0]==1:
            cname=encoders['College'].inverse_transform([int(r['College'])])[0]
            possible.append(cname)
    if possible:
        st.success("🎯 Admission Possible:")
        tbl=pd.DataFrame({"College":sorted(set(possible))})
        st.table(tbl.style.set_properties(**{
            'background-color':'#ffffffaa',
            'border':'1px solid #ddd',
            'border-radius':'8px',
            'box-shadow':'0 4px 16px rgba(0,0,0,0.2)'
        }))
    else:
        st.error("❌ No colleges found!")
