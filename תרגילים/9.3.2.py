def my_mp4_playlist(file_path, new_song):
    one_part = []
    two_part = ''
    three_part = []
    with open(file_path, 'r') as f:
        body_file = []
        body_file = f.readlines()
        one_part = body_file[:2]
        two_part = body_file[2]
        three_part = body_file[3:]
        line_song_update = two_part.split(';')
        if len(line_song_update) == 4:
            two_part = new_song + ';' + line_song_update[1] + ';' + line_song_update[2]  + ';' + line_song_update[3]
    with open(file_path, 'w') as f:
        while len(one_part) < 2:
            one_part.append('\n')
        f.writelines(one_part)
        f.write(two_part)
        f.writelines(three_part)
    with open(file_path, 'r') as f:
        for line in f.readlines():
            print(line.strip())


my_mp4_playlist('../משימה מתגלגלת/test_file.txt', 'Python Love Story')