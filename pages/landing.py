import streamlit as st

st.set_page_config(
    page_title="Circle Up Community",
    page_icon="🟣",
    layout="wide",
    initial_sidebar_state="collapsed"
)

from menu import menu


st.divider()
if st.button(':material/hiking: Volver al Inicio', type="secondary", help='Volver al menú principal', use_container_width=True):
    st.switch_page('app.py')
st.image('./gallery/WebSvg/main_footer.svg', use_column_width=True)

menu()