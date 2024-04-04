# Choose the LLM that will drive the agent
# Only certain models support this
import os

from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.chat_models import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.prompts.chat import SystemMessagePromptTemplate
from langchain_core.messages import HumanMessage, AIMessage

import image_utils
import prompts

llm = AzureChatOpenAI(
    openai_api_version="2023-05-15",
    azure_deployment=os.environ['AZURE_OPENAI_DEPLOYMENT_NAME'],
    temperature=0
)
MEMORY_KEY = "chat_history"

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a tutor that assists student learning through framing student's math problem in relation to their interest",
        ),
        MessagesPlaceholder(variable_name=MEMORY_KEY),
        SystemMessagePromptTemplate.from_template(
            prompts.SETUP_PROMPT
        ),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)
tools = [modelutils.generate_image]

agent = create_openai_tools_agent(llm, tools, prompt)


agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

chat_history = []


def agent_run(user_input, interest):
    result = agent_executor.invoke({"input": user_input, "interest": interest, "chat_history": chat_history})
    chat_history.extend(
        [
            HumanMessage(content=user_input),
            AIMessage(content=result["output"]),
        ]
    )

    return result["output"]


if __name__ == "__main__":
    input = "Integrate 2*x^3"


    print(agent_executor.invoke({"input": "I have a follow up question", "interest": "Farming", "chat_history": chat_history}))


