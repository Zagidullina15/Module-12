number = input("Введите числа через пробел:")
us_number = int(input('Введите любое число:'))

array=list(map(int,number.split()))
if us_number <= min(array) or us_number > max(array):
 print("Число выходит за границы!")
else:
    def merge_sort(array):
        if len(array) < 2:  # если кусок массива равен 2,
            return array[:]  # выходим из рекурсии
        else:
            middle = len(array) // 2  # ищем середину
            left = merge_sort( array[:middle] )  # рекурсивно делим левую часть
            right = merge_sort( array[middle:] )  # и правую
            return merge( left, right )  # выполняем слияние
    def merge(left, right):  # "властвуй"
        result = []  # результирующий массив
        i, j = 0, 0  # указатели на элементы
 # пока указатели не вышли за границы
        while i < len( left ) and j < len( right ):
            if left[i] < right[j]:
                result.append( left[i] )
                i += 1
            else:
                result.append( right[j] )
                j += 1

      # добавляем хвосты
        while i < len( left ):
            result.append( left[i] )
            i += 1

        while j < len( right ):
            result.append( right[j] )
            j += 1
        return result
    print(merge_sort(array))
    sorted_array = merge_sort(array)

    def BinarySearch(sorted_array,us_number):
        first = 0
        last = len(sorted_array)
        while first < last:
            mid = (first+last)//2
            if us_number>sorted_array[mid]:
                first = mid+1
            else:
                last = mid
        return first-1
    print(BinarySearch(sorted_array, us_number))
