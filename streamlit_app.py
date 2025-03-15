import streamlit as st
import pandas as pd
import numpy as np
from PyPDF2 import PdfReader
from io import StringIO
from datetime import date  # Import for today's date

st.title("🎈Jinginakadi")
st.write(
    "Let's start building! For help here is link [docs.streamlit.io](https://docs.streamlit.io/)."
)
with st.sidebar:
    st.markdown("""
    # 🔹 Description

    This tool is useful for businesses, and individuals** who want to ease reviews.

    ### 🚀 How It Works
    1 ** Upload file.  
    2 ** Automated Workflow   
    3 ** Download file

    ### 🔹 Key Features
    ---
    """)
option = st.selectbox(
    "Select format of file?",
    ("LEDES", "Text", "MS Excel", "CSV", "XML", "Custom"),
)

st.write("You selected:", option)

uploaded_file = st.file_uploader("Upload a legal document (Word or PDF)", type=["docx", "pdf"], accept_multiple_files=True)


st.write(
    "Summary of "+ str(len(uploaded_file))+" "+option+" file(s)"
)

#df = pd.DataFrame(
#    np.random.randn(5, 5), columns=("col %d" % i for i in range(5))
#)

#st.table(df)
# Check if any files are uploaded
if uploaded_file:
    # Extract the names of the uploaded files
    file_names = [file.name for file in uploaded_file]

    # Create a DataFrame with the file names
    df = pd.DataFrame({
        "File Name": file_names,  # Add other data if needed
        "Date":date.today()
    })
    df["Amount"] = [f"$ {value:.2f}" for value in np.random.randn(len(df))*1000]
    # Display the DataFrame
    ##st.write("Uploaded Files DataFrame:")
    st.write(df)
else:
    st.write("Please upload some files!")

#for i in range(len(uploaded_file)):
#    st.write(uploaded_file[i].name)

 # Add copy to clipboard button
if st.button("📋 Submit "+ str(len(uploaded_file))+" "+option+" file(s) for review", use_container_width=True):
    st.toast("File(s) submitted for review !", icon="✅")

if uploaded_file:
    st.write("Uploaded file(s):")
    for file in uploaded_file:
        st.write(f"- {file.name}")  # Display the name of the uploaded file
        
        # Check file type and process content
        if file.name.endswith(".pdf"):
            st.write(f"**Short summary of {file.name}:**")
            pdf_reader = PdfReader(file)
            pdf_text = ""
            for page in pdf_reader.pages:
                pdf_text += page.extract_text()
                break  # Only read the first page
            # Show the first 4 lines
            pdf_lines = pdf_text.split("\n")[:4]
            st.write("\n".join(pdf_lines))