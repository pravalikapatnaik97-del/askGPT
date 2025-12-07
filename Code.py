import streamlit as st

from google import genai

client = genai.Client(api_key="")
st.title("askGPT")
def inputs(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Please summerise the file: {prompt}",
    )
    return response.text
file=st.file_uploader("Upload a file for summerizing")
if st.button('Upload'):
    if file:
        with st.spinner("Reading the file..."): 
            prompt=file.read()
            result=inputs(prompt)      
            st.write(result)
            st.snow()
    else:
        st.warning("1st ask any question!")


