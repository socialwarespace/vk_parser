import vk, re, time, random


class SignIn(object):
    def __init__(self):
        path_to_acc = self.__private_path_to_()
        list_data_acc = self.__private_regular(path_to_acc)

        self.__list_data_acc_0 = list_data_acc[0]
        self.__list_data_acc_1 = list_data_acc[1]
        self.__list_data_acc_2 = list_data_acc[2]

    def __private_path_to_(self):
        try:
            # кодировка utf-8 без BOM,
            # таким способом убрал '\ufeff',
            # который появлялся в списке
            line_file = open('account.txt', 'r',
                             encoding='utf-8-sig')
        except FileNotFoundError as error_1:
            print('Фаил "account.txt" не найден \n',
                  error_1)
            input("\n\n Нажмите Enter, чтобы выйти")

        try:
            line = line_file.readline()
        except NameError as error_2:
            print("\n", error_2)

        line_file.close()

        return line[:]


    def __private_regular(self, line_reg):
        result = re.split(r' ', line_reg)
        return result

    def authorization_vk(self):
        session = vk.AuthSession(self.__list_data_acc_0,
                                 self.__list_data_acc_1,
                                 self.__list_data_acc_2)

        vk_api = vk.API(session)

        time.sleep(random.randrange(5, 7))  # Пауза после авторизации

        return vk_api


if __name__ == '__main__':
    print("\n" + "Вы запустили этот модуль напрямую, а не импортировали его" + "\n")
    input("Нажмите Enter, чтобы выйти")
