import commands

test_file_path = "testfile.txt"


def write_to_test_file(text: str):
    with open(test_file_path, "w") as f:
        f.write(text)
    pass


def compile_by_jar():
    commands.getstatusoutput('ls')
