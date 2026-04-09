# # '''#Общая часть
# # #1
# #Контейнер расчета
# from sympy import *
# k, T, C, L = symbols('k T C L')
# #1 способ
# C_ost = 100000
# Am_lst = []
# C_ost_lst = []
# for i in range (5):
#   Am = (C - L )/ T
#   C_ost -= Am.subs({C:100000, T:5, L:0})
#   Am_lst.append(round(Am.subs({C:100000, T:5, L:0}),2))
#   C_ost_lst.append(round(C_ost,2))
# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# #2 
# Aj=0
# C_ost = 100000
# Am_lst_2 = []
# C_ost_lst_2 = []
# for i in range (5):
#   Am = k * 1/ T * (C - Aj)
#   C_ost -= Am.subs({C:100000, T:5, k:2})
#   Am_lst_2.append(round(Am.subs({C:100000, T:5, k:2}),2))
#   Aj += Am
#   C_ost_lst_2.append(round(C_ost,2))
# print('Am_lst_2:', Am_lst_2)
# print ('C_ost_lst_2:', C_ost_lst_2)

# #3
# #Контейнер расчета
# from sympy import *
# k, T, C, L = symbols('k T C L')

# #1 способ
# C_ost_3 = 30000
# Am_lst_3 = []
# C_ost_lst_3 = []
# for i in range (8):
#    Am = (C - L )/ T
#    C_ost_3 -= Am.subs({C:30000, T:8, L:0})
#    Am_lst_3.append(round(Am.subs({C:30000, T:8, L:0}),2))
#    C_ost_lst_3.append(round(C_ost_3,2))
# print('Am_lst_3:', Am_lst_3)
# print('C_ost_lst_3:', C_ost_lst_3)

# #2 способ
# Aj = 0
# C_ost_3 = 30000
# Am_lst_2_3 = []
# C_ost_lst_2_3 = []
# for i in range (8):
#    Am = k * 1/ T * (C - Aj)
#    C_ost_3 -= Am.subs({C:30000, T:8, k:2})
#    Am_lst_2_3.append(round(Am.subs({C:30000, T:8, k:2}),2))
#    Aj += Am
#    C_ost_lst_2_3.append(round(C_ost_3,2))
# print  ('Am_lst_2_3:', Am_lst_2_3)
# print ('C_ost_lst_2_3:', C_ost_lst_2_3)

# #Контейнер табличного вывода
# import pandas as pd
# Y = range (1,9)
# table1 = list(zip( Y, Am_lst_3, C_ost_lst_3))
# table2 = list(zip( Y, Am_lst_2_3, C_ost_lst_2_3))
# tfame = pd.DataFrame(table1, columns = ['Y', 'Am_lst_3', 'C_ost_lst_3'])
# tfame2 = pd.DataFrame(table2, columns = ['Y', 'Am_lst_2_3', 'C_ost_lst_2_3'])
# print(tfame)
# print(tfame2)

# #Контейнер визуализации
# import numpy as np
# import matplotlib.pyplot as plt
# plt.plot (tfame['Y'], tfame ['C_ost_lst_3'], label = 'Am')
# plt.savefig('chart1.png')
# plt.figure()
# plt.plot (tfame2['Y'], tfame2 ['C_ost_lst_2_3'], label = 'Am_2')
# plt.savefig('chart2.png')

# vals = Am_lst_3
# labels = [str(x) for x in range (1,9)]
# explde = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie (vals, labels = labels, autopct = '%1.1f%%', shadow = True, explode = explde, wedgeprops = {'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels = True)
# ax.axis("equal")
# plt.savefig('chart3.png')

# vals = Am_lst_2_3
# labels = [str(x) for x in range (1,9)]
# explde = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie (vals, labels = labels, autopct = '%1.1f%%', shadow = True, explode = explde, wedgeprops = {'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels = True)
# ax.axis("equal")
# plt.savefig('chart4.png')

# #Гистограммы
# table1 = list(zip(Y, Am_lst_3))
# table2 =  list(zip(Y, Am_lst_2_3))
# tfame = pd.DataFrame(table1, columns = ['Y', 'Am_lst_3'])
# tfame2 = pd.DataFrame(table2, columns = ['Y', 'Am_lst_2_3'])

# plt.figure()
# plt.bar (tfame['Y'], tfame['Am_lst_3'])
# plt.savefig('chart5.png')

# plt.figure()
# plt.bar (tfame2['Y'], tfame2['Am_lst_2_3'])
# plt.savefig('chart6.png')
# plt.figure()

# #Индивидуальная часть
# from sympy import *
# k, T, C, L = symbols('k T C L')

# #1 способ
# C_ost_4 = 90000
# Am_lst_4 = []
# C_ost_lst_4 = []
# for i in range (9):
#    Am = (C - L )/ T
#    C_ost_4 -= Am.subs({C:90000, T:9, L:0})
#    Am_lst_4.append(round(Am.subs({C:90000, T:9, L:0}),2))
#    C_ost_lst_4.append(round(C_ost_4,2))
# print('Am_lst_4:', Am_lst_4)
# print('C_ost_lst_4:', C_ost_lst_4)

# #2 способ
# Aj = 0
# C_ost_4 = 90000
# Am_lst_2_4 = []
# C_ost_lst_2_4 = []
# for i in range (9):
#    Am = k * 1/ T * (C - Aj)
#    C_ost_4 -= Am.subs({C:90000, T:9, k:2})
#    Am_lst_2_4.append(round(Am.subs({C:90000, T:9, k:2}),2))
#    Aj += Am
#    C_ost_lst_2_4.append(round(C_ost_4,2))
# print  ('Am_lst_2_4:', Am_lst_2_4)
# print ('C_ost_lst_2_4:', C_ost_lst_2_4)

