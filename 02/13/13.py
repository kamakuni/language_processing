def text_to_array(file_name):
    with open(file_name,"r") as file:
        array = file.readlines()
    return array

def main():
    data1 = text_to_array("col1.txt")
    data2 = text_to_array("col2.txt")

    with open("merged.txt","w") as file:
        for col1,col2 in zip(data1, data2):
            file.write(col1.replace("\n","\t")+col2)

if __name__ == "__main__":
    main()