person_dict = {'first_name': 'Mariah', 'last_name': 'Carey', 'birth_date': '27.03.1970',
               'hobbies': ['Sing', 'Compose', 'Act']}
while True:
    print(
        """
        1. שם המשפחה
        2. הדפסת החודש מתאריך הלידה
        3. כמות התחביבים
        4. התחביב האחרון ברשימת התחביבים
        5. הוספה של התחביב "Cooking" לסוף רשימת התחביבים.
        6. להפוך את טיפוס תאריך הלידה לטאפל שכולל 3 מספרים (יום, חודש ושנה - משמאל לימין) והדפיסו אותו.
        7. הוספה של מפתח חדש בשם age אשר כולל את גילה של מריה והציגו אותו.
        """
    )

    user_select = int(input('אנא בחר:\n'))
    if user_select == 1:
        print(person_dict['last_name'])
    elif user_select == 2:
        print(person_dict['birth_date'].split('.')[1] if type(person_dict['birth_date']) == str else person_dict['birth_date'][1])
    elif user_select == 3:
        print(len(person_dict['hobbies']))
    elif user_select == 4:
        print(person_dict['hobbies'][len(person_dict['hobbies']) - 1])
    elif user_select == 5:
        person_dict['hobbies'].append('Cooking')
    elif user_select == 6:
        if type(person_dict['birth_date']) == str:
            person_dict['birth_date'] = tuple(person_dict['birth_date'].split('.'))
        print(person_dict['birth_date'])
    elif user_select == 7:
        person_dict['age'] = input('אנא הזן את הגיל:')
        print(person_dict['age'])

    input('הקש אנטר להמשך')
