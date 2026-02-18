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
}

# Get ID with error handling for integer validation
while True:
    try:
        id_input = input("Enter your ID: ")
        student_info["ID"] = int(id_input)
        break
    except ValueError:
        print("Error: ID must be an integer. Please try again.")
while True:
    try:
        score_input = input("Enter your score: ")
        student_info["Score"] =  int(score_input)
        break
    except:
        print("Ivalid input. Try again..")

grade = calc_score(student_info)

# Append a simple Markdown table row to grades.txt without using extra modules.
row = f"| {student_info['Name']} | {student_info['ID']} | {student_info['Score']} | {grade} |\n"
has_header = False
try:
    with open("grades.txt", "r", encoding="utf-8") as f:
        first = f.readline()
        if first.strip().startswith("|"):
            has_header = True
except FileNotFoundError:
    has_header = False

with open("grades.txt", "a", encoding="utf-8") as f:
    if not has_header:
        f.write("| Name | ID | Score | Grade |\n")
    f.write(row)
print("Appended successfully as table row.")