import customtkinter
import parcer

dictionary_of_cities = {
    "Вінниця": "https://ua.sinoptik.ua/погода-вінниця",
    "Луцьк": "https://ua.sinoptik.ua/погода-луцьк",
    "Дніпро": "https://ua.sinoptik.ua/погода-дніпро",
    "Донецьк": "https://ua.sinoptik.ua/погода-донецьк",
    "Житомир": "https://ua.sinoptik.ua/погода-житомир",
    "Запоріжжя": "https://ua.sinoptik.ua/погода-запоріжжя",
    "Івано-Франківськ": "https://ua.sinoptik.ua/погода-івано-франківськ",
    "Київ": "https://ua.sinoptik.ua/погода-київ",
    "Кропивницький": "https://ua.sinoptik.ua/погода-кропивницький",
    "Луганськ": "https://ua.sinoptik.ua/погода-луганськ",
    "Львів": "https://ua.sinoptik.ua/погода-львів",
    "Миколаїв": "https://ua.sinoptik.ua/погода-миколаїв",
    "Одеса": "https://ua.sinoptik.ua/погода-одеса",
    "Полтава": "https://ua.sinoptik.ua/погода-полтава",
    "Рівне": "https://ua.sinoptik.ua/погода-рівне",
    "Севастополь": "https://ua.sinoptik.ua/погода-севастополь",
    "Сімферополь": "https://ua.sinoptik.ua/погода-сімферополь",
    "Суми": "https://ua.sinoptik.ua/погода-суми",
    "Тернопіль": "https://ua.sinoptik.ua/погода-тернопіль",
    "Харків": "https://ua.sinoptik.ua/погода-харків",
    "Херсон": "https://ua.sinoptik.ua/погода-херсон",
    "Хмельницький": "https://ua.sinoptik.ua/погода-хмельницький",
    "Черкаси": "https://ua.sinoptik.ua/погода-черкаси",
    "Чернівці": "https://ua.sinoptik.ua/погода-чернівці",
    "Чернігів": "https://ua.sinoptik.ua/погода-чернігів",
    "Ужгород": "https://ua.sinoptik.ua/погода-ужгород"
}
list_of_Ukr_cities = ["Вінниця", "Луцьк", "Дніпро", "Донецьк", "Житомир", "Запоріжжя", "Івано-Франківськ", "Київ", "Кропивницький", "Луганськ", "Львів", "Миколаїв", "Одеса", "Полтава", "Рівне", "Севастополь", "Сімферополь", "Суми", "Тернопіль", "Харків", "Херсон", "Хмельницький", "Черкаси", "Чернівці", "Чернігів", "Ужгород"]

app = customtkinter.CTk()
app.title("Моя погода")
app.geometry("600x500")

# Block resize function
app.minsize(600, 500)
app.maxsize(600, 500)

# Set the theme of the application
customtkinter.set_appearance_mode('light')

# First label with the temperature
label1 = customtkinter.CTkLabel(app, text="Оберіть місто ", fg_color="transparent", wraplength=500)
label1.pack(padx=20, pady=100)
label1.configure(compound="right")

# Second label with the weather forecast
label2 = customtkinter.CTkLabel(app, text="", fg_color="transparent", wraplength=500)
label2.pack(padx=20, pady=110)
label2.configure(compound="right")

# Function for making choice
def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)
    label1.configure(text=choice + " : " + parcer.parse_website(dictionary_of_cities[choice]))
    label2.configure(text=parcer.get_current_weather(dictionary_of_cities[choice]))

# Create the combobox, where user can choose city
combobox_var = customtkinter.StringVar(value="Київ")
combobox1 = customtkinter.CTkComboBox(app, values=list_of_Ukr_cities, command=combobox_callback, variable=combobox_var, state="readonly")
combobox_var.set("Місто")
combobox1.place(relx=0.3, rely=0.2, anchor=customtkinter.NE)

app.mainloop()
