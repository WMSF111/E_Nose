import os
from dotenv import load_dotenv, find_dotenv
from langchain.document_loaders.pdf import PyMuPDFLoader
from langchain.document_loaders.markdown import UnstructuredMarkdownLoader

# 读取本地/项目的环境变量。
_ = load_dotenv(find_dotenv())

# 获取folder_path下所有文件路径，储存在file_paths里
file_paths = []
folder_path = 'knowledge_db'
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_paths.append(file_path)
print(file_paths[:3])

# 遍历文件路径并把实例化的loader存放在loaders里
loaders = []

for file_path in file_paths:

    file_type = file_path.split('.')[-1]
    if file_type == 'pdf':
        loaders.append(PyMuPDFLoader(file_path))
    elif file_type == 'md':
        loaders.append(UnstructuredMarkdownLoader(file_path))

# 下载文件并存储到text
texts = []

for loader in loaders: texts.extend(loader.load())
text = texts[1]
# print(f"每一个元素的类型：{type(text)}.",
#     f"该文档的描述性数据：{text.metadata}",
#     f"查看该文档的内容:\n{text.page_content[0:]}",
#     sep="\n------\n")

from langchain.text_splitter import RecursiveCharacterTextSplitter

# 切分文档
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, chunk_overlap=50)

split_docs = text_splitter.split_documents(texts)

# 使用我们自己封装的智谱 Embedding，需要将封装代码下载到本地使用
from ZHIPU.zhipuai_embedding import ZhipuAIEmbeddings

# 定义 Embeddings
embedding = ZhipuAIEmbeddings()

# 定义持久化路径
persist_directory = './chroma'

import shutil
# 检查文件夹是否存在，如果存在则删除
if os.path.exists(persist_directory):
    shutil.rmtree(persist_directory)
    print(f"文件夹 '{persist_directory}' 已被删除。")
else:
    print(f"文件夹 '{persist_directory}' 不存在。")

from langchain.vectorstores.chroma import Chroma

vectordb = Chroma.from_documents(
    documents=split_docs[:20], # 为了速度，只选择前 20 个切分的 doc 进行生成；使用千帆时因QPS限制，建议选择前 5 个doc
    embedding=embedding,
    persist_directory=persist_directory  # 允许我们将persist_directory目录保存到磁盘上
)
#来持久化向量数据库
vectordb.persist()
print(f"向量库中存储的数量：{vectordb._collection.count()}")





