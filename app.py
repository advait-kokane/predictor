# import streamlit as st
# import pandas as pd
# import numpy as np
# import pickle

# # Load saved model & encoders
# model = pickle.load(open('model.pkl', 'rb'))
# encoders = pickle.load(open('encoders.pkl', 'rb'))

# # Load dataset
# df = pd.read_csv("nashik data.csv")

# # Custom CSS for styling
# CUSTOM_STYLE = """
# <style>
# :root {
#     --deep-navy: #0a192f;
#     --cool-teal: #64ffda;
#     --light-slate: #ccd6f6;
#     --slate: #8892b0;
#     --dark-slate: #495670;
#     --accent: #1e90ff;
#     --gradient: linear-gradient(135deg, #64ffda 0%, #1e90ff 100%);
#     --highlight: rgba(100, 255, 218, 0.2); /* subtle input focus shadow */
# }

# /* Main app styling */
# .stApp {
#     background: linear-gradient(135deg, var(--deep-navy), #0d2142) !important;
#     color: var(--light-slate) !important;
#     padding: 2rem !important;
# }

# /* Title styling */
# h1 {
#     text-align: center !important;
#     margin: 0 auto 1.5rem !important;
#     font-size: 2.5rem !important;
#     background: var(--gradient) !important;
#     -webkit-background-clip: text !important;
#     background-clip: text !important;
#     color: transparent !important;
#     position: relative !important;
#     padding-bottom: 1rem !important;
#     width: fit-content !important;
# }

# h1::after {
#     content: '' !important;
#     position: absolute !important;
#     bottom: 0 !important;
#     left: 50% !important;
#     transform: translateX(-50%) !important;
#     width: 120px !important;
#     height: 3px !important;
#     background: var(--gradient) !important;
#     border-radius: 3px !important;
# }

# /* Card container */
# div[data-testid="stBlock"] {
#     background: rgba(10, 25, 47, 0.7) !important;
#     backdrop-filter: blur(12px) !important;
#     -webkit-backdrop-filter: blur(12px) !important;
#     border-radius: 16px !important;
#     padding: 2.5rem !important;
#     border: 1px solid rgba(100, 255, 218, 0.15) !important;
#     box-shadow: 0 8px 32px rgba(2, 12, 27, 0.5) !important;
#     margin: 0 auto 2rem !important;
#     max-width: 800px !important;
# }

# /* Form elements */
# .stSelectbox, .stSlider, .stTextInput, .stNumberInput {
#     margin-bottom: 1.5rem !important;
#     width: 100% !important;
#     transition: all 0.3s ease !important;
#     box-shadow: 0 0 0 rgba(100,255,218,0) !important;
#     border-radius: 8px !important;
# }

# /* Input focus effect */
# .stSelectbox:focus-within, .stSlider:focus-within, .stTextInput:focus-within, .stNumberInput:focus-within {
#     box-shadow: 0 0 8px var(--cool-teal) !important;
# }

# /* Label styling */
# label {
#     font-size: 1rem !important;
#     color: var(--cool-teal) !important;
#     margin-bottom: 0.5rem !important;
#     display: block !important;
#     font-weight: 500 !important;
# }

# /* Custom slider styling */
# div[data-testid="stSlider"] > div {
#     padding: 0.8rem 1rem !important;
#     background: rgba(10, 25, 47, 0.6) !important;
#     border-radius: 10px !important;
#     border: 1px solid var(--dark-slate) !important;
# }

# div[data-testid="stThumbValue"] {
#     color: var(--cool-teal) !important;
#     font-weight: 600 !important;
# }

# /* The slider track */
# div[data-testid="stThumbValue"] + div > div {
#     background: var(--dark-slate) !important;
#     height: 6px !important;
# }

# /* The slider thumb */
# div[data-testid="stThumbValue"] + div > div > div {
#     background: var(--gradient) !important;
#     border: none !important;
#     width: 20px !important;
#     height: 20px !important;
#     box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3) !important;
# }

