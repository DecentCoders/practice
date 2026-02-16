def calc_score(student_info):
    """function for calculating the grade"""
    score = student_info.get("Score")
    try:
         score = int(score)
    except(TypeError,ValueError):
        return "Invalid score"
        
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

student_info = {
        "Name": input("Enter your name: "),
        "ID": input("Enter your ID: "),
        "Score": input("Enter your score: "),}
    
grade = calc_score(student_info)

with open("grades.txt","a")as file:
    line = f'Name: {student_info["Name"]}, ID: {student_info["ID"]}, Score: {student_info["Score"]}, Grade: {grade} \n'
    file.write(line)
    print("Appended successfully..")