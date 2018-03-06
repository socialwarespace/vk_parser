import time, random


class Parsing(object):
    def __init__(self):
        __group_id = self.__private_path_to_()
        self.__group_id = __group_id

    def __private_path_to_(self):
        try:
            # кодировка utf-8 без BOM,
            # таким способом убрал '\ufeff',
            # который появлялся в списке
            line_file = open('group_id.txt', 'r',
                             encoding='utf-8-sig')
        except FileNotFoundError as error_1:
            print('Фаил "group_id.txt" не найден' + "\n",
                  error_1)
            input("\n\n Нажмите Enter, чтобы выйти")

        try:
            line = line_file.readline()
        except NameError as error_2:
            print("\n", error_2)
            input("\n\n Нажмите Enter, чтобы выйти")

        line_file.close()
        line_ = line[:]

        return line_

    def parsing(self, session):
        try:
            s = session.groups.getMembers(group_id=self.__group_id,
                                          sort='id_asc',
                                          offset=1, fields='sex, bdate',
                                          count=1, v=5.73)
        except:
            print("\nОшибка при парсинге!")
            print("\nvk.exceptions.VkAPIError: 8. Invalid request")
            input("\n\n Нажмите Enter, чтобы выйти")

        # Получаем колличество подписчиков группы
        all_count = s.get("count")
        print("Всего подписчиков: ", all_count)

        if all_count >= 100 and all_count < 1000:
            offset_= 100
            count_ = 100

        elif all_count >= 1000 and all_count < 10000:
            offset_ = 500
            count_ = 500
        elif all_count >= 10000:
            offset_ = 1000
            count_ = 1000
        else:
            offset_ = 1
            count_ = 1

        s_list_items = []
        s_list_items_ = []
        while all_count > offset_:
            print("offset =", offset_, "\n")
            try:
                s = session.groups.getMembers(group_id=self.__group_id,
                                              sort='id_asc',
                                              offset=offset_, fields='sex, bdate',
                                              count=count_, v=5.73)
            except:
                print("\nОшибка при парсинге!")
                print("\nvk.exceptions.VkAPIError: 8. Invalid request")
                input("\n\n Нажмите Enter, чтобы выйти")

            s1 = s.get("items")

            for k in s1:
                s_list_items.append(k)
            s_list_items_ = s_list_items_ + s_list_items[:]

            offset_ += len(s_list_items_)

            time.sleep(random.randrange(5, 7))

        print("\n")
        return s_list_items_[:]


if __name__ == '__main__':
    print("\n" + "Вы запустили этот модуль напрямую, а не импортировали его" + "\n")
    input("Нажмите Enter, чтобы выйти")
