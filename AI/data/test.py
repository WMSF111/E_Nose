import os
from dotenv import load_dotenv, find_dotenv
from langchain.vectorstores.chroma import Chroma
from ZHIPU.zhipuai_embedding import ZhipuAIEmbeddings
from zhipuai import ZhipuAI

# 读取本地/项目的环境变量。
_ = load_dotenv(find_dotenv())

client = ZhipuAI(
    api_key=os.environ["ZHIPUAI_API_KEY"]
)

# 定义 Embeddings
embedding = ZhipuAIEmbeddings()

# 向量数据库持久化路径
persist_directory = './chroma'

# 加载数据库
vectordb = Chroma(
    persist_directory=persist_directory,  # 允许我们将persist_directory目录保存到磁盘上
    embedding_function=embedding
)
print(f"向量库中存储的数量：{vectordb._collection.count()}")

question = "电子鼻在牛乳中的应用?"

docs = vectordb.similarity_search(question,k=3)
print(f"检索到的内容数：{len(docs)}")

for i, doc in enumerate(docs):
    print(f"检索到的第{i}个内容: \n {doc.page_content}", end="\n-----------------------------------------------------\n")

# 核心思想是在已经选择了一个相关性高的文档之后，再选择一个与已选文档相关性较低但是信息丰富的文档。
# mmr_docs = vectordb.max_marginal_relevance_search(question,k=3)
# for i, sim_doc in enumerate(mmr_docs):
#     print(f"MMR 检索到的第{i}个内容: \n{sim_doc.page_content[:200]}", end="\n--------------\n")


