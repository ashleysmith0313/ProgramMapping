import streamlit as st


st.title("Reporting")
st.page_link("streamlit_app.py", label="← Back to map")


st.info("Purpose: Review outcomes and identify improvements.")


with st.expander("Compile results & identify opportunities — (VISTA & Client)"):
st.write("""
* Summarize KPIs and qualitative feedback.
* Highlight quick wins and longer-term improvements.
""")


with st.expander("Review results — (VISTA & Client)"):
st.write("""
* Present findings and agree on action items.
* Decide on timeline for next review.
""")