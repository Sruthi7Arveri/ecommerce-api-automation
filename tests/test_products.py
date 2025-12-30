def test_get_all_products(api_client):
    """
        verify products present in the database
    """
    response = api_client.get('/products')
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_single_product(api_client):
    """
        verify product-1 present in the database
    """
    response = api_client.get('/products/1')
    assert response.status_code == 200
    assert response.json()['id'] == 1

def test_get_invalid_product(api_client):
    """
        verify product-9999 does not present in the database
    """
    response = api_client.get("/products/9999")
    assert response.status_code == 200
