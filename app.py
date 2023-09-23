import streamlit as st
import streamlit.components.v1 as components

# Load the custom component
camera_3d_overlay = components.html(open("camera_3d_overlay.html").read(), height=600)

st.write("Camera feed with 3D model overlay.")
