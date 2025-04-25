with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged_file.txt", "w") as merged:
    lines1, lines2 = f1.readlines(), f2.readlines()
    for i in range(max(len(lines1), len(lines2))):
        if i < len(lines1): merged.write(lines1[i])
        if i < len(lines2): merged.write(lines2[i])
print("Files merged successfully.")
