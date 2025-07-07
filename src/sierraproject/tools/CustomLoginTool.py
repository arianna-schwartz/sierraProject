# custom_login_tool.py
from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from crewai_tools import StagehandTool
from stagehand.schemas import AvailableModel
from sierraproject.tools.stagehand_client import stagehand_tool

# for loading in env variables
import os 
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# define the type of input the tool expects 
class LoginToolInput(BaseModel):
    email: str = Field(..., description="Sierra dashboard login email")

# defining the logic of the tool
class CustomLoginTool(BaseTool):
    name: str = "Sierra Login Tool"
    description: str = (
        "Logs into the Madison Reed Sierra dashboard using provided credentials."
    )

    args_schema: Type[BaseModel] = LoginToolInput
    
    def _run(self, email: str) -> str:
        try:
            # Using run() with the action as part of the instruction
            result1 = stagehand_tool.run(
                instruction = "Click the email field and input the email {email}. Then click the sign in button.",
                url="https://madison-reed.sierra.ai/"
            )

            print("RESULT 1: " + str(result1))
            return str(result1) # right now this step isn't sucessful
            

        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return f"An error occurred: {str(e)}"
        finally:
            stagehand_tool.close()