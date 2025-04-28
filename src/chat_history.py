from typing import List,Dict
from langchain_ollama import ChatOllama
from langchain_core.messages import (
  HumanMessage,
  AIMessage,
  BaseMessage
)
from langchain_core.prompts import (
  ChatMessagePromptTemplate,
  MessagesPlaceholder
) 



class ChatHistory:
  def __init__(self):
    ... 
  
  def _simple_query(self,query:str,modify_query:bool = False) -> str:
    ... 


class RAG:
  ...
