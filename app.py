import streamlit as st
import streamlit.components.v1 as components

# Load the custom component
camera_component = components.html(open("camera_component.html").read(), height=600)

st.write("Point your camera at a Hiro marker to view the 3D model in AR.")
