"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)

    for i in range(len(data)):
        print(f"{data[i][0]} is taught by {data[i][1]} and has {data[i][2]} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data_entries = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data_entries.append(parts)
    input_file.close()
    return data_entries


main()
