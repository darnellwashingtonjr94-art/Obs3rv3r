from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def broadcast_agent_status(self, message: dict):
        for connection in self.active_connections:
            await connection.send_json(message)
