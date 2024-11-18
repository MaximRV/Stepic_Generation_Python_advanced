students_lst = [input() for _ in range(int(input()))]
good_marks_stud_list = [i for i in students_lst if
                        int(i[-1]) == 4 or int(i[-1]) == 5]
print(*students_lst, sep="\n")
print()
print(*good_marks_stud_list, sep="\n")
