import asyncio
from langgraph_system.graph_creation import graph

async def continue_graph_execution(messages):
    async for state in graph.astream({"messages": messages}, config={}):
        # Handle the state as needed in the graph
        current_state = state.asdict()
        print(f"Current State: {current_state}")
        # Check for message updates
        if 'messages' in current_state:
            message_state = current_state.get('messages')[-1]  # Get the latest message
            print(f"Latest Message: {message_state}")
        else:
            print("Key 'messages' not found in state, skipping message update.")

async def main():
    student_id = input("Enter your user ID: ")
    messages = [{"student_id": student_id}]
    
    # Start the graph execution with the student ID included
    await continue_graph_execution(messages)

if __name__ == "__main__":
    asyncio.run(main())
