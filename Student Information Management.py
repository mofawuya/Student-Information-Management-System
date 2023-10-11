import os
filename = 'student.txt'

def main():
    while True:
        menu()
        choice = int(input('Please input the number'))
        if choice in range(0, 6):
            if choice == 0:
                answer = input('Are you sure you want to exit? y/n')
                if answer == 'y' or answer == 'Y':
                    print('Thank you!!')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                delete()
            elif choice == 3:
                modify()
            elif choice == 4:
                total()
            elif choice == 5:
                show()


def show():
    try:
        f_hand = open('student.txt', 'r')
        content = f_hand.readlines()
        for item in content:
            print(item, end='')
    except:
        print("Something unexpected occurred!")


def menu():
    print("==================Student information==================\n")
    print('--------------------Menu---------------------------')
    print('\t\t\t\t\t1.Input student information')
    print('\t\t\t\t\t2.Delete information')
    print('\t\t\t\t\t3.Modify information')
    print('\t\t\t\t\t4.Count total number of student')
    print('\t\t\t\t\t5.Show the information')
    print('\t\t\t\t\t0.Exit')
    print('-----------------------------------------------------')


def insert():
    student_list = []
    while True:
        id = input('Please input the id:')
        if not id:
            break
        name = input('please input the name:')
        if not name:
            break

        try:
            c_p = int(input('Please input C++ score:'))
            python = int(input('please input Python score:'))
            java = int(input('please input Java score:'))
        except:
            print('invalid input, please try again')
            continue

        student = {'id': id, 'name': name, 'C++': c_p, 'python': python, 'java': java}

        student_list.append(student)
        answer = input('Do you want to continue? y/n')
        if answer == 'y':
            print()
            continue
        else:
            print()
            break

    save(student_list)
    print('Information saved!!')


def save(lst):
    try:
        stu_txt = open(filename, 'a')
    except:
        stu_txt = open(filename, 'w')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def delete():
    while True:
        student_id = input('Please input the ID:')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False
            if student_old:
                with open(filename, 'w') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id{student_id} has been removed')
                    else:
                        print(f'ID{student_id}not found')
            else:
                print('No information')
                break
            show()
            answer = input('Do you want to continue? y/n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('Please input the ID')
    with open(filename, 'w') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('Information found.')
                while True:
                    try:
                        d['name'] = input('please input the name:')
                        d['c++'] = input('Please input the C++ score:')
                        d['python'] = input('Please input the Python score:')
                        d['java'] = input('Please input the Java score:')
                    except:
                        print('Invalid input, please try again')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('Modify Succeed')
            else:
                print('No information found')
                ans = input("Do you want to add the information? y/n")
                if ans == 'y' or 'Y':
                    insert()
                else:
                    break
            answer = input('Do you want to continue? y/n')
            if answer == 'y' or answer == 'Y':
                continue


def total():
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            students = rfile.readlines()
            if students:
                print(f'There are{len(students)} students in total')
    else:
        print('No information saved!')

if __name__ == '__main__':
    main()