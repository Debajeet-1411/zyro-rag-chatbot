import streamlit as st

st.set_page_config(
    page_title="Zyro Dynamics HR Assistant",
    page_icon="🤖"
)

st.title("🤖 Zyro Dynamics HR Assistant")

st.markdown(
    '''
Ask questions about:

- Leave Policy
- Work From Home
- Compensation & Benefits
- Travel & Reimbursements
- Performance Reviews
- IT & Security
- Employee Handbook
'''
)

question = st.chat_input(
    "Ask an HR question..."
)

if question:

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):

        st.info(
            "This demo was created for the "
            "NIAT Masterclass RAG Challenge."
        )

        st.write(
            "In deployment, connect this UI "
            "to your RAG pipeline."
        )