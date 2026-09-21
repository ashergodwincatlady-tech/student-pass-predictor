import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("claes.csv")

st.title("🎓 Student Pass Predictor")

st.write("Enter the student's information below.")

education_numbers = {
    "Pre-K": 0,
    "Elementary": 1,
    "Middle School": 2,
    "High School": 3,
    "University": 4
}

study_numbers = {
    "Active Recall": 0,
    "The Feynman Technique": 1,
    "Spaced Repetition": 2
}

df["Education_Level"] = df["Education_Level"].map(education_numbers)
df["Study_method"] = df["Study_method"].map(study_numbers)

X = df[
    [
        "Hours_studied",
        "Attendance",
        "Sleep_hours",
        "Education_Level",
        "Study_method"
    ]
]

y = df["Passed"]

model = DecisionTreeClassifier(
    max_depth=4,
    min_samples_split=2,
    random_state=42
)

model.fit(X, y)

st.header("Student Information")

hours = st.number_input(
    "Hours studied",
    min_value=0.0,
    max_value=24.0,
    value=0.0,
    step=0.5
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=00.0,
    step=1.0
)

sleep = st.number_input(
    "Sleep hours",
    min_value=0.0,
    max_value=24.0,
    value=0.0,
    step=0.5
)

education = st.selectbox(
    "Education Level",
    [
        "Pre-K",
        "Elementary",
        "Middle School",
        "High School",
        "University"
    ]
)

study_method = st.selectbox(
    "Study Method",
    [
        "Active Recall",
        "The Feynman Technique",
        "Spaced Repetition"
    ]
)

if st.button("🔮 Predict"):

    if education == "Not specified":
        st.error("Education level not specified. Please select an education level.")
    else:
        education_value = education_numbers[education]

    if study_method == "Not specified":
        st.error("Study method not specified. Please select a study method.")
    else:
        study_value = study_numbers[study_method]

    new_student = pd.DataFrame(
        [[
            hours,
            attendance,
            sleep,
            education_value,
            study_value
        ]],
        columns=[
            "Hours_studied",
            "Attendance",
            "Sleep_hours",
            "Education_Level",
            "Study_method"
        ]
    )

    # Predict
    prediction = model.predict(new_student)

    # Show result
    if prediction[0] == "Yes":
        st.success("🎉 Prediction: PASS")
    else:
        st.error("Prediction: FAIL")