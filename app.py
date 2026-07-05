import streamlit as st
import uuid

from leaders.language_leader import language_leader

from storage.database import (
    init_db,
    save_message,
)

st.set_page_config(
    page_title="Finance AI Agent",
    page_icon="📈",
    layout="wide",
)

init_db()

st.html("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<style>
.app-title {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 0;
}
.app-title i {
    font-size: 1.4rem;
}

div[data-testid="stChatMessage"] {
    border-radius: 10px;
}

.sidebar-label {
    display: flex;
    align-items: center;
    gap: 8px;
    font-weight: 600;
    font-size: 0.95rem;
    margin-bottom: 2px;
}
</style>
""")

# NEW SESSION EVERY REFRESH
st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

st.sidebar.markdown(
    '<div class="sidebar-label"><i class="fa-solid fa-clock-rotate-left"></i>&nbsp;New Session</div>',
    unsafe_allow_html=True,
)

if st.sidebar.button("New Chat", use_container_width=True, icon=":material/add:"):
    st.session_state.session_id = str(uuid.uuid4())
    st.session_state.messages = []
    st.rerun()

st.markdown(
    '<h1 class="app-title"><i class="fa-solid fa-chart-line"></i>&nbsp;Finance AI Agent</h1>',
    unsafe_allow_html=True,
)
st.caption("Ask anything about stocks, markets, or companies.")

for msg in st.session_state.messages:
    avatar = ":material/person:" if msg["role"] == "user" else ":material/smart_toy:"
    with st.chat_message(msg["role"], avatar=avatar):
        st.write(msg["content"])

user_input = st.chat_input(
    "Ask anything about stocks, markets, or companies..."
)

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Still saves to DB (optional)
    save_message(
        st.session_state.session_id,
        "user",
        user_input
    )

    with st.chat_message("user", avatar=":material/person:"):
        st.write(user_input)

    history_text = ""

    for msg in st.session_state.messages:
        history_text += f"{msg['role']}: {msg['content']}\n"

    with st.chat_message("assistant", avatar=":material/smart_toy:"):
        with st.spinner("Analyzing markets..."):

            response = language_leader.run(
                input=history_text,
                session_id=st.session_state.session_id
            )

            if hasattr(response, "content"):
                response = response.content
            else:
                response = str(response)

            st.write(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    save_message(
        st.session_state.session_id,
        "assistant",
        response
    )