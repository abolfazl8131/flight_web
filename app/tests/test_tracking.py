from app.api.tracking import apps
from fastapi.testclient import TestClient


client = TestClient(apps.app)


def test_create_message():
    response = client.post("/track",json={"Code":"754535"})
    
    assert response.status_code == 200
   

    


    