# #Контейнер табличного вывода
# import pandas as pd
# Y = range (1,10)
# table1 = list(zip( Y, Am_lst_4, C_ost_lst_4))
# table2 = list(zip( Y, Am_lst_2_4, C_ost_lst_2_4))
# tfame = pd.DataFrame(table1, columns = ['Y', 'Am_lst_4', 'C_ost_lst_4'])
# tfame2 = pd.DataFrame(table2, columns = ['Y', 'Am_lst_2_4', 'C_ost_lst_2_4'])
# print(tfame)
# print(tfame2)

# #Контейнер визуализации
# import numpy as np
# import matplotlib.pyplot as plt
# plt.plot (tfame['Y'], tfame ['C_ost_lst_4'], label = 'Am')
# plt.savefig('chart7.png')
# plt.figure()
# plt.plot (tfame2['Y'], tfame2 ['C_ost_lst_2_4'], label = 'Am_2')
# plt.savefig('chart8.png')

# vals = Am_lst_4
# labels = [str(x) for x in range (1,10)]
# explde = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie (vals, labels = labels, autopct = '%1.1f%%', shadow = True, explode = explde, wedgeprops = {'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels = True)
# ax.axis("equal")
# plt.savefig('chart9.png')

# vals = Am_lst_2_4
# labels = [str(x) for x in range (1,10)]
# explde = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie (vals, labels = labels, autopct = '%1.1f%%', shadow = True, explode = explde, wedgeprops = {'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels = True)
# ax.axis("equal")
# plt.savefig('chart10.png')

# #Гистограммы
# table1 = list(zip(Y, Am_lst_4))
# table2 =  list(zip(Y, Am_lst_2_4))
# tfame = pd.DataFrame(table1, columns = ['Y', 'Am_lst_4'])
# tfame2 = pd.DataFrame(table2, columns = ['Y', 'Am_lst_2_4'])

# plt.figure()
# plt.bar (tfame['Y'], tfame['Am_lst_4'])
# plt.savefig('chart11.png')

# plt.figure()
# plt.bar (tfame2['Y'], tfame2['Am_lst_2_4'])
# plt.savefig('chart12.png')'''



#3 ЛР Общая часть
#1 часть делала с Рощиной
#print(Lihonos)
 
#SESSION_SECRET=os.environ['SESSION_SECRET']
#print(SESSION_SECRET)

#POLI=os.environ['POLI']
#print(POLI)

#2 часть делала с Мамедовой
# Индивидуальный вариант 2
# from sympy import *
# k, T, C, L = symbols ('k C T L')
# #1 способ
# C_ost=50000
# Am_lst=[]
# C_ost_lst=[]
# for i in range(9):
#   Am = (C-L)/T
#   C_ost -= Am.subs({C: 50000, T:9, L:0})
#   Am_lst.append (round (Am.subs({C: 50000, T:9, L:0}), 2))
#   C_ost_lst.append(round(C_ost, 2))
# print ('Am_lst:', Am_lst)
# print ('Am_lst:', C_ost_lst)
# #2 способ
# Aj=0
# C_ost=50000
# Am_lst_2= []
# C_ost_lst_2=[]
# for i in range(9):
#    Am = k * 1/T * (C-Aj)
#    C_ost -= Am.subs({C: 50000, T:9, k:2})
#    Am_lst_2.append (round (Am.subs({C: 50000, T:9, k:2}), 2))
#    Aj += Am
#    C_ost_lst_2.append(round(C_ost, 2))
# print ('Am_lst_2:', Am_lst_2)
# print ('C_ost_lst_2:', C_ost_lst_2)

# #Табличный вывод
# import pandas  as pd
# Y = range(1,10)
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd. DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst'])
# tfame2 = pd. DataFrame(table2, columns=['Y', 'C_ost_lst_2', 'Am_lst_2'])
# print(tfame)
# print(tfame2)
# #Визуализация
# import numpy as np
# import matplotlib.pyplot as plt
# plt.plot(tfame['Y'], tfame ['C_ost_lst'], label = 'Am')
# plt.savefig ('chart13.png')
# plt.figure()
# plt.plot(tfame2['Y'], tfame2 ['C_ost_lst_2'], label = 'Am_2')
# plt.savefig ('chart14.png')
# vals = Am_lst
# labels = [str(x) for x in range(1,10)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie (vals, labels=labels, autopct='%1.1f%%', shadow=True,
#          explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"},
#          rotatelabels=True)
# ax.axis("equal")
# plt.savefig ('chart15.png')
# vals = Am_lst_2
# labels = [str(x) for x in range(1,10)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True,
#         explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"},
#         rotatelabels=True) # что это? это настройки отображения диаграммы, которые включают в себя ширину линии (lw), стиль линии (ls) и цвет линии (edgecolor), а также поворот меток (rotatelabels) Оценка: 5/5 всё верно
# ax.axis("equal")
# plt.savefig ('chart16.png')
# plt.figure()
# table1 = list(zip(Y, Am_lst))
# table2 = list(zip(Y, Am_lst_2))
# tfame = pd.DataFrame(table1, columns = ['Y', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns = ['Y', 'Am_lst_2'])
# plt.bar(tfame['Y'], tfame['Am_lst'])
# plt.savefig ('chart17.jpeg')
# plt.figure()
# plt.bar(tfame['Y'], tfame2['Am_lst_2'])
# plt.savefig ('chart18.png')
# plt.figure()
# Выполнено корректно, ставлю 5/5

# Задание 3
# Восстановлен после удаления контейнер визуализации расчетов

# Задание 4
# Выполняла с Мамедовой
# строка 264

