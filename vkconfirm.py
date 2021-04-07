

import vk_api, time
vk = vk_api.VkApi(token="access_token") # получаем в https://vkhost.github.io/ [VK API]
print("Включен автоприем в друзья")
id2 = 0
followers_count = vk.method("users.getFollowers", {"count": 0})["count"] #получаем количество подписчиков
if followers_count > 0:
    if followers_count == 1:
        print("Добавляю в друзья "+str(followers_count)+ " пользователя")
    if followers_count > 1:
        print("Добавляю в друзья "+str(followers_count)+ " пользователей")
if followers_count > 1000:
    followers_count == 1000
while True:
    followers_count = vk.method("users.getFollowers", {"count": 0})["count"] #получаем количество подписчиков
    if followers_count >= 1:
        print("Новая заявка в друзья")
    followers = vk.method("users.getFollowers", {"count": 10}) #получаем id подписчиков
    for i in range(followers_count):
        try:
            id = followers["items"][0] #получаем id подписчика
            if id != id2 or id2 == 0:
                id2 = id
                print("id пользователя " + str(id))
                user_get = vk.method("users.get", {"user_ids": id}) #получаем инфу про подписчика
                try:
                    vk.method("friends.add", {"user_id": id})
                    print("Добавил пользователя c id " + str(id) + " в друзья")
                except:
                    try:
                        vk.method("account.ban", {"owner_id": id})
                        print("Пользователь с id " + str(id) + " добавлен в чёрный список")
                    except:
                        print("Пользователь уже добавлен в чёрном списке")
        except:
            continue

