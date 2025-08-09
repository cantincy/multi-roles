import streamlit as st

from agent import Agent
from config import Config


@st.cache_resource
def get_ying():
    return Agent(Config.YING_SYSTEM_PROMPT, Config.MEMORY, Config.YING)


@st.cache_resource
def get_yi():
    return Agent(Config.YI_SYSTEM_PROMPT, Config.MEMORY, Config.YI)


def main():
    options = ["小樱", "易大师"]
    selected_option = st.sidebar.selectbox("请选择角色", options)

    if selected_option == "小樱":
        agent = get_ying()
        chat_history = "ying_history"
    else:
        agent = get_yi()
        chat_history = "yi_history"

    if chat_history not in st.session_state:
        st.session_state[chat_history] = []
    else:
        for message in st.session_state[chat_history]:
            if message["role"] == 'user':
                st.chat_message('user').text(message["content"])
            else:
                st.chat_message('assistant').text(message["content"])

    if user_query := st.chat_input("请输入你的问题："):
        st.chat_message('user').text(user_query)
        st.session_state[chat_history].append(
            {"role": "user", "content": user_query})

        with st.spinner("正在思考中..."):
            response = agent.invoke(user_query)
        print(response)

        st.chat_message('assistant').text(response)
        st.session_state[chat_history].append(
            {"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
