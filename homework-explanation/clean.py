import regex

with open('sample.txt') as f:
    text = f.read()

cleaned_data = text.lower().replace(".", '').replace(',', '').replace('\n', ' ').split()
print(cleaned_data)