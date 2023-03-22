from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_name_Theetach():
    name= "Theetach"
    url=f"/callname/{name}"
    expected_result ={"hello" : name}
    actual_result = client.get(url)
    assert actual_result.status_code == 200
    assert actual_result.json() == expected_result
    
def test_post_name_junior():
    response = client.post("/callname")
    assert response.status_code == 200
    assert response.json() == {"hello" : "junior"}
