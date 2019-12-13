class ConfigDict(dict):
    def __init__(self, file_name):
        self.file_name = file_name
        self.dict_data = {}
        with open(file_name, 'r') as f:
            str_cont = f.read()
            self.dict_data = dict(x.split('=') for x in str_cont.split('\n'))
    def __setitem__(self, key, val):
        dict.__setitem__(self.dict_data, key, val)
        with open(self.file_name, 'a+') as f:
            f.write("\n" + str(key) + '=' + str(val))
    def __getitem__(self, item):
        return dict.__getitem__(self.dict_data, item)


cc = ConfigDict('config_file.txt')

print(cc['query'])                     # SELECT this FROM that WHERE condition
print(cc['email_to'])                  # me@mydomain.com
cc['database'] = 'mysql_managed'
print()
print()

print(cc.dict_data)

