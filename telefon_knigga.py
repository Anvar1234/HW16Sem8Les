# создаем ТК 
filename = "myphonebook.txt" 
myfile = open(filename, "a+") 
myfile.close 
 
# Определяем главное меню
def main_menu(): 
    print( "\nГлавное меню\n") 
    print( "1. Показать все контакты") 
    print( "2. Добавить новый контакт") 
    print( "3. Поиск контактов") 
    print( "4. Выход") 
    choice = input("Укажите свой выбор: ") 
    if choice == "1": 
        myfile = open(filename, "r+") 
        filecontents = myfile.read() 
        if len(filecontents) == 0: 
            print( "Нет контактов") 
        else: 
            print(filecontents) 
        myfile.close 
        enter = input("Нажмите Enter ...") 
        main_menu() 
    elif choice == "2": 
        newcontact() 
        enter = input("Нажмите Enter ...") 
        main_menu() 
    elif choice == "3": 
        searchcontact() 
        enter = input("Нажмите Enter ...") 
        main_menu() 
    elif choice == "4": 
        main_menu() 
    else: 
        print( "Нет такого пункта!\n") 
        enter = input( "Нажмите Enter ...") 
        main_menu() 
 
# Определяем функцию поиска         
def searchcontact(): 
    searchname = input( "Введите Имя: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname 
    myfile = open(filename, "r+") 
    filecontents = myfile.readlines() 
      
    found = False 
    for line in filecontents: 
        if searchname in line: 
            print( "Искомый контакт:", end = " ") 
            print( line) 
            found = True 
            break 
    if found == False: 
        print( "Искомый контакт не найден", searchname) 
 
# Имя 
def input_firstname(): 
    first = input( "Введите Имя: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 
 
# Фамилия
def input_lastname(): 
    last = input( "Введите Фамилию: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname 
 
# Сохранение контакта 
def newcontact(): 
    firstname = input_firstname() 
    lastname = input_lastname() 
    phoneNum = input( "Введите номер телефона: ") 
    opisanie = input( "Описание: ") 
    contactDetails =("[" + firstname + ", " + lastname + ", " + phoneNum + ", " + opisanie +  "]\n") 
    myfile = open(filename, "a") 
    myfile.write(contactDetails) 
    print( "Информация о контакте:\n " + contactDetails + "\nУспешно сохранено!") 
 
main_menu()

