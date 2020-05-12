def main():
    L = []
    while 1:
        x = input('姓名:')
        if not x :
            break
        y = int(input('年紀'))
        z = int(input('成績'))
        d={}
        d['name']=x
        d['age']=y
        d['score']=z
        L.append(d)
    return L
def see(L):
    print('+------------+------+-------+')
    print('|   name     | age  | score |')
    print('+------------+------+-------+')
    for d in L:  
        t = (d['name'].center(12),str(d['age']).center(6),str(d['score']).center(7))
        line = "|%s|%s|%s|" % t
        print(line)
    print('+------------+------+-------+')
def amend(lst):
    x = input('要修改成績的學生:')
    for d in lst:
        if d['name'] == x:
            score = int(input('輸入新的成績:'))
            d['score'] = score
            print('修改', x, '的成績為:', score)
            return
    print('未找到')
def remove(lst):
    x = input('要刪除資料的學生:')
    for i in range(len(lst)):
        if lst[i]['name'] == x:
            del lst[i]
            print('success delet the student.')
            return
        print('未找到')
def save_to_file(does):
    try:
        f = open('student.csv', 'w')
        for stu in does:
            stu.wrute_to_file(f)
            f.close()
        print('save success')
    except OSError:
        print('save fail')

def open_from_file():
    L = []
    try:
        f = open('student.csv')
        for line in f:
            s = line.rstrip()
            lst = s.strip(',')
            name, age, score = lst
            age = int(age)
            score = int(score)
            L.append(student(name, age, score))
        f.close()
    except OSError:
        print('open fail')