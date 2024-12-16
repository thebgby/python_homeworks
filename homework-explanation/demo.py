from collections import defaultdict, OrderedDict

# person = defaultdict(list)
person = {}

person['name'] = 'John'

# skills = person.get('skills')
# if not skills:
#     person['skills'] = []

person.setdefault('skills', []).append('c#')

person['skills'].append('python')
person['skills'].append('django')
person['skills'].append('writing')


print(person['skills'])
