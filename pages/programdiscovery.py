import streamlit as st


st.title("Program discovery & development")
st.page_link("streamlit_app.py", label="← Back to map")


st.info("Purpose: Align on goals and understand pain points to define the work.")


with st.expander("Collect goals & objectives, set timeline expectations — (VISTA & Client)"):
st.write("""
* Hold a kickoff meeting.
* Clarify desired outcomes and success measures.
* Agree on key milestones and target dates.
""")


with st.expander("Uncover pain points — (VISTA & Client)"):
st.write("""
* Identify blockers and risks.
* Document current workflows and gaps.
* Prioritize issues to address during implementation.
""")
