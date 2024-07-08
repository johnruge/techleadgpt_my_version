import os
import sys
import openai
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.indexes.vectorstore import VectorStoreIndexWrapper, VectorstoreIndexCreator
from langchain_community.vectorstores import Chroma
import constants

os.environ["OPENAI_API_KEY"] = constants.APIKEY

# Enable to save to disk & reuse the model (for repeated queries on the same data)
PERSIST = False

query = None
if len(sys.argv) > 1:
    query = sys.argv[1]

# Initialize the embeddings
embeddings = OpenAIEmbeddings()

if PERSIST and os.path.exists("persist"):
    print("Reusing index...\n")
    vectorstore = Chroma(persist_directory="persist", embedding_function=embeddings)
else:
    loader = TextLoader("data/data.txt")
    vectorstore = Chroma(embedding_function=embeddings)  # Initialize Chroma with embeddings

    # Create the index
    index = VectorstoreIndexCreator(embedding=embeddings).from_loaders([loader])

chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)

chat_history = []
while True:
    if not query:
        query = input("Prompt: ")
    if query in ['quit', 'q', 'exit', 'exit ', 'quit ', 'q ', '']:
        sys.exit()
    result = chain({"question": query, "chat_history": chat_history})
    print(result['answer'])

    chat_history.append((query, result['answer']))
    query = None
