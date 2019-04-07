class info:
    def __init__(self, name, phone, sex):
        self.name = name
        self.phone = phone
        if sex == 'male' or sex == 'female':
            self.sex = sex
        else:
            self.sex = 'unknown'

    def print(self):
        print('이름은 {}, 전화번호는 {}, 성별은 {}입니다.'.format(self.name, self.phone, self.sex))

info_list = list()
name = ""
while name != '그만':
    name = input('이름을 입력하세요: ')
    if name == '그만':
        for person in info_list:
            person.print()
        break
    phone = input('전화번호를 입력하세요: ')
    sex = input('성별을 입력하세요(male이나 female로 작성해주세요): ')

    info_list.append(info(name,phone,sex))
    for person in info_list:
        person.print()
    print()
