def sort_by_length(song_info_dict):
    return song_info_dict['length']


def sort_dict_by_value(item):
    return item[1]


def my_mp3_playlist(file_path):
    songs_info_list = []
    artist_count = {}
    with open(file_path, 'r') as f:
        for line in f.readlines():
            line_list = line.strip().split(';')
            song_info = dict()
            song_info['name'] = line_list[0]
            if line_list[1] in artist_count.keys():
                artist_count[line_list[1]] += 1
            else:
                artist_count[line_list[1]] = 1
            song_info['artist'] = line_list[1]
            song_info['length'] = line_list[2]
            songs_info_list.append(song_info)
    return sorted(songs_info_list, key=sort_by_length, reverse=True)[0]['name'], len(songs_info_list), \
        sorted(artist_count, key=sort_dict_by_value)[0]


print(my_mp3_playlist('../משימה מתגלגלת/test_file.txt'))
