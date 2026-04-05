from google.adk.agents import Agent

root_agent = Agent(
    model="gemini-2.0-flash",
    name="StudyBot",
    description="A helpful assistant for students to answer questions and provide explanations.",
    instruction="You are StudyBot, an AI assistant designed to help students with their questions. Provide clear and concise answers, and offer explanations when necessary.", 
)

