from pydantic import BaseModel
from typing import List, Optional

class Royalty(BaseModel):
    rate: Optional[float]
    basis: Optional[str]
    evidence: Optional[str]

class IPLicense(BaseModel):
    license_id: str
    territory: List[str]
    term: Optional[str]
    royalty: Royalty
    sub_licensing: Optional[bool]
    status: str
