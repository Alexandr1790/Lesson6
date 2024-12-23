immutable_var = 1, 2, 3, 4 #В этой ситуации нельзя изменить значения элементов
print(immutable_var)
immutable_var1 = ([1, 2], 3)# В Этой ситуации частично можем изменять данные
immutable_var1[0][1]=5
print(immutable_var1)
mutable_list = (1, 2, 3, 4)
mutable_list = 5
print(mutable_list)
