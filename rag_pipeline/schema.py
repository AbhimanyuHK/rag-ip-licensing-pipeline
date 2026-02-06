from pydantic import BaseModel
from typing import List, Optional

class Royalty(BaseModel):
    rate: Optional[float]
    basis: Optional[str]
    evidence: Optional[str]

class IPLicense(BaseModel):
    license_id: str
    licensor: Optional[str]
    licensee: Optional[str]
    ip_assets: List[str]
    territory: List[str]
    term_start: Optional[str]
    term_end: Optional[str]
    royalty: Royalty
    sub_licensing: Optional[bool]
    restrictions: List[str]
    status: str
