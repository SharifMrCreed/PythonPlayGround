

def extract_skills_from_skillstxt():
    #Extracting only the skills from the skills.txt and putting them in the newSkills.txt file
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


def extract_skills_from_skillsXIcsv():
    #Extracting only the skills from the skillsXI.csv and putting them in the newSkillsList.txt file
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

def extract_skills_from_berufecsv():
    #Extracting only the skills from the berufe.csv and putting them in the newBerufe.txt file
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


def firebase_friendly_skills():
    #skills in a firebase friendly format with an id an the name.
    #this will be from berufe.scv and put in beruf_firebase_friendly.csv
    new_list = []
    with open("berufe.csv", "r") as file:
        for line in file:
            skills = line.split(",")
            if not new_list.__contains__(skills[1].replace("\n", "").replace("\"", "")):
                new_list.append(skills[0].replace("\n", "").replace("\"", "")+","+skills[1].replace("\n", "").replace("\"", ""))

    print(new_list)
    print(len(new_list))
    with open("BerufeForFirestore.csv", "w") as _file:
        for e in new_list:
            _file.write(e+"\n")

def new_berufe_to_list():
    #Returns the new skills as a list
    new_list = []
    with open("newBerufe.txt", "r") as file:
        for line in file:
            new_list.append(line.replace("\n", ""))

    with open("BerufeList", "w") as _file:
        for e in new_list:
            _file.write(f'"{e}",')
            
    print(new_list)
    print(len(new_list))

new_berufe_to_list()