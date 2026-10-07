from fastapi.testclient import TestClient
from main import app
client=TestClient(app)
def test_health():assert client.get("/health").json()=={"status":"ok"}
def test_assessment_names_blockers():
 data=client.post("/assess",json={"sku_id":"maple-granola","evidence_ids":["gs1","label","case"],"case_units":6,"lead_days":21}).json();assert data["ready"] is False and [x["id"] for x in data["blockers"]]==["allergen","coa"] and data["submission"]=="founder_review_only"
def test_complete_assessment():
 data=client.post("/assess",json={"sku_id":"maple-granola","evidence_ids":["gs1","label","formula","lab","case"],"case_units":6,"lead_days":21}).json();assert data["ready"] is True and data["evidenced"]==data["total"]==5
def test_unknown_sku_is_404():assert client.post("/assess",json={"sku_id":"missing","case_units":6,"lead_days":21}).status_code==404
def test_unknown_evidence_is_explicit():
 response=client.post("/assess",json={"sku_id":"maple-granola","evidence_ids":["invented"],"case_units":6,"lead_days":21});assert response.status_code==422 and response.json()["detail"]["unknown_evidence"]==["invented"]
def test_invalid_pack_values_rejected():assert client.post("/assess",json={"sku_id":"maple-granola","case_units":0,"lead_days":181}).status_code==422
