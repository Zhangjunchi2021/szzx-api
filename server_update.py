# everyday update server data at 2 a.m.


import time
import schedule


def update_data():
    
    from datetime import datetime
    from requests_json import get_analyze_json

    print(f"{datetime.now()}:Start update")
    for i in range(3):
        with open(f"page{i}.json", "w") as fp:
            fp.write(get_analyze_json("https://www.szzx1000.cn",
                                      "/e/action/ListInfo/index.php",
                                      {"page":str(i),
                                       "classid":"1"}).json)
    
def check_first_run():
    import os
    
    if "page0.json" in os.listdir(os.getcwd()):
        return False
    else:
        return True
        

def main():

    if check_first_run():
        update_data()
    
    schedule.every().day.at("02:00").do(update_data)

    while True:
        schedule.run_pending()
        time.sleep(60)
    


if __name__ == "__main__":
    main()
