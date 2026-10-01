import requests

def test_kubernetes_query():
    response = requests.post("http://127.0.0.1:8000/query?q=What does Geoffry do for fun?")
    
    if response.status_code != 200:
        raise Exception(f"Server returned {response.status_code}: {response.text}")
    
    answer = response.json()["answer"]

    # Check for key concepts
    assert "one piece" in answer.lower(), "Missing 'one piece' keyword"

    print("✅ Kubernetes query test passed")

if __name__ == "__main__":
    test_kubernetes_query()
    print("All semantic tests passed!")