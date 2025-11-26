from google.adk.sessions import InMemorySessionService
import uuid

class SessionStore:
    """
    Wrapper around ADK's InMemorySessionService to manage session state.
    """
    def __init__(self):
        self.service = InMemorySessionService()
        self.session_id = str(uuid.uuid4())
        self.user_id = "user" # Default user
        self.app_name = "enterprise_analyst"

    async def initialize(self):
        await self.service.create_session(
            app_name=self.app_name,
            user_id=self.user_id,
            session_id=self.session_id
        )

    def get_service(self):
        return self.service

    def get_session_id(self):
        return self.session_id
