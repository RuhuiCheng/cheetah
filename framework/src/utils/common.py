import string


def str_clear(txt):
    return txt.translate(str.maketrans('', '', string.punctuation))


def int_val(val):
    bl_int = isinstance(val, int)
    if bl_int:
        return val
    bl_str = isinstance(val, str)
    if bl_str:
        bl_str_int = val.isdigit()
        if bl_str_int:
            return int(val)
    return None


def read_txt(file_path):
    with open(file_path, 'r') as f:
        ls_item = f.readlines()
        txt = ''.join(ls_item)
        return txt


def write_txt(file_path, txt_content):
    with open(file_path, "w") as f:
        f.write(txt_content)


def read_sqlheader(file_path):
    dict_header = {}
    dict_header['sql_path'] = file_path
    with open(file_path, 'r') as f:
        line1 = f.readline().strip('\n').strip('--').strip()
        line2 = f.readline().strip('\n').strip('--').strip()
        if (len(line1) == 0) or (len(line2) == 0):
            raise ValueError('SQL hearder is invalid. sql_file --> {0}'.format(file_path))
        item1 = line1.split('=')
        dict_header[item1[0]] = item1[1]
        item2 = line2.split('=')
        dict_header[item2[0]] = item2[1]
    return dict_header
