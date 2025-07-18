import os
from typing import List

from crewai import LLM, Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task
from crewai.tasks.llm_guardrail import LLMGuardrail
from dotenv import load_dotenv
from pydantic import BaseModel

from sierraproject.tools.mcp_config import get_stagehand_mcp_tools
from sierraproject.tools.verification_code_input_tool import VerificationCodeInputTool

# Load environment variables
load_dotenv()


class SierraInformation(BaseModel):
    category: str
    count: str
    summary: str


class SierraInformations(BaseModel):
    list_of_apartments: list[SierraInformation]


@CrewBase
class SierraCrew:
    """Sierra Login Crew"""

    llm = LLM(
        model="gpt-4.1",
        temperature=0.1,
    )

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    agents: List[BaseAgent]
    tasks: List[Task]
    mcp_adapter = None
    tools = []

    def __init__(self):
        """Initialize the crew with MCP tools."""
        # Load environment variables
        load_dotenv()

        # Initialize MCP adapter
        self.mcp_adapter = get_stagehand_mcp_tools()
        self.tools = self.mcp_adapter.tools

        # Add verification code input tool to tools list
        verification_tool = VerificationCodeInputTool()
        self.tools.append(verification_tool)

        print(
            f">>> Available tools from Stagehand MCP server: {[tool.name for tool in self.tools]}"
        )

    # @agent
    # def login_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config["login_agent"],  # type: ignore[index]
    #         tools=self.tools,
    #         verbose=True,
    #     )

    # @agent
    # def filter_statuses_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config["filter_statuses_agent"],  # type: ignore[index]
    #         tools=self.tools,
    #         verbose=True,
    #         temperature=0.1,  # Adding low temperature for more precise, deterministic behavior
    #         reasoning=True,  # Enable reasoning for better decision-making
    #         planning=True  # Enable planning for better task execution
    #     )

    # @agent
    # def get_first_convo_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config["get_first_convo_agent"],  # type: ignore[index]
    #         tools=self.tools,
    #         verbose=True,
    #         temperature=0.5,  # Adding low temperature for more precise, deterministic behavior
    #         reasoning=True,  # Enable reasoning for better decision-making
    #         planning=True
    # )

    @agent
    def sierra_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["sierra_agent"],  # type: ignore[index]
            tools=self.tools,
            verbose=True,
            reasoning=False,  # Temporarily disable reasoning to avoid the error
            llm=self.llm,
        )

    # @task
    # def login_to_sierra(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["login_to_sierra"],  # type: ignore[index]
    #         # human_input= True,
    #     )

    # @task
    # def get_first_problem_convo(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["get_first_problem_convo"],  # type: ignore[index]
    #     )

    # @task
    # def filter_statuses(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["filter_statuses"],  # type: ignore[index]
    #     )

    # @task
    # def get_first_convo(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["get_first_convo"],  # type: ignore[index]
    #     )

    @task
    def analyze_sierra_conversations(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_sierra_conversations"],  # type: ignore[index]
            # human_input= True,
            output_pydantic=SierraInformations,
            guardrail=[
                LLMGuardrail(
                    description="Ensure that the agent waited for the response, the response contains all the rows from the table and columns requested as part of the pydantic output",
                    llm=self.llm,
                )
            ],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Login Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            planning=True,
        )
