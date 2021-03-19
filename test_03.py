# Функция преобразования списка входов и выходов в матрицу.
def matrix_transformation(list_of_time):
    i = 0
    matrix = list()
    while len(matrix) != len(list_of_time) // 2:
        temp_list = list()
        temp_list.append(list_of_time[i])
        temp_list.append(list_of_time[i + 1])
        matrix.append(temp_list)
        i += 2
    return matrix


# Функция ограничивающая временные интервалы временем урока.
def enter_exit_point_limiter(list_of_time, limiter_list):
    if list_of_time[0] < limiter_list[0]:
        list_of_time[0] = limiter_list[0]
    if list_of_time[-1] > limiter_list[-1]:
        list_of_time[-1] = limiter_list[-1]
    return list_of_time


# Функция сравнивающая временные интервалы, суммирующая пересекающиеся интервалы
# и возвращающая общее время в секундах.
def appearance(intervals):
    lesson_time = intervals.get('lesson')
    pupil_time = intervals.get('pupil')
    tutor_time = intervals.get('tutor')
    enter_exit_point_limiter(pupil_time, lesson_time)
    enter_exit_point_limiter(tutor_time, lesson_time)
    pupil_matrix_time = matrix_transformation(pupil_time)
    tutor_matrix_time = matrix_transformation(tutor_time)
    ttl_time = list()
    for pupil in pupil_matrix_time:
        for tutor in tutor_matrix_time:
            point_in_range = pupil[0] in range(tutor[0], tutor[1]) \
                             or pupil[1] in range(tutor[0], tutor[1])
            if pupil[0] < tutor[0] and pupil[1] < tutor[1] and point_in_range:
                ttl_time.append(pupil[1] - tutor[0])
            elif pupil[0] > tutor[0] and pupil[1] > tutor[1] and point_in_range:
                ttl_time.append(tutor[1] - pupil[0])
            elif pupil[0] in range(tutor[0], tutor[1]) and point_in_range:
                ttl_time.append(pupil[1] - pupil[0])
    return sum(ttl_time)


# Тестовый словарь из задания.
time_dict = {
  'lesson': [1594663200, 1594666800],
  'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
  'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
}

if __name__ == '__main__':
    print(appearance(time_dict))
