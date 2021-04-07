

import sys, vk_api, time
print("\nAutoFriendAdd (Stable v2.0) by Sykten13 - vk.com/glideru")
access_token = input("(https://vkhost.github.io) - [VK API]\nВведите ваш access token : ")
vk = vk_api.VkApi(token=access_token)
print("\nЗаявок в друзья: " + str(vk.method("users.getFollowers", {"count": 1})["count"])+"\n")
id2 = 0
while True:
    followers_count = vk.method("users.getFollowers", {"count": 1})["count"]
    if followers_count > 0:
        id = vk.method("users.getFollowers", {"count": 1})["items"][0]
        if id != id2 or id2 == 0:
            id2 = id
            print("Новая заявка в друзья, id пользователя " + str(id))
            try:
                vk.method("friends.add", {"user_id": id})
                print("Добавил пользователя c id " + str(id) + " в друзья\n")
            except:
                try:
                    vk.method("account.ban", {"owner_id": id})
                    print("Пользователь с id " + str(id) + " добавлен в чёрный список\n")
                except:
                    print("Пользователь уже добавлен в чёрном списке\n")
    else:
        for i in range(4):
            sys.stdout.write("Ждём заявки в друзья" + "." * i + "\r")
            time.sleep(0.8)

