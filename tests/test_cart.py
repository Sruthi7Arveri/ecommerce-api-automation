def test_add_product_to_cart_valid_data(api_client):
    """
        Verify cart creation with valid user and product
    """
    payload = {
        "userId": 1,
        "date": "2025-01-01",
        "products": [
            {
                "productId": 1,
                "quantity": 2
            }
        ]
    }

    response = api_client.post("/carts", payload)

    print(response.status_code)
    print(response.text)
    assert response.status_code in [200, 201]
    assert response.json()["userId"] == 1
