import argparse
import asyncio

from app import jsonConfig
from autogen import UserProxyAgent
from autogen.agentchat.contrib.multimodal_conversable_agent import MultimodalConversableAgent
from playwright.async_api import async_playwright


# Get json
config = jsonConfig.Json()
OPENAI_API_KEY = config.readConfig("config.json", "OPENAI_API_KEY")
OPENAI_API_BASE = config.readConfig("config.json", "OPENAI_API_BASE")
MODEL = config.readConfig("config.json", "MODEL")
SEED = config.readConfig("config.json", "SEED")
TEMPERATURE = config.readConfig("config.json", "TEMPERATURE")
TIMEOUT = config.readConfig("config.json", "TIMEOUT")


# The prompt
prompt = """
Describe this screenshot as best as possible: <img input.png>
"""


# The main function
async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="URl that will be analyzed")

    args = parser.parse_args()

    if not args.url:
        print("Please provide a link (ex. https://google.com)")
        return

    async with async_playwright() as p:
        browser = await p.chromium.launch()

        page = await browser.new_page()
        await page.goto(args.url)
        await page.screenshot(path='input.png', full_page=True)
        await browser.close()

    config_list = [
        {
            "base_url": OPENAI_API_BASE,
            "api_key": OPENAI_API_KEY,
            "model": MODEL
        }
    ]

    llm_config = {
        "config_list": config_list,
        "cache_seed": None,
        "temperature": TEMPERATURE,
        "max_tokens": -1,
        "timeout": TIMEOUT
    }

    image_agent = MultimodalConversableAgent(
        name="Image-Explainer",
        llm_config=llm_config
    )

    user = UserProxyAgent(
        name="User",
        # human_input_mode="ALWAYS",
        human_input_mode="ALWAYS",
        is_termination_msg=lambda x: x.get(
            "content", "").rstrip().endswith("TERMINATE"),
        code_execution_config={
            "work_dir": "coding",
            "use_docker": False
        }
    )

    user.initiate_chat(
        recipient=image_agent,
        message=prompt,
        silent=False
    )

    # json.dump(user.chat_messages[image_agent], open("conversations.json", "w"), indent=2)


if __name__ == "__main__":
    asyncio.run(main())
