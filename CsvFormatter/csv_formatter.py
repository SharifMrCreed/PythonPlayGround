_id = []
rank = []
main_skills = []
other_skills = []
header = ""
with open("candidate - Sheet1.csv", "r") as file:
    for line in file:
        words = line.split(",")
        if not words[0].__contains__("id"):
            _id.append(words[0])
            rank.append(words[1])
            main_skills.append(words[2])
            other_skills.append(words[3:])
        else:
            header = line

with open("Candidates.csv", "w") as csv_file:
    csv_file.write(header)
    i = 0
    while i < len(_id):
        print(str(other_skills[i]))
        csv_file.write(f"{_id[i]},{rank[i]},{main_skills[i]},\"" +
                       ', '.join(other_skills[i]).replace('\n', '').replace('"', '') + "\"\n")
        i += 1

# with open("Candidates.csv", "r") as cs_file:
#     for l in cs_file:
#         print(l)
