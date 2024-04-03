import asyncio
import semantic_kernel as sk
from semantic_kernel import KernelArguments
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.contents.chat_history import ChatHistory

import prompts

kernel = sk.Kernel()

deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
service_id = "default"
kernel.add_service(
    AzureChatCompletion(service_id=service_id, deployment_name=deployment, endpoint=endpoint, api_key=api_key),
)


# Define the request settings
req_settings = kernel.get_service(service_id).get_prompt_execution_settings_class()(ai_model_id=service_id)
req_settings.max_tokens = 2000
req_settings.temperature = 0.7
req_settings.top_p = 0.8


chat_history = ChatHistory()


# Run your prompt
# Note: functions are run asynchronously
async def main():
    
    prompt_template_config = sk.PromptTemplateConfig(
        template=prompts.SETUP_PROMPT,
        name="tldr",
        template_format="semantic-kernel",
        execution_settings=req_settings,
    )
    function = kernel.create_function_from_prompt(
        function_name="tldr_function",
        plugin_name="tldr_plugin",
        prompt_template_config=prompt_template_config,
    )

    arguments = KernelArguments(interest1="space exploration")

    response = await kernel.invoke(function,  arguments)
    chat_history.add_assistant_message(str(response))
    print(response)
    

    #arguments = KernelArguments(user_input="Can you repeat what I asked the first time?", history=chat_history)
    #response = await kernel.invoke(function,  arguments)
    #chat_history.add_assistant_message(str(response))

    #print(response) # => Robots must not harm humans.

if __name__ == "__main__":
    asyncio.run(main())