import requests, os

class Imagine:
    def __init__(self, temp_dir):
        self.headers = {
            "authority": "api.craiyon.com",
            "accept": "application/json",
            "accept-language": "en-IR,en-US;q=0.9,en;q=0.8,fa;q=0.7",
            "content-type": "application/json",
            "origin": "https://www.craiyon.com",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        }
        self.temp_dir = temp_dir
        if not os.path.exists(temp_dir):
            os.mkdir(temp_dir)

    def generate(self, message, id):
        json_data = {
            "prompt": message,
            "version": "35s5hfwn9n78gb06",
            "token": None,
            "model": "art",
            "negative_prompt": "",
        }
        if not os.path.exists(f"{self.temp_dir}/{id}"):
            os.mkdir(f"{self.temp_dir}/{id}")


        output = []
        response = requests.post("https://api.craiyon.com/v3", headers=self.headers, json=json_data).json()
        if "images" in response:
            for i in response["images"]:
                name = i.split("/")[1]
                with open(f"{self.temp_dir}/{id}/{name}", "wb") as f:
                    f.write(requests.get("https://img.craiyon.com/"+i).content)
                    output.append(f"{self.temp_dir}/{id}/{name}")
        return output
