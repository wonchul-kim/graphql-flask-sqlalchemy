import requests 


def test(url, query):  
    resp = requests.post(url=url, json={"query": query})

    if resp.status_code == 200:
        # print(resp.content)
        return True, resp.json()
    else:
        return False, {}
        
        