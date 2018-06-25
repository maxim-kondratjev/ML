import requests

def mediane(values):
	sorted_values = sorted(values)
	return sorted_values[len(values)//2]

names=['machine learning', 'python', 'data science', 'машинное обучение', 'big data', 'data analytics']
vacancies = {name:(requests.get('https://api.hh.ru/vacancies?text={}'.format(name))).json()['items'] for name in names}
print(vacancies)
#salaries = {name: med(list(map(lambda x: x.get('salary'),filter(lambda x:False if x is None, cur.salary))))
				#for name, car in vacancies.items()}