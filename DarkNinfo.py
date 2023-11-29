RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m' 
CYAN = "\033[36m"
END = "\033[0m"

banner = f"""
  {RED}                        𝗗𝗮𝗿𝗸-᥊
  
  𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 :- @𝗗𝗔𝗥𝗞_𝗫25
  
𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 2𝗡𝗗 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 :-  @𝗜𝗺𝗺𝗼𝗿𝘁𝗮𝗹_𝘅_25
  

                                       """

print(banner)

import requests

url = "https://app.mynagad.com:20002/api/user/check-user-status-for-log-in"
number = input("𝗡A𝗚𝗢𝗗 𝗡𝗨𝗠𝗕 : ")  # Assuming you get the phone number as input

headers = {
    "X-KM-User-AspId": "100012345612345",
    "X-KM-User-Agent": "ANDROID/1152",
    "X-KM-DEVICE-FGP": "19DC58E052A91F5B2EB59399AABB2B898CA68CFE780878C0DB69EAAB0553C3C6",
    "X-KM-Accept-language": "bn",
    "X-KM-AppCode": "01",
}

params = {"msisdn": number}

response = requests.get(url, headers=headers, params=params)

print(response.text)

RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m' 
CYAN = "\033[36m"
END = "\033[0m"

banner = f"""
  {RED}       𝗧𝗛𝗔𝗡𝗞𝗦 𝗙𝗢𝗥 𝗦𝗨𝗣𝗣𝗢𝗥𝗧𝗜𝗡𝗚         
  
                  𝗗𝗮𝗿𝗸-᥊
  
  𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 :- @𝗗𝗔𝗥𝗞_𝗫25
  
𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 2𝗡𝗗 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 :-  @𝗜𝗺𝗺𝗼𝗿𝘁𝗮𝗹_𝘅_25
  

                                       """

print(banner)
