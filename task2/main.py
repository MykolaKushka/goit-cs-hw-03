from pymongo import MongoClient
from bson.objectid import ObjectId

# Підключення до MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Замініть URI на ваш MongoDB Atlas URI за потреби
db = client["cat_database"]  # Назва бази даних
collection = db["cats"]  # Назва колекції

# Create (створення документа)
def create_cat(name, age, features):
    try:
        cat = {"name": name, "age": age, "features": features}
        result = collection.insert_one(cat)
        print(f"Кіт успішно доданий із _id: {result.inserted_id}")
    except Exception as e:
        print(f"Помилка під час створення: {e}")

# Read (читання документів)
def read_all_cats():
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"Помилка під час читання: {e}")

def read_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"Кіт із ім'ям {name} не знайдений.")
    except Exception as e:
        print(f"Помилка під час читання: {e}")

# Update (оновлення документів)
def update_cat_age(name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.matched_count > 0:
            print(f"Вік кота {name} оновлено до {new_age}.")
        else:
            print(f"Кіт із ім'ям {name} не знайдений.")
    except Exception as e:
        print(f"Помилка під час оновлення: {e}")

def add_cat_feature(name, feature):
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": feature}})
        if result.matched_count > 0:
            print(f"Характеристика '{feature}' додана для кота {name}.")
        else:
            print(f"Кіт із ім'ям {name} не знайдений.")
    except Exception as e:
        print(f"Помилка під час оновлення: {e}")

# Delete (видалення документів)
def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Кіт із ім'ям {name} видалений.")
        else:
            print(f"Кіт із ім'ям {name} не знайдений.")
    except Exception as e:
        print(f"Помилка під час видалення: {e}")

def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f"Усі коти видалені. Видалено документів: {result.deleted_count}")
    except Exception as e:
        print(f"Помилка під час видалення: {e}")

# Головна функція
if __name__ == "__main__":
    while True:
        print("\nМеню:")
        print("1. Додати кота")
        print("2. Переглянути всіх котів")
        print("3. Знайти кота за ім'ям")
        print("4. Оновити вік кота")
        print("5. Додати характеристику коту")
        print("6. Видалити кота за ім'ям")
        print("7. Видалити всіх котів")
        print("8. Вийти")

        choice = input("Оберіть дію: ")

        if choice == "1":
            name = input("Введіть ім'я кота: ")
            age = int(input("Введіть вік кота: "))
            features = input("Введіть характеристики (через кому): ").split(", ")
            create_cat(name, age, features)

        elif choice == "2":
            read_all_cats()

        elif choice == "3":
            name = input("Введіть ім'я кота: ")
            read_cat_by_name(name)

        elif choice == "4":
            name = input("Введіть ім'я кота: ")
            new_age = int(input("Введіть новий вік кота: "))
            update_cat_age(name, new_age)

        elif choice == "5":
            name = input("Введіть ім'я кота: ")
            feature = input("Введіть нову характеристику: ")
            add_cat_feature(name, feature)

        elif choice == "6":
            name = input("Введіть ім'я кота: ")
            delete_cat_by_name(name)

        elif choice == "7":
            confirm = input("Ви впевнені? Це видалить усіх котів (так/ні): ")
            if confirm.lower() == "так":
                delete_all_cats()

        elif choice == "8":
            print("Вихід з програми.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")
