from typing import List

from fastapi import FastAPI

from character_model.character import Character
from character_model.simulation import DndSimulation

app = FastAPI()


@app.get("/getCharacters")
async def get_characters():
    characters: List[Character] = DndSimulation().get_characters()
    return [repr(character) for character in characters]


@app.get("/health")
async def health():
    return {"message": "I am alive"}
