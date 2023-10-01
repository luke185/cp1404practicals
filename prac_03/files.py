input_name = input("Name: ")
out_file = open('name.txt', 'w')
print(input_name, file=out_file)
out_file.close()

in_file = open('name.txt', 'r')
file_name = in_file.readline().strip()
in_file.close()
print(f"Your name is {file_name}")


in_file = open('numbers.txt', 'r')
result = int(in_file.readline()) + int(in_file.readline())
in_file.close()
print(result)

total = 0
in_file = open('numbers.txt', 'r')
for line in in_file:
    total = int(line) + total
in_file.close()
print(total)