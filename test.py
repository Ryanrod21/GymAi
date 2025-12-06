import asyncio
from agents import Agent, Runner 
from dotenv import load_dotenv

load_dotenv()


async def testagent(txt: str):
    instructions = f"Rank this {txt} from 1 - 10"
    agent = Agent(
        name="TestAgent",
        instructions=instructions,
        model="gpt-4o-mini"
    )
    result = await Runner.run(agent, txt)
    return result.final_output

print(asyncio.run(testagent("bench press")))
