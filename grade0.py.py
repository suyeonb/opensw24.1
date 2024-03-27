def input_student_info():
    student_info = {}
    student_info['학번'] = input("학번: ")
    student_info['이름'] = input("이름: ")
    student_info['영어'] = int(input("영어 점수: "))
    student_info['C-언어'] = int(input("C-언어 점수: "))
    student_info['파이썬'] = int(input("파이썬 점수: "))
    return student_info

def calculate_total_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return total, average

def calculate_grade(average):
    if 90 <= average <= 100:
        return 'A+'
    elif 80 <= average < 90:
        return 'A'
    elif 70 <= average < 80:
        return 'B+'
    elif 60 <= average < 70:
        return 'B'
    elif 50 <= average < 60:
        return 'C+'
    elif 40 <= average < 50:
        return 'C'
    else:
        return 'F'

def calculate_rank(scores):
    sorted_scores = sorted(scores, reverse=True)
    rank_dict = {score: i+1 for i, score in enumerate(sorted_scores)}
    return [rank_dict[score] for score in scores]

def print_student_info(student_info, total, average, grade, ranks):
    print("===================================================================================")
    print("성적관리 프로그램")
    print("===================================================================================")
    print(f"{'학번':<12}{'이름':<10}{'영어':<10}{'C-언어':<10}{'파이썬':<10}{'총점':<10}{'평균':<10}{'학점':<10}{'등수':<10}")
    print("===================================================================================")
    print(f"{student_info['학번']:<15}{student_info['이름']:<12}{student_info['영어']:<12}{student_info['C-언어']:<12}"
          f"{student_info['파이썬']:<12}{total:<12}{average:<10.2f}{grade:<12}{ranks[0]:<12}")

def main():
    students = []
    for _ in range(5):
        student_info = input_student_info()
        total, average = calculate_total_average([student_info['영어'], student_info['C-언어'], student_info['파이썬']])
        grade = calculate_grade(average)
        students.append((student_info, total, average, grade))

    sorted_students = sorted(students, key=lambda x: x[2], reverse=True)
    ranks = calculate_rank([student[2] for student in sorted_students])

    for i, (student_info, total, average, grade) in enumerate(sorted_students):
        print_student_info(student_info, total, average, grade, [ranks[i]])

if __name__ == "__main__":
    main()
