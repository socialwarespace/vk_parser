import sing_in, parsing, filter, plots

if __name__ == '__main__':
    print("\n\t\tДанные для входа находятся в файле 'account.txt'"
          + "\n")
    print("\t\tДанные записываются в формате ->app_id login password"
          + "\n")

    # Авторизация
    a = sing_in.SignIn()
    session_vk = a.authorization_vk()

    print("Авторизация прошла успешно\n")
    print("Начинаем парсинг группы...\n")

    p = parsing.Parsing()
    result_parsing = p.parsing(session_vk)

    print("Парсинг выполнен успешно\n")

    f = filter.Filter(result_parsing)
    man, girl = f.filter_sex()

    print("В группе мужчин =", man, " и девушек =", girl, "\n")

    birth_data_age = []
    birth_data_count = []
    birth_data_age, birth_data_count = f.filter_bdate()

    pl = plots.Plots()
    pl.round_plot(birth_data_age, birth_data_count)

    print("\nДиаграмма построена\n")
    input("\nНажмите Enter, чтобы выйти\n")
