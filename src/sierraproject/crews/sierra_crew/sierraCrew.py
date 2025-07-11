import os
from typing import List

from crewai import Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv

from sierraproject.tools.mcp_config import get_stagehand_mcp_tools
from sierraproject.tools.verification_code_input_tool import VerificationCodeInputTool

# Load environment variables
load_dotenv()

# one tool for taking screen shots of conversations
# one tool for analyzing screenshots to read the conversations - vision_tool()


@CrewBase
class SierraCrew:
    """Sierra Login Crew"""

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
        
        print(f">>> Available tools from Stagehand MCP server: {[tool.name for tool in self.tools]}")

    @agent
    def login_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["login_agent"],  # type: ignore[index]
            tools=self.tools,
            verbose=True,
        )

    # @agent 
    # def get_first_problem_convo_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config["get_first_problem_convo_agent"],  # type: ignore[index]
    #         tools=self.tools,
    #         verbose=True,
    #     )

    @agent
    def filter_statuses_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["filter_statuses_agent"],  # type: ignore[index]
            tools=self.tools,
            verbose=True,
        )
    
    # @agent
    # def check_filters_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config["check_filters_agent"],  # type: ignore[index]
    #         tools=self.tools,
    #         verbose=True,
    #     )

    @agent
    def dropdown_check_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["dropdown_check_agent"],  # type: ignore[index]
            tools=self.tools,
            verbose=True,
        )

    # @agent
    # def summarize_convo_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config["summarize_convo_agent"],  # type: ignore[index]
    #         tools=self.tools,
    #         verbose=True,
    #     )
    
    # @agent 
    # def verify_page_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config["verify_page_agent"],  # type: ignore[index]
    #         tools=self.tools,
    #         verbose=True,
    #     )


    # @agent 
    # def click_out_of_filters_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config["click_out_of_filters_agent"],  # type: ignore[index]
    #         tools=self.tools,
    #         verbose=True,
    #     )
    
    # @agent
    # def get_first_convo_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config["get_first_convo_agent"],  # type: ignore[index]
    #         tools=self.tools,
    #         verbose=True,
    #     )

    @task
    def login_to_sierra(self) -> Task:
        return Task(
            config=self.tasks_config["login_to_sierra"],  # type: ignore[index]
            # human_input= True,
        )

    # @task
    # def get_first_problem_convo(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["get_first_problem_convo"],  # type: ignore[index] 
    #     )


    @task
    def filter_statuses(self) -> Task:
        return Task(
            config=self.tasks_config["filter_statuses"],  # type: ignore[index]
        )
    
    # @task
    # def check_filters(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["check_filters"],  # type: ignore[index]
    #     )
    # @task
    # def verify_page(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["verify_page"],  # type: ignore[index]
    #     )

    # @task
    # def click_out_of_filters(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["click_out_of_filters"],  # type: ignore[index]
    #     )

    # @task
    # def get_first_conversation(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["get_first_convo"],  # type: ignore[index]
    #     )

    # @task
    # def summarize_convo(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["summarize_convo"],  # type: ignore[index]
    #     )

    @task
    def dropdown_check(self) -> Task:
        return Task(
            config=self.tasks_config["dropdown_check"],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Login Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

