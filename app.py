import streamlit as st
import pandas as pd

st.title("Talking Rabbitt: Conversational Data Analytics")

st.write("Upload a CSV file and ask questions about your data.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Dataset Preview")
    st.write(df)

    question = st.text_input("Ask a question about your data")

    if question:
        st.write("Analyzing your question...")
        
        # Simple demo logic
        numeric_cols = df.select_dtypes(include='number').columns
        
        if len(numeric_cols) > 0:
            st.write("Sample Insight: The system detected numeric data and generated a visualization.")
            st.bar_chart(df[numeric_cols])
        else:
            st.write("Please upload a dataset with numeric values.")
