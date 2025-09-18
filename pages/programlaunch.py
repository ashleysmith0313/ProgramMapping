import streamlit as st


st.title("Implementation")
st.page_link("streamlit_app.py", label="← Back to map")


st.info("Purpose: Configure systems and train users to get the program running.")


with st.expander("Onboard clinician leaders — (Client)"):
st.write("""
* Identify leaders and champions.
* Align on communication to broader teams.
""")


with st.expander("Build / setup VMS technology — (VISTA)"):
st.write("""
* Configure vendor management system.
* Establish workflows and templates.
""")


with st.expander("Setup technology access — (VISTA & Client)"):
st.write("""
* Provision accounts and permissions.
* Validate security requirements are met.
""")


with st.expander("Conduct technology training — (VISTA)"):
st.write("""
* Deliver training sessions and quick reference guides.
* Confirm readiness via a go-live checklist.
""")