import json

if __name__ == "__main__":
    file_palindrome = open("out/test/spark-palindrome.txt","r")#write mode 
    lines = file_palindrome.readlines() 
    
    print(lines)
    print(len(lines))
    file_palindrome.close() 
    with open('out/test/data.json') as f:
        data = json.load(f)
        print(data)
        print(data["did"])