import asyncio
from agents import Agent, Runner 
from dotenv import load_dotenv

load_dotenv()


async def testagent(days, goal, train):
    instructions = f"Make a short sentence using {days}, {goal}, {train}"
    
    agent = Agent(
        name="TestAgent", 
        instructions=instructions, 
        model="gpt-4o-mini"),
    
    result = await Runner.run(agent, days=days, goal=goal, train=train),

    return result.final_output


