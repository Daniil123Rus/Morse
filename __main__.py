from sys import argv
from data import *

def Starter():
    arguments = argv[1:]

    if len(arguments) < 1:
        print("Compilation error. Specify path to the file.")
        exit()

    if arguments[0].split(".")[1] != "morse":
        print('Compilation error. The compiler is intended for programs with the ".morse" extension.')
        exit()

    return arguments[0]

def Compile(input_file):
    try:
        with open(input_file, "r") as file:
            data = file.read().replace(" ", "").split(";")
            count_line = 0
            compiled_data = """#This code was generated using Morse Compiler 0.1 (MorseLang -> Python 3)
#You can use the code for your own purposes without restrictions.
#Any questions? https://github.com/Daniil123Rus/Morse/issues | https://t.me/daniil_backend_developer
#Thanks for the help: PansanGG_

"""
            for line in data:
                value = ''
                count_line += 1
                real_function = False

                if line == "":
                    continue

                if ":" not in line:
                    print(f"Warning: Failed to compile string {count_line} because it is missing a function. The line was skipped!")
                    continue

                func_name = line.split(":")[0]
                real_func_name = ""

                for function in functions_compile:
                    if func_name.replace(" ", "") == function.replace(" ", ""):
                        real_function = True
                        real_func_name = functions_compile[function]
                        break

                if not real_function:
                    print(f'Warning: Failed to compile string {count_line} because function "{func_name}" does not exist. Line skipped!')
                    continue

                compiled_data += real_func_name

                if len(line.split(":")) < 2:
                    print(f'Warning: Failed to compile "{line}" ({count_line} line) so this was skipped.')
                    continue

                for word in line.split(":")[1].split(" "):
                    try:
                        if word == "":
                            continue

                        value += translate_compile[word]
                    except KeyError:
                        print(f'Warning: Failed to compile "{word}" ({count_line} line) so this was skipped.')
                        continue

                compiled_data += f'("{value}")\n'

        with open("output.py", "w") as file:
            file.write(compiled_data)

        print("Successful compilation. The file was saved in the current directory (output.py)")

    except FileNotFoundError:
        print("Compilation error. The specified file was not found. Please try to specify the full path to the file and try again.")
        exit()

# def Decompile(input_file):
#     print("In developing..")
#     exit()

file = Starter()
Compile(input_file=file)
