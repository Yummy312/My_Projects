import re


class Data:
    def __init__(self, full_name, email, file_name,color):
        self.fullname = full_name
        self.email = email
        self.file_name = file_name
        self.color = color

    @property
    def full_name(self):
        return self.fullname

    @full_name.setter
    def full_name(self, value):
        pass

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, value):
        pass

    @property
    def file_name(self):
        return self.file_name

    @file_name.setter
    def file_name(self, value):
        pass

    @property
    def color(self):
        return self.color

    @color.setter
    def color(self, value):
        pass


with open('MOCK_DATA.txt', "r", encoding="utf-8") as file:
    content = file.read()
    Data.color = re.findall(r'\#......', content)
    print(Data.color)

for Data.color in Data.color:
    with open('color.txt', "a", encoding="utf-8") as new_file:
        new_file .write(f'{Data.color}\n')
#
with open('MOCK_DATA.txt', "r", encoding="utf-8") as file:
    content = file.read()
    Data.email = re.findall(r'[\w.-]+@[A-Za-z-]+\.[\w.]+', content)
    print(Data.email)

for Data.email in Data.email:
    with open('email.txt', "a", encoding="utf-8") as new_file:
        new_file .write(f'{Data.email}\n')


with open('MOCK_DATA.txt', "r", encoding="utf-8") as file:
    content = file.read()
    Data.file_name = re.findall(r'\w+\.avi|\w+.pdf|\w+.png|\w+.mp3|\w+.xls|\w+.txt|\w+.jpeg|w+.mpeg',content)

for Data.file_name in Data.file_name:
    with open('file_name.txt', "a", encoding="utf-8") as second_file:
        second_file .write(f'{Data.file_name}\n')


with open('MOCK_DATA.txt', "r", encoding="utf-8") as file:
    content = file.read()
    Data.full_name = re.findall(r'[A-Z][a-z]+\s', content)
    # Data.full_name = re.findall(r'^[A-Z]+\s\w+\s', content)

for Data.full_name in Data.full_name:
    with open('full_name.txt', "a", encoding="utf-8") as third_file:
        third_file .write(f'{Data.full_name}\n')

#