# /* Prediction button */
# .stButton > button {
#     width: 100% !important;
#     padding: 1.2rem !important;
#     font-size: 1.2rem !important;
#     background: var(--gradient) !important;
#     color: var(--deep-navy) !important;
#     border: none !important;
#     border-radius: 10px !important;
#     font-weight: 700 !important;
#     letter-spacing: 0.5px !important;
#     transition: all 0.3s ease !important;
#     box-shadow: 0 4px 20px rgba(100, 255, 218, 0.4) !important;
#     margin: 1.5rem 0 0 !important;
# }

# .stButton > button:hover {
#     transform: translateY(-2px) !important;
#     box-shadow: 0 6px 25px rgba(100, 255, 218, 0.6) !important;
# }

# /* Results styling */
# .stSuccess {
#     background: rgba(10, 25, 47, 0.7) !important;
#     border: 1px solid var(--cool-teal) !important;
#     border-radius: 12px !important;
# }

# .stSuccess > div {
#     color: var(--cool-teal) !important;
#     font-size: 1.3rem !important;
# }

# .stMarkdown {
#     color: var(--light-slate) !important;
#     font-size: 1.1rem !important;
#     line-height: 1.8 !important;
# }

# /* Error styling replaced with subtle teal accent */
# .stError {
#     background: rgba(100, 255, 218, 0.1) !important;
#     border: 1px solid rgba(64, 255, 200, 0.3) !important;
# }
# </style>
# """

# # Apply the custom styles
# st.markdown(CUSTOM_STYLE, unsafe_allow_html=True)

# # Main app content
# st.title("College Admission Predictor")

# with st.container():
#     branch = st.selectbox("Branch", sorted(df['Branch'].unique()))
#     category = st.selectbox("Category", sorted(df['Category'].unique()))
#     gender = st.selectbox("Gender", sorted(df['Gender'].unique()))
#     region = st.selectbox("Region", sorted(df['Region'].unique()))
#     tech = st.selectbox("Technical/Non-Technical", sorted(df['Technical/Non Technical'].unique()))
    
#     # Dual input for marks
#     col1, col2 = st.columns([2, 1])
#     with col1:
#         marks_slider = st.slider("Enter your Marks (%)", min_value=0.0, max_value=100.0, value=70.0, step=0.1)
#     with col2:
#         marks_input = st.number_input("Or type Marks (%)", min_value=0.0, max_value=100.0, value=70.0, step=0.1)
    
#     # Use whichever input was last updated
#     marks = marks_input if marks_input != marks_slider else marks_slider

# if st.button("Predict Possible Colleges"):
#     # Prediction logic
#     filtered_df = df[
#         (df['Branch'] == branch) &
#         (df['Category'] == category) &
#         (df['Gender'] == gender) &
#         (df['Region'] == region) &
#         (df['Technical/Non Technical'] == tech)
#     ]

#     possible_colleges = []
#     X_columns = list(model.feature_names_in_)

#     for _, row in filtered_df.iterrows():
#         row_data = row.copy()
#         row_data['Student_Marks'] = marks
#         for col in ['Branch', 'Category', 'Gender', 'Region', 'Technical/Non Technical', 'College']:
#             row_data[col] = encoders[col].transform([row_data[col]])[0]
#         input_data = row_data.reindex(X_columns).astype(float)
#         pred = model.predict([input_data])[0]
        
#         if pred == 1:
#             college_name = encoders['College'].inverse_transform([int(row_data['College'])])[0]
#             possible_colleges.append(college_name)

#     if possible_colleges:
#         # Create a DataFrame for stylish table
#         result_df = pd.DataFrame({
#             "S.No": range(1, len(possible_colleges)+1),
#             "College Name": sorted(set(possible_colleges))
#         })

