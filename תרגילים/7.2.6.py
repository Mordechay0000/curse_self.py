products_list = input('אנא הזן רשימה של המוצרים מופרדים על ידי פסיק:\n').split(',')

# בשביל לבדוק אם הקלט תקין
# select = '0'
# while select < '1' or select > '9':

def is_valid_product_name(name: str):
    # הגדרת הקריטריונים לבדיקת השם
    min_length = 3

    # בדיקת אורך השם
    if len(name) < min_length:
        return False

    # בדיקת האם השם מכיל תווים שאינם אותיות
    if not name.isalpha():
        return False

    # אם כל הבדיקות עברו בהצלחה
    return True

def find_remove_duplicates(lst):
    seen = []
    duplicates = []
    for item in lst:
        if item in seen:
            duplicates.append(item)
        else:
            seen.append(item)
    return seen, duplicates



while True:
    print(
        """
        1. רשימת המוצרים
        2. מספר המוצרים ברשימת הקניות
        3. האם המוצר נמצא ברשימה?
    4. כמה פעמים מופיע מוצר מסוים?    
        5. מחיקת מוצר מהרשימה (באם יש כפילויות מוצר אחד בלבד יימחק)
    6. הוספת מוצר לרשימה    
    7. הדפסת כל המוצרים שאינם חוקיים    
        8. הסרת כל כפילויות במוצרים הקיימות ברשימה
    9. יציאה    
    
        """
    )
    user_select = input()
    if user_select == '1':
        print('רשימת מוצרים:\n' + '\n'.join(products_list))
    elif user_select == '2':
        print(len(products_list))
    elif user_select == '3':
        product_name = input('אנא הזן שם מוצר:\n')
        print('המוצר נמצא ברשימה' if product_name in products_list else 'המוצר לא נמצא ברשימה')
    elif user_select == '4':
        product_name = input('אנא הזן שם מוצר:\n')
        print(('המוצר נמצא ברשימה כ: ' + str(products_list.count(product_name)) + ' פעמים') if product_name in products_list else 'המצור לא נמצא ברשימה')
    elif user_select == '5':
        product_name = input('אנא הזן את שם המוצר להסרה מהרשימה:\n')
        products_list.remove(product_name)
        print('המוצר ' + product_name + ' הוסר בהצלחה מהרשימה')
        if product_name in products_list:
            print('אזהרה: שימו-לב שהוסר מופע אחד בלבד של המוצר, אך המוצר מופיע ברשימה עוד ' + str(products_list.count(product_name)) + ' פעמים')
    elif user_select == '6':
        product_name = input('אנא הזן את שם המוצר להוספה לרשימה:\n')
        if product_name in products_list:
            print('אזהרה: שימו-לב שהמוצר כבר מופיע ברשימה כ '+ str(products_list.count(product_name)) + 'פעמים')
            is_cancel_append = input('לביטול הוספת המוצר הקישו \'ביטול\' או הקישו \'לא\'')
            if is_cancel_append == 'ביטול' or is_cancel_append == 'לא':
                continue
        products_list.append(product_name)
        print('המוצר ' + product_name + 'נוסף בהצלחה לרשימה')
    elif user_select == '7':
        print('רשימת המוצרים שאינם חוקיים:\n')
        for product in products_list:
            if not is_valid_product_name(product):
                print(product + '\n')
    elif user_select == '8':
        seen, duplicates = find_remove_duplicates(products_list)
        products_list = seen
        print('הוסרו הכפילויות של הפריטים הבאים: ' + '\n'.join(duplicates))
    elif user_select == '9':
        exit(0)
    input('\n\nהקש אנטר לחזרה לתפריט ראשי.\n')