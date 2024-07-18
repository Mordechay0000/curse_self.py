def copy_file_content(source, destination):
    with open(source, 'r') as source_file, open(destination, 'w') as destination_file:
        for line in source_file:
            destination_file.write(line)
    print('העתקה בוצעה בהצלחה.')