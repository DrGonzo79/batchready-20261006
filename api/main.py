import json
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
app=FastAPI(title="BatchReady assessment API",version="0.1.0")
FIXTURE=json.loads((Path(__file__).parents[1]/"data"/"demo_brands.json").read_text())
SKUS={sku["id"]:sku for brand in FIXTURE["brands"] for sku in brand["skus"]};EVIDENCE={item["id"] for item in FIXTURE["evidence"]}
class AssessmentRequest(BaseModel):
    sku_id:str=Field(min_length=1,max_length=80);evidence_ids:list[str]=Field(default_factory=list,max_length=20);case_units:int=Field(ge=1,le=200);lead_days:int=Field(ge=1,le=180)
@app.get("/health")
def health()->dict[str,str]:return {"status":"ok"}
@app.post("/assess")
def assess(request:AssessmentRequest)->dict:
    sku=SKUS.get(request.sku_id)
    if not sku:raise HTTPException(status_code=404,detail="SKU not found")
    unknown=sorted(set(request.evidence_ids)-EVIDENCE)
    if unknown:raise HTTPException(status_code=422,detail={"unknown_evidence":unknown})
    supplied=set(request.evidence_ids);requirements=[{**item,"status":"evidenced" if item["evidence"] in supplied else "blocked"} for item in sku["requirements"]];blockers=[item for item in requirements if item["status"]=="blocked"]
    return {"sku_id":sku["id"],"ready":not blockers,"evidenced":len(requirements)-len(blockers),"total":len(requirements),"blockers":blockers,"case_pack":{"units":request.case_units,"lead_days":request.lead_days},"submission":"founder_review_only","disclaimer":"Fictional readiness assessment; not regulatory or retailer approval."}
