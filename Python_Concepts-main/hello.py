from modules import addition
print ("Hello, World!");

names =["Karthik", "Manju","Srinisha", "soujitth"];
print(names);
names.append("sri");
print(names);
print(names.count("sri"));

# tupels
colors = ("red", "green", "blue");
print(colors);
colors = list(colors);
print(colors);

set1 = {"apple", "banana", "cherry","apple"};
print(set1);

students = {"Karthik": 21, "Manju": 22, "Srinisha": 20};
print(students);

def add_numbers(a, b):
    return a + b;

#a= int(input("Enter first number: "));
#b= int(input("Enter second number: "));

#result = add_numbers(a, b);
#print(result);

for st in students:
    print(st);

print(addition.add(5, 10));

try:
    print(10 / 0);
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.");
finally:
    print("Execution completed.");

with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample text file.");

with open("sample.txt", "r") as file:
    content = file.read();
    print(content);

with open("sample.txt", "a") as file:
    file.write("\nThis line is appended to the file.");

with open("sample.txt", "r") as file:
    content = file.read();
    print(content);

# Test git commit