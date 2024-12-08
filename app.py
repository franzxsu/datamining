import streamlit as st

st.title("data mining")
st.subheader("simply drag and drop your file or use the file picker to upload files")

uploaded_file = st.file_uploader(
    "upload your file here:",
    type=None,
    accept_multiple_files=True,
)

if uploaded_file:
    st.success(f"File uploaded: {uploaded_file.name}")
    st.write("File Details:")
    st.write(f"Name: {uploaded_file.name}")
    st.write(f"Type: {uploaded_file.type}")
    st.write(f"Size: {uploaded_file.size} bytes")

    try:
        file_content = uploaded_file.read().decode("utf-8")
        st.text_area("File Content:", file_content, height=200)
    except Exception as e:
        st.warning("Could not read file content. The file might be binary.")