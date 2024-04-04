# Choose the LLM that will drive the agent
# Only certain models support this
import os
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)

#from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.agents import AgentExecutor, Agent
from langchain.chat_models import ChatOpenAI, AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.prompts.chat import BaseMessagePromptTemplate, SystemMessagePromptTemplate

import modelutils
import prompts

llm = AzureChatOpenAI(
    openai_api_version="2023-05-15",
    azure_deployment=os.environ['AZURE_OPENAI_DEPLOYMENT_NAME']
)

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(
            prompts.SETUP_PROMPT
        ),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)
tools = [modelutils.generate_image]

llm_with_tools = llm.bind_tools(tools)


agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_tool_messages(
            x["intermediate_steps"]
        ),
    }
    | prompt
    | llm_with_tools
    | OpenAIToolsAgentOutputParser()
)


agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
