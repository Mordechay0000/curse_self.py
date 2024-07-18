def seven_boom(end_number):
    boom_list = []
    for i in range(end_number + 1):
        # אם התו 0 לא צריך להחשב כ BOOM
        # אפשר להוסיף לתנאי 'and i != 0'
        # אבל בדוגמה בקמפוס il הוצג
        # ש 0 גם נחשב BOOM למרות שלכאורה זה לא כפולה של המספר 7...
        if i%7 == 0:
            boom_list.append('BOOM')
        elif str(i).count('7') != 0:
            boom_list.append('BOOM')
        else:
            boom_list.append(i)
    return boom_list