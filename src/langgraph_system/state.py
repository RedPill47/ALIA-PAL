import asyncio

class MessageState:
    """
    A class to manage the state of messages and events for asynchronous communication.
    """

    def __init__(self):
        self.content = "-"
        self.agent_name = "-"
        self.event = asyncio.Event()
        self.user_input_event = asyncio.Event()
        self.acknowledgment_event = asyncio.Event()
        self.user_input = ""

    async def wait_for_update(self):
        """
        Waits for the event to be set, indicating that the message content has been updated.
        """
        await self.event.wait()
        self.event.clear()
        return {"content": self.content, "agent_name": self.agent_name}

    def update_content(self, new_content, new_agent_name):
        """
        Updates the message content and agent name, and sets the event to notify waiting coroutines.
        """
        self.content = new_content
        self.agent_name = new_agent_name
        self.event.set()
        print('Successfully updated content!')

    async def wait_for_input(self):
        """
        Waits for the user input event to be set, indicating that user input has been received.
        """
        await self.user_input_event.wait()
        self.user_input_event.clear()
        return self.user_input

    def update_user_input(self, user_input):
        """
        Updates the user input and sets the user input event to notify waiting coroutines.
        """
        self.user_input = user_input
        self.user_input_event.set()

    async def wait_for_acknowledgment(self):
        """
        Waits for the acknowledgment event to be set, indicating that the message has been acknowledged.
        """
        await self.acknowledgment_event.wait()
        self.acknowledgment_event.clear()

    def acknowledge_message(self):
        """
        Sets the acknowledgment event to indicate that the message has been acknowledged.
        """
        self.acknowledgment_event.set()

# Create an instance of MessageState to manage the message state globally.
message_state = MessageState()
