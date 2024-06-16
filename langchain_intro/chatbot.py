import dotenv
import os
from langchain_huggingface import HuggingFaceEndpoint

#Loading the environment variables
dotenv.load_dotenv()

token = os.getenv("HUGGINGFACE_TOKEN")

#Initializing the chat model
chatModel = HuggingFaceEndpoint(repo_id="meta-llama/Meta-Llama-3-8B-Instruct", max_length=128,temperature=0.7,token=token)
print(chatModel.invoke("What is machine learning"))
