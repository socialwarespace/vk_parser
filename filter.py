from datetime import date


class Filter(object):
    def __init__(self, list_parsing):
        self.__list_paring = list_parsing

    def filter_sex(self):
        tr = []
        for i in self.__list_paring:
            string = str(i.get("sex")) + "\n"
            tr.append(string)
        girl = tr.count('1\n')
        man = tr.count('2\n')

        return man, girl

    def filter_bdate(self):
        tr = []
        for i in self.__list_paring:
            string = str(i.get("bdate"))
            tr.append(string)

        birth_data = []
        i = 0
        while i < len(tr):
            dat = tr[i].split('.')
            if dat[0] != 'Note' and len(dat) == 3 and int(dat[2]) > 1973:
                self.__year = int(dat[2])
                self.__month = int(dat[1])
                self.__day = int(dat[0])

                birth_data.append(self.__private_calculate_age())
                birth_data.sort()

            i += 1

        k = 0
        age = []
        count_age = []
        for i in birth_data:
            if k != i:
                age_count = birth_data.count(i)
                age.append(i)
                count_age.append(age_count)
                k = i

        return age[:], count_age[:]

    def __private_calculate_age(self):
        today = date.today()
        age = today.year - self.__year
        full_year_passed = (today.month, today.day) < (self.__month, self.__day)
        if not full_year_passed:
            age -= 1

        return age

    def seve_list(self, list, name_file_txt):
        line_file = open(name_file_txt, 'w',
                         encoding='utf-8-sig')
        line_file.writelines(list)
        line_file.close()


if __name__ == '__main__':
    print("\n" + "Вы запустили этот модуль напрямую, а не импортировали его" + "\n")
    input("Нажмите Enter, чтобы выйти")
