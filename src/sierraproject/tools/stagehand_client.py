import os
from crewai_tools import StagehandTool
from dotenv import load_dotenv

load_dotenv()

stagehand_tool = StagehandTool(
    api_key=os.getenv("BROWSERBASE_API_KEY"),
    project_id=os.getenv("BROWSERBASE_PROJECT_ID"),
    model_api_key=os.getenv("OPENAI_API_KEY"),
    model_name=os.getenv("LLM_MODEL"),
)
