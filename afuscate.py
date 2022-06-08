
languages = {
    "c++":"cpp",
    "cpp":"cpp",
    "cxx":"cpp",
    "c":"c",
}

SPECIAL_CHARS = ["{","}","\"","'",]

import sys

for arg in sys.argv:
    if not arg.startswith('-'):
        CFile = arg
    else:
        if arg.startswith("-x"):
            lang = languages[arg.strip("-x").lower()]

file = open(CFile)
output = []
output_file = []

lang = languages["c++"]

a_counter = 1

output_file.append("#include \"A_FUSCATE.h\"\n")

for line in file.readlines():
    if line.startswith("#"):
        output_file.append(line)
    elif line == "": continue
    else:
        for word in line.split(" "):
            if any(t in word for t in SPECIAL_CHARS):
                for t in word:
                    if t in SPECIAL_CHARS:
                        output.append(f"#define {'A'*a_counter} {t}")
                        output_file.append("A"*a_counter+";")
                        a_counter += 1
                        output.append(f"#define {'A'*a_counter} {word.strip(t)}")
                        output_file.append("A"*a_counter+";")
                        a_counter += 1
                     

            else:
                output.append(f"#define {'A'*a_counter} {word}")
            output_file.append("A"*a_counter+";")
            a_counter += 1

with open("A_FUSCATE.h", "w") as f:
    f.write("\n".join(output))

with open(f"output.{lang}", "w") as f:
    output_str = ""
    for i in output_file:
        if i.startswith("#"):
            output_str+=i+"\n"
        else:
            output_str+=i+"\n"
    f.write(output_str)
