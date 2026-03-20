with open(r"C:\Users\Адильхан\Desktop\pp2\work\Practice6\example.txt", "w") as file:
    file.write("Hello\n")
    file.write("Python\n")
    file.write("World\n")


with open(r"C:\Users\Адильхан\Desktop\pp2\work\Practice6\example.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(line1)
    print(line2)