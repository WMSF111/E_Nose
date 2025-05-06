import os
from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(
    temperature=0.95,
    model="glm-4",
    openai_api_key="a9c854d12d28f483ece072f2772da3a5.kqGuOiY1O5x5tbYm",
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)
# 创建聊天提示模板
prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "你被用于对电子鼻数据的分析，所给的数据是经过分析方法进行分析后，并且进行训练后的结果。"
        ), # 定义机器人的角色或任务。
        # 用于插入之前的聊天记录。
        # MessagesPlaceholder(variable_name="chat_history"),
        # 定义用户提问的格式。
        HumanMessagePromptTemplate.from_template("请根据以下格式进行回复："
                                    "1.{An_M}分析方法的准确率是多少。"
                                    "2.{AAA}分析方法得出的数据具有什么含义")
    ]
)
# 用于存储和管理对话历史，以便模型能够参考之前的对话。
# memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# 将语言模型、提示和记忆结合在一起，处理对话。
# conversation = llm|prompt
conversation = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    # memory=memory
)
# 向聊天机器人发送一个问题（在这个例子中是“讲个笑话”），并触发对话。
respond = conversation.invoke({"An_M": "pca", "AAA": "BBB"})
print(respond)
