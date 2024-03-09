from infrastructure.metta_reader import read_metta_file

value = read_metta_file("test_files/compound_nodes.metta")
for i in value:
    print(i.strip())
