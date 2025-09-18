import streamlit as st


st.title("Program Partnership Alignment")
st.page_link("streamlit_app.py", label="← Back to map")


st.info("Purpose: Align teams, roles, and technology to start work.")


with st.expander("Solutions proposal delivered — (VISTA)"):
st.write("""
* Present delivery plan and assumptions.
* Share any requirements for client resources.
""")


with st.expander("Define roles & responsibilities — (VISTA & Client)"):
st.write("""
* RACI (who is Responsible, Accountable, Consulted, Informed).
* Confirm escalation path and decision owners.
""")


with st.expander("Gain alignment & agreement — (VISTA & Client)"):
st.write("""
* Sign off on the plan and RACI.
* Schedule standing touchpoints.
""")


with st.expander("Technology vendor engaged — (VISTA)"):
st.write("""
* Notify vendor(s) and kick off integrations if needed.
* Share timelines and access requirements.
""")