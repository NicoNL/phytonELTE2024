class StudentsDataException(Exception):
    pass
class BadLine(StudentsDataException):
    pass

class FileEmpty(StudentsDataException):
    pass


def grade_reader(filename):
    dic = {}
    try:
        with open(filename, "r") as f:
            lines = f.readline()
            if(len(lines) == 0): raise FileEmpty()
            for line in f:
                words = line.split()
                if(len(words) !=  3): raise BadLine();
                name = words[0]
                last = words[1]
                if name in dic:
                    dic[f"{name} {last}"] += float(words[2])
                else:
                    dic[f"{name} {last}"] = float(words[2])
        for key,value in dic.items():
            print(f"{key} {value}")
    except BadLine:
        print("The line is wrong")
    except FileEmpty:
        print("The file is Empty")
    except FileNotFoundError:
        print("The file was not found")
        

grade_reader("students.txt")

                
         