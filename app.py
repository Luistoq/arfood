import streamlit as st
from PIL import Image
import numpy as np

def main():
    st.title("Webcam Image Capture with Streamlit")
    
    img_file_buffer = st.camera_input("Take a picture")
    
    if img_file_buffer is not None:
        # To read image file buffer as a PIL Image:
        img = Image.open(img_file_buffer)
        
        # Display the captured image
        st.image(img, caption="Captured Image", use_column_width=True)
        
        # To convert PIL Image to numpy array:
        img_array = np.array(img)
        
        # Display the type and shape of the numpy array
        st.write("Type of numpy array:", type(img_array))
        st.write("Shape of image array:", img_array.shape)

if __name__ == "__main__":
    main()
