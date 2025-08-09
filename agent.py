from langchain_community.embeddings import ZhipuAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from config import Config


class Agent:
    def __init__(self, system_prompt, memory_path, name):
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
        )

        llm = ChatOpenAI(model_name=Config.OPENAI_MODEL_NAME,
                         openai_api_base=Config.OPENAI_API_BASE,
                         openai_api_key=Config.OPENAI_API_KEY)

        self.embedding = ZhipuAIEmbeddings(
            api_key=Config.ZHIPUAI_API_KEY,
            model=Config.ZHIPUAI_MODEL
        )

        self.memory = Chroma(
            persist_directory=memory_path,
            embedding_function=self.embedding,
        )

        self.name = name

        self.model = prompt | llm

    def retrieve_from_memory(self, query):
        docs = self.memory.similarity_search(query, k=5)

        return [doc.page_content for doc in docs]

    def invoke(self, query):
        try:
            related_chat_history = self.retrieve_from_memory(query)

            final_input = f"""
                ---中的内容是用户的问题：
                ---
                {query}
                ---
                
                你也可以参考历史对话记录回答问题。
                ```中的内容是历史对话记录:
                ```
                {related_chat_history}
                ```
            """

            print("final_input:", final_input, end="\n\n")

            response = self.model.invoke({"input": final_input})
            final_res = response.content

            chat_history = f"""
                "历史问题": {query}
                "历史回答": {final_res}
                "回答人": {self.name}
            """

            self.memory.add_texts(texts=[chat_history])

            return final_res
        except Exception as e:
            return f"我无法回答这个问题 ({e})"
