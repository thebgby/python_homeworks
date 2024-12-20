N = int(input("Nechta qator kiritmoqchisiz: "))

universities = []

for _ in range(N):
    user_input = input("Enter: ") # California Institute of Technology , 2175, 37704
    words = [word.strip() for word in user_input.split(',')]
    for i in range(1, 3):
        words[i] = int(words[i])
    universities.append(words)
    
print(universities)
