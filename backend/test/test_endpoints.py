from app.config import Config


def test_get_me(client):
    response = client.get("/me")
    assert response.status_code == 200
    data = response.json()
    assert data["telegram_user_id"] == 123456789


def test_send_code(client):
    payload = {"phone_number": Config.MY_PHONE}
    response = client.post("/auth/send-code", json=payload)
    assert response.status_code == 200
    json_response = response.json()
    print(json_response)
    assert json_response.get("success")
    assert "data" in json_response
    assert "phone_code_hash" in json_response["data"]
