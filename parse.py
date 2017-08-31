import docx
import sys

def main(argv):
    if argv.size() != 3:
        print("Usage: parse.py input.doxc output.txt")
        return -1
    text = read_file(argv[1])
    print(text)
     
    


def read_file(filename):
    doc = Document(filename)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return '\n'.join(text)
        


def print_to_gedcom(filename):
    file = open(filename, "w")
    #start header
    file.write("0 HEAD\n")
    file.write("1 SOUR wordToGedcom\n")
    file.write("2 NAME Personal Ancestral File\n")
    file.write("2 VERS 5.5\n")
    file.write("1 DATE 31 AUG 2017\n")
    file.write("1 GEDC\n")
    file.write("2 FORM LINEAGE-LINKED\n")
    file.write("1 CHAR ANSEL")
    #end header

    #start individual records
    


    #end individual records

    #start family record



    #end family records

    file.close()

if __name__ == "__main__":
    main(sys.argv)


