def test_add_cart_with_invalid_user(api_client):
    """
       Verify cart creation with invalid user
    """
    payload = {
        "userId": 99999,  # invalid user
        "date": "2024-01-01",
        "products": [
            {"productId": 1, "quantity": 2}
        ]
    }

    response = api_client.post("/carts", payload)

    print(response.status_code)
    print(response.text)

    assert response.status_code in [200, 201] # FakeStore API accepts invalid data – mock behavior
