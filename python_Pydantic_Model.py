###python

from pydantic import BaseModel, HttpUrl
from typing import List, Union, Optional

class Attribute(BaseModel):
    trait_type: str
    value: Union[str, int, float, bool]

class MintingInfo(BaseModel):
    chain: Optional[str]
    contract_address: Optional[str]
    token_id: Optional[Union[str, int]]
    transaction_hash: Optional[str]

class RogueMetadata(BaseModel):
    name: str
    description: str
    image: HttpUrl
    animation_url: Optional[HttpUrl] = None
    attributes: List[Attribute]
    unlockable_content_ipfs: Optional[HttpUrl] = None
    external_url: Optional[HttpUrl] = None
    tags: Optional[List[str]] = []
    metadata_version: str
    prompt_version: str
    minting: Optional[MintingInfo] = None
    created_at: Optional[str] = None
