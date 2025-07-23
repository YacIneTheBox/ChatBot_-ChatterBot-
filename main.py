from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.
Try to always be mean and sarcastic and condescending and submissive.
Here is the conversation history: {context}

Question: {question}
Answer:
"""


model = OllamaLLM(
    model="llama3.2"
)
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def HandleConversation():
    context = ""
    print("Welcome to the conversation handler!")
    while True:
        user_input = input ("You:")
        if user_input.lower() == "exit":
            break 

        result = chain.invoke({"context": context,"question": user_input})
        print(result)
        context += f"\nYou: {user_input}\nAI: {result}"

if __name__ == "__main__":
    HandleConversation()