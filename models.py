from pydantic import BaseModel
from typing import List, Optional, Union

class JinaRerankerResult(BaseModel):
    index: int
    relevance_score: float
    document: Union[str, dict, None] = None

class JinaRerankerResponse(BaseModel):
    model: str
    usage: dict
    results: List[JinaRerankerResult]

class JinaRerankerRequest(BaseModel):
    query: str
    documents: List[str]
    top_n: Optional[int] = None
    return_documents: bool = True
    batch_size: int = 64