#         # Display as styled table
#         st.markdown(
#             """
#             <style>
#             .result-table {
#                 width: 100%;
#                 border-collapse: collapse;
#                 box-shadow: 0 4px 15px rgba(100, 255, 218, 0.2);
#                 border-radius: 10px;
#                 overflow: hidden;
#             }
#             .result-table th, .result-table td {
#                 padding: 12px 15px;
#                 text-align: left;
#             }
#             .result-table th {
#                 background: linear-gradient(135deg, #64ffda 0%, #1e90ff 100%);
#                 color: #0a192f;
#                 font-weight: 600;
#             }
#             .result-table tr:nth-child(even) {
#                 background: rgba(100,255,218,0.05);
#             }
#             .result-table tr:hover {
#                 background: rgba(100,255,218,0.15);
#                 transition: 0.3s;
#             }
#             </style>
#             """, unsafe_allow_html=True
#         )
#         st.markdown(result_df.to_html(index=False, classes="result-table"), unsafe_allow_html=True)
#     else:
#         st.error("❌ No colleges found matching your criteria")


import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load saved model & encoders
model = pickle.load(open('model.pkl', 'rb'))
encoders = pickle.load(open('encoders.pkl', 'rb'))

# Load dataset
df = pd.read_csv("nashik data.csv")

# Custom CSS for styling
CUSTOM_STYLE = """
<style>
:root {
    --deep-navy: #0a192f;
    --cool-teal: #64ffda;
    --light-slate: #ccd6f6;
    --slate: #8892b0;
    --dark-slate: #495670;
    --accent: #1e90ff;
    --gradient: linear-gradient(135deg, #64ffda 0%, #1e90ff 100%);
    --highlight: rgba(100, 255, 218, 0.2); /* subtle input focus shadow */
}

/* Main app styling */
.stApp {
    background: linear-gradient(135deg, var(--deep-navy), #0d2142) !important;
    color: var(--light-slate) !important;
    padding: 2rem !important;
}

/* Title styling */
h1 {
    text-align: center !important;
    margin: 0 auto 1.5rem !important;
    font-size: 2.5rem !important;
    background: var(--gradient) !important;
    -webkit-background-clip: text !important;
    background-clip: text !important;
    color: transparent !important;
    position: relative !important;
    padding-bottom: 1rem !important;
    width: fit-content !important;
}

h1::after {
    content: '' !important;
    position: absolute !important;
    bottom: 0 !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    width: 120px !important;
    height: 3px !important;
    background: var(--gradient) !important;
    border-radius: 3px !important;
}

/* Card container */
div[data-testid="stBlock"] {
    background: rgba(10, 25, 47, 0.7) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border-radius: 16px !important;
    padding: 2.5rem !important;
    border: 1px solid rgba(100, 255, 218, 0.15) !important;
    box-shadow: 0 8px 32px rgba(2, 12, 27, 0.5) !important;
    margin: 0 auto 2rem !important;
    max-width: 800px !important;
}

/* Form elements */
.stSelectbox, .stSlider, .stTextInput, .stNumberInput {
    margin-bottom: 1.5rem !important;
    width: 100% !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 0 0 rgba(100,255,218,0) !important;
    border-radius: 8px !important;
}

/* Input focus effect */
.stSelectbox:focus-within, .stSlider:focus-within, .stTextInput:focus-within, .stNumberInput:focus-within {
    box-shadow: 0 0 8px var(--cool-teal) !important;
}

/* Label styling */
label {
    font-size: 1rem !important;
    color: var(--cool-teal) !important;
    margin-bottom: 0.5rem !important;
    display: block !important;
    font-weight: 500 !important;
}

/* Custom slider styling */
div[data-testid="stSlider"] > div {
    padding: 0.8rem 1rem !important;
    background: rgba(10, 25, 47, 0.6) !important;
    border-radius: 10px !important;
    border: 1px solid var(--dark-slate) !important;
}

div[data-testid="stThumbValue"] {
    color: var(--cool-teal) !important;
    font-weight: 600 !important;
}

/* The slider track */
div[data-testid="stThumbValue"] + div > div {
    background: var(--dark-slate) !important;
    height: 6px !important;
}

/* The slider thumb */
div[data-testid="stThumbValue"] + div > div > div {
    background: var(--gradient) !important;
    border: none !important;
    width: 20px !important;
    height: 20px !important;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3) !important;
}

/* Prediction button */
.stButton > button {
    width: 100% !important;
    padding: 1.2rem !important;
    font-size: 1.2rem !important;
    background: var(--gradient) !important;
    color: var(--deep-navy) !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    letter-spacing: 0.5px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 20px rgba(100, 255, 218, 0.4) !important;
    margin: 1.5rem 0 0 !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 25px rgba(100, 255, 218, 0.6) !important;
}

/* Results styling */
.stSuccess {
    background: rgba(10, 25, 47, 0.7) !important;
    border: 1px solid var(--cool-teal) !important;
    border-radius: 12px !important;
}

.stSuccess > div {
    color: var(--cool-teal) !important;
    font-size: 1.3rem !important;
}

.stMarkdown {
    color: var(--light-slate) !important;
    font-size: 1.1rem !important;
    line-height: 1.8 !important;
}

/* Error styling replaced with subtle teal accent */
.stError {
    background: rgba(100, 255, 218, 0.1) !important;
    border: 1px solid rgba(64, 255, 200, 0.3) !important;
}
</style>
"""

