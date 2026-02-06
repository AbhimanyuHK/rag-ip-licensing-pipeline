import json
from schema import IPLicense
from pydantic import ValidationError

def parse_and_validate(llm_output: str) -> IPLicense:
    try:
        data = json.loads(llm_output)
        return IPLicense(**data)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON returned by LLM")
    except ValidationError as e:
        raise ValueError(f"Schema validation failed: {e}")
