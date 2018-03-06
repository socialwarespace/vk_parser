import matplotlib as mpl
import matplotlib.pyplot as plt


class Plots(object):
    def round_plot(self, data_names, data_values):
        dpi =50
        fig = plt.figure(dpi=dpi, figsize=(700 / dpi, 500 / dpi))
        mpl.rcParams.update({'font.size': 12})

        plt.title('Диаграмма возрастов участников паблика (%)')

        plt.pie(data_values,  autopct='%1.1f%%',
                startangle=90)
        plt.axis('tight')
        plt.legend(loc='best', labels=data_names)
        fig.savefig('pie.png')


if __name__ == '__main__':
    print("\n" + "Вы запустили этот модуль напрямую, а не импортировали его" + "\n")
    input("Нажмите Enter, чтобы выйти")
