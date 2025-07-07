# import os
# from stagehand import Stagehand, StagehandConfig

# # Test credentials
# config = StagehandConfig(
#     env="BROWSERBASE",
#     api_key=os.getenv("BROWSERBASE_API_KEY"),
#     project_id=os.getenv("BROWSERBASE_PROJECT_ID"),
# )

# try:
#     stagehand = Stagehand(config)
#     print("Configuration appears valid")
# except Exception as e:
#     print(f"Configuration error: {e}")