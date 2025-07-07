from crewai import Agent, Task, Crew
from crewai_tools import StagehandTool
from stagehand.schemas import AvailableModel

# Initialize the tool with API keys
stagehand_tool = StagehandTool(
    api_key="XXX",
    project_id="a815daa8-d671-4e8a-a93c-ee5e33eaf2d2",
    model_api_key="XXX",
    model_name="gpt-4o"
)

# Create an agent with the tool
researcher = Agent(
    role="Web Researcher",
    goal="Find and summarize information from websites",
    backstory="I'm an expert at finding information online.",
    verbose=True,
    tools=[stagehand_tool],
)

# Create a task that uses the tool - right now I want to just get a simple task working
research_task = Task(
    description="Go to https://madison-reed.sierra.ai/ and tell me what you see on the homepage using the 'observe' action of stagehand.",
    agent=researcher,
    expected_output="State the color of the company logo as seen on the homepage.",
)

# Run the crew
crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=True,
)

result = crew.kickoff()
stagehand_tool.close()
print(result)


