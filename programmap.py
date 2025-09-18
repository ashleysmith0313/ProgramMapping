import streamlit as st


st.set_page_config(
page_title="Transitional Management Solution",
page_icon="📊",
layout="wide",
)


st.title("Rapid Deployment Solution: Transitional Management Solution")
st.subheader("Implementation Process")


st.markdown(
"""
Click a stage below to see its details. You can also use the sidebar to jump between pages.
"""
)


# Map the big top boxes to their pages
PAGES = [
("Program discovery & development", "pages/01_Program_Discovery.py"),
("Contracting", "pages/02_Contracting.py"),
("Program Partnership Alignment", "pages/03_Program_Partnership_Alignment.py"),
("Implementation", "pages/04_Implementation.py"),
("Program Launch", "pages/05_Program_Launch.py"),
("Reporting", "pages/06_Reporting.py"),
]


# Optional: show your original image (place it in assets/ as program_map.png)
# st.image("assets/program_map.png", use_column_width=True)


st.write("")
cols = st.columns(len(PAGES), gap="large")
for (label, path), col in zip(PAGES, cols):
with col:
st.markdown(
f"<div style='padding:14px 10px;border-radius:16px;background:#0f766e;"
f"color:white;text-align:center;font-weight:700;min-height:90px;display:flex;"
f"align-items:center;justify-content:center;'>" + label + "</div>",
unsafe_allow_html=True,
)
if st.button("Open", use_container_width=True, key=label):
# Navigate to the page for this box
try:
st.switch_page(path)
except Exception:
# Fallback: show a link if switch_page isn't available
st.page_link(path, label=f"Go to {label}")


st.divider()


st.caption(
"Responsible legend: **VISTA** | **Client** | **VISTA & Client** — used on the details pages."
)