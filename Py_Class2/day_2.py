__author__ = 'FRSummit'
if __name__ == "__main__":
    File = file("test_file.txt", "w+")
    for i in range(1000):
        File.write(str(i)+"\t"+str(i+10)+"\n")
        File.close()