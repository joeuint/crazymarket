import json
import os
import openai
from dataclasses import asdict, dataclass
from enum import Enum
from typing import TYPE_CHECKING


class EventType(Enum):
    COLLAPSE = "collapse"
    BOOM = "boom"

@dataclass
class StockDescription:
    name: str
    biography: str
    beforePrice: int

@dataclass
class Event:
    event_type: EventType
    stock: StockDescription
    dollar_impact: int


class EventsManager:
    def __init__(self):
        self.openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def dispatch_event(self, event: Event):
        msg = json.dumps(asdict(event), default=str)
        print(msg)
        
        response = self.openai_client.responses.create(
            model=os.getenv("OPENAI_API_MODEL", "gpt-4.1"),
            prompt={
                "id": os.getenv("OPENAI_API_PROMPT", ""),
                "version": os.getenv("OPENAI_API_PROMPT_VERSION", "5"),
            },
            input=msg
        )

        text = response.output_text
        print(text)
