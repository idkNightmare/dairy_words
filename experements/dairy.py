import json
FILENAME="words.json"
def load_words():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def save_words(words):
    with open(FILENAME,"w", encoding="utf-8") as file:
        json.dump(words,file,ensure_ascii=False,indent=4)
def add_word():
    name=input("введіть нове слово: ").strip()
    traslete=input("переклад слова: ").strip()
    if not name or not traslete:
        print("Помилка! ви ввели в якомусь полі нічого")
        return
    words = load_words()
    new_words={"name":name,"traslete":traslete}
    words.append(new_words)
    save_words(words)
    print("все було успішно додано!")
def show_words():
    words = load_words()
    if not words:
        print("поки не має слів")
        return
    for index, word in enumerate(words,start=1):
        print(f"{index}. {word['name']} - {word['traslete']}")
def delete_word():
    title_to_delete=input("виберіть те що видалити: ").strip().lower()
    words=load_words()
    initial_count=len(words)
    words=[word for word in words if word["name"].strip().lower() != title_to_delete]
    if len(words)<initial_count:
        save_words(words)
        print("успішно видалено!")
    else:
        print("слово не знайдено")
def main():
    while True:
        print("\n === Меню Словника === ")
        print("1: показати всі слова з перекладом")
        print("2: додати слово")
        print("3: видалити слово")
        print("4: вийти")
        choise=input("оберіть дію (1-4): ").strip()
        if choise=="1":
            show_words()
        elif choise=="2":
            add_word()
        elif choise=="3":
            show_words()
            delete_word()
        elif choise=="4":
            print("ви вийшли, до зустрічі!")
            break
        else:
            print("ви ввели не коректну дію!")
if __name__ == "__main__":
    main()