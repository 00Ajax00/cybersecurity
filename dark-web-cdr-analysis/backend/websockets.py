# backend/websockets.py
from fastapi import WebSocket, WebSocketDisconnect
from typing import List

class WebSocketManager:
    def __init__(self):
        self.connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)

    async def broadcast(self, message: str):
        for connection in self.connections:
            await connection.send_text(message)

manager = WebSocketManager()