# Apply the custom styles
st.markdown(CUSTOM_STYLE, unsafe_allow_html=True)

# Main app content
st.title("College Admission Predictor")

with st.container():
    branch = st.selectbox("Branch", sorted(df['Branch'].unique()))
    category = st.selectbox("Category", sorted(df['Category'].unique()))
    gender = st.selectbox("Gender", sorted(df['Gender'].unique()))
    region = st.selectbox("Region", sorted(df['Region'].unique()))
    tech = st.selectbox("Technical/Non-Technical", sorted(df['Technical/Non Technical'].unique()))
    
    # Dual input for marks
    col1, col2 = st.columns([2, 1])
    with col1:
        marks_slider = st.slider("Enter your Marks (%)", min_value=0.0, max_value=100.0, value=70.0, step=0.1)
    with col2:
        marks_input = st.number_input("Or type Marks (%)", min_value=0.0, max_value=100.0, value=70.0, step=0.1)
    
    # Use whichever input was last updated
    marks = marks_input if marks_input != marks_slider else marks_slider

if st.button("Predict Possible Colleges"):
    # Prediction logic
    filtered_df = df[
        (df['Branch'] == branch) &
        (df['Category'] == category) &
        (df['Gender'] == gender) &
        (df['Region'] == region) &
        (df['Technical/Non Technical'] == tech)
    ]

    possible_colleges = []
    X_columns = list(model.feature_names_in_)

    for _, row in filtered_df.iterrows():
        row_data = row.copy()
        row_data['Student_Marks'] = marks
        for col in ['Branch', 'Category', 'Gender', 'Region', 'Technical/Non Technical', 'College']:
            row_data[col] = encoders[col].transform([row_data[col]])[0]
        input_data = row_data.reindex(X_columns).astype(float)
        pred = model.predict([input_data])[0]
        
        if pred == 1:
            college_name = encoders['College'].inverse_transform([int(row_data['College'])])[0]
            possible_colleges.append(college_name)

    if possible_colleges:
        # Create a DataFrame for stylish table
        result_df = pd.DataFrame({
            "S.No": range(1, len(possible_colleges)+1),
            "College Name": sorted(set(possible_colleges))
        })

        # Display as styled table
        st.markdown(
            """
            <style>
            .result-table {
                width: 100%;
                border-collapse: collapse;
                box-shadow: 0 4px 15px rgba(100, 255, 218, 0.2);
                border-radius: 10px;
                overflow: hidden;
            }
            .result-table th, .result-table td {
                padding: 12px 15px;
                text-align: left;
            }
            .result-table th {
                background: linear-gradient(135deg, #64ffda 0%, #1e90ff 100%);
                color: #0a192f;
                font-weight: 600;
            }
            .result-table tr:nth-child(even) {
                background: rgba(100,255,218,0.05);
            }
            .result-table tr:hover {
                background: rgba(100,255,218,0.15);
                transition: 0.3s;
            }
            </style>
            """, unsafe_allow_html=True
        )
        st.markdown(result_df.to_html(index=False, classes="result-table"), unsafe_allow_html=True)
    else:
        st.error("❌ No colleges found matching your criteria")


