from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

import sys

class VerificationCodeInput(BaseModel):
    prompt: str = Field(
        default="Please enter the verification code from your email:",
        description="The prompt to show to the user when requesting the verification code"
    )

class VerificationCodeInputTool(BaseTool):
    name: str = "Verification Code Input Tool"
    description: str = "Tool for getting verification code input from the user"
    args_schema: Type[BaseModel] = VerificationCodeInput

    def _run(self, prompt: str) -> str:
        """Run the tool to get verification code input from the user."""
        print("\n" + "="*50)
        print("Code: ")
        print("="*50)
        # verification_code = input(f"{prompt}\nVerification Code: ")
        verification_code = sys.stdin.readline().strip().replace("-", "")
        print("="*50 + "\n")
        return verification_code
