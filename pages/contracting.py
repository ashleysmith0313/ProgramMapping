import streamlit as st


st.title("Contracting")
st.page_link("streamlit_app.py", label="← Back to map")


st.info("Purpose: Formalize scope, pricing, and terms.")


with st.expander("Contract signed — (VISTA & Client)"):
st.write("""
* Finalize scope of services and responsibilities.
* Confirm pricing, term, and exit provisions.
* Capture points-of-contact and communication cadence.
""")