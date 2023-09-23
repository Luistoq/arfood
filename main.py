from echo3d_api import *
import streamlit as st
from render import *

def fetch_3d_models(api_key, security_key):
    # Retrieve 3d models via Echo3D API
    api = Echo3DAPI(api_key=api_key, security_key=security_key)
    return api.retrieve_model_info()

def render_selected_model(api_key, security_key, entry_id):
    api = Echo3DAPI(api_key=api_key, security_key=security_key)
    renderer = Renderer('downloads', api.entries)
    file_format = api.retrieve(entry_id)

    if file_format == 'obj':
        renderer.obj_render(entry_id)
    elif file_format == 'glb':
        renderer.glb_render(entry_id)
    else:
        st.write("File format " + file_format + " not supported yet")

def main():
    st.title("Echo3D Integration with Streamlit")
    
    api_key = st.text_input("Enter your Echo3D API Key:", type="solitary-dream-8207")
    security_key = st.text_input("Enter your Echo3D Security Key:", type="7e5d1522-bc79-4cad-a0be-4c12743a2520")
    
    if st.button("Fetch 3D Models"):
        model_list = fetch_3d_models(api_key, security_key)
        
        model_names = {key: value[1] for key, value in model_list.items()}
        selected_model_name = st.selectbox("Choose a 3D model to render:", list(model_names.values()))
        selected_model_id = [key for key, value in model_names.items() if value == selected_model_name][0]

        if st.button("Render Model"):
            render_selected_model(api_key, security_key, model_list[selected_model_id][0])

if __name__ == "__main__":
    main()
