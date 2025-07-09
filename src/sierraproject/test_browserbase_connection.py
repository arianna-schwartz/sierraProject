import asyncio
from stagehand import Stagehand
import logging

# Enable detailed logging
logging.basicConfig(level=logging.DEBUG)

async def test_browserbase_connection():
    try:
        config = {
            "env": "BROWSERBASE",
            "apiKey": "bb_live_V1Ze7mz6s4pL6E-jjPtF9AORRp4",
            "projectId": "a815daa8-d671-4e8a-a93c-ee5e33eaf2d2",
            "domSettleTimeoutMs": 30000,
            "browserbaseSessionCreateParams": {
                "projectId": "a815daa8-d671-4e8a-a93c-ee5e33eaf2d2"
            },
            "enableCaching": True,
            "useAPI": True  # Changed to True to use Browserbase API
        }
        
        print("Initializing Stagehand...")
        stagehand = await Stagehand.create(config)
        
        print("Testing browser connection...")
        await stagehand.goto("https://www.google.com")
        
        print("Connection successful!")
        
        # Clean up
        await stagehand.close()
        
    except Exception as e:
        print(f"Error during connection test: {str(e)}")
        raise

if __name__ == "__main__":
    asyncio.run(test_browserbase_connection())
