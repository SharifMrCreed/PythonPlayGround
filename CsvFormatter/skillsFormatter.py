
skills_List = []

with open("skills.txt", "r") as file:
    for line in file:
        skill = line.replace("\n", "").replace("\"", "")
        if not skills_List.__contains__(skill):
            skills_List.append(skill)

print(skills_List)
print(len(skills_List))

with open("newSkills.txt", "w") as _file:
    for e in skills_List:
        _file.write(e+"\n")


new_list = []
with open("skillsXl.csv", "r") as file:
    for line in file:
        skills = line.split(",")
        if not new_list.__contains__(skill[1].replace("\n", "").replace("\"", "")):
            new_list.append(skills[1].replace("\n", "").replace("\"", ""))

print(new_list)
print(len(new_list))

with open("newSkillsList.txt", "w") as _file:
    for e in new_list:
        _file.write(e+"\n")


new_list = []
with open("berufe.csv", "r") as file:
    for line in file:
        skills = line.split(",")
        if not new_list.__contains__(skill[1].replace("\n", "").replace("\"", "")):
            new_list.append(skills[1].replace("\n", "").replace("\"", ""))

print(new_list)
print(len(new_list))
with open("newBerufe.txt", "w") as _file:
    for e in new_list:
        _file.write(e+"\n")