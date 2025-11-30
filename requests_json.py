# get news in szzx
# and return data in json


class get_analyze_json():
    
    def __init__(self, root_url, directory, params):
        self.root_url = root_url
        self.url = root_url + directory
        self.params = params

        self.my_requests_get()
        self.bs_analyze()
        self.json_dumps()

    def my_requests_get(self):

        import requests
        
        try:
            response = requests.get(url=self.url, params=self.params)
            if response.status_code !=200:
                raise Exception(f"status_code is {response.status_code} not 200")

        except Exception as e:
            raise 

        response.encoding = "utf-8"
        content = response.text
        
        self.content = content


    def bs_analyze(self):

        import bs4

        soup = bs4.BeautifulSoup(self.content, "html.parser")
        news = soup.find("ul", attrs={"class":"listsbox"}).find_all("a")
        times = soup.find("ul", attrs={"class":"listsbox"}).find_all("span")
        self.news = news
        self.times = times
                

    def json_dumps(self):

        import json
        
        nodes = []
        Id = 0
        for data in self.news:
            node = {"id":Id,
                    "href":f"{self.root_url}{data['href']}",
                    "text":data.get_text(),
                    "time":self.times[Id].get_text()}
            nodes.append(node)
            Id += 1
        
        self.json = json.dumps(nodes)




def main():

    root_url = "https://www.szzx1000.cn"
    direction = "/e/action/ListInfo/index.php"
    params = {"page":"1",
               "classid":"1"}
    
    szzx = get_analyze_json(root_url, direction, params)
    print(szzx.json)
    #print(szzx.times)





if __name__ == "__main__":
    main()
