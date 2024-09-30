import requests
BASE_URL="https://fakestoreapi.com"

#1 Вывести продукты, цена которых <20
res1 = requests.get(f"{BASE_URL}/products")
result = filter(lambda f: f['price'] > 20, res1.json())
print(list(result))

#2 Вывести все категории
res2 = requests.get(f"{BASE_URL}/products/categories")
print(res2.json())

#3 Вывести все продукты с категорией  "jewelery"
res3 = requests.get(f"{BASE_URL}/products/category/jewelery")
print(res3.json())

#4 Вывести всех пользователей
res4 = requests.get(f"{BASE_URL}/users")
print(res4.json())

#5 Добавить пользователя со своим именем.
new_user = {
    "email":'knightalli12@gmail.com',
    "username":'knightalli',
    "password":'qwerty',
    "name":{
        "firstname":'Natalya',
        "lastname":'Mironova'
    },
    "address":{
        "city":'Ekaterinburg',
        "street":'Mira street',
        "number":19,
        "zipcode":'000000',
        "geolocation":{
            "lat":'-12',
            "long":'12'
        }
    },
    "phone":'8-900-400-00-00'
}
res5 = requests.post(f"{BASE_URL}/users", json=new_user)
print(res5.json())