import streamlit as st
import src.ui.constants as c

def render_title():
    left, middle , right = st.columns([0.27, 0.65, 0.1])
    with left:
        st.empty()
    with middle:
        if st.session_state.danger_level == "safe":
            st.markdown(c.safe_title, True)
        elif st.session_state.danger_level == "warning":
            st.markdown(c.warning_title, True)
        elif st.session_state.danger_level == "dangerous":
            st.markdown(c.dangerous_title, True)
        else:
            st.markdown(c.starter_title, True)
    with right:
        st.empty()

def render_body(run_orchestrator):
    if st.session_state.danger_level == "starter":
        with st.form('form1', clear_on_submit = False):
            query = st.text_input(
                label='**Coloque o endereço do site que deseja validar na caixa de texto abaixo**', 
                placeholder='siteparavalidar.com' 
            )
            submitted = st.form_submit_button('Validar')

            if submitted:
                run_orchestrator(query)
    elif st.session_state.danger_level == "safe":
        st.html(c.safe_body)
    elif st.session_state.danger_level == "warning":
        st.html(c.warning_body)
    elif st.session_state.danger_level == "dangerous":
        st.html(c.dangerous_body)

def render_reload_button():
    left, middle , right = st.columns([0.47, 0.65, 0.1])
    with left:
        st.empty()
    with middle:
        if st.button('Recarregar Página'):
            st.session_state.danger_level = "starter"
            st.rerun()
    with right:
        st.empty()
    

def layout(
        run_orchestrator
):
    render_title()
    render_body(run_orchestrator)
    render_reload_button()
