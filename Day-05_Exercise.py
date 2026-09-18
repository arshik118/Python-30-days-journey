# Exercises: Level 1
# 1. Declare an empty list
lst = list()
print(lst)

# 2.Declare a list with more than 5 items
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
print(fruits)

# 3.Find the length of your list
print(len(fruits))

# 4.Get the first item, the middle item and the last item of the list
print(fruits[0])
print(fruits[2])
print(fruits[5])

# 5.Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Arshi Khan', 20, 5.9, 'Unmarried', '10 Gulabi Nagar 2nd Bhankrota Jaipur']

# 6.Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print('Number of companies in the list are: ', len(it_companies))
print(it_companies[0],it_companies[3], it_companies[len(it_companies)-1])

it_companies[3] = 'Deloitte'
print(it_companies)
it_companies.append('Apple')
it_companies.insert(3, 'Tesla')
print(it_companies[0].upper())
res = '# '.join(it_companies)
print(res)
does_exist = 'Oracle' in it_companies
print(does_exist)

it_companies.sort()
print(it_companies)
it_companies = sorted(it_companies, reverse=True)
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[:3])
print(it_companies[6:])
print(it_companies[3:5])
it_companies.pop(0)
print(it_companies)
it_companies.pop(3)
print(it_companies)
it_companies.pop()
print(it_companies)
it_companies.clear()
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
lst3 = front_end + back_end
print(lst3)
front_end.extend(back_end)
print(front_end)
full_stack = front_end
front_end.append('python')
front_end.append('SQL')
print(front_end)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_ages = min(ages)
print(min_ages)
max_ages = max(ages)
print(max_ages)
total_age = min_ages + max_ages
print(total_age)

ages.sort()
print(ages)

median = ages[len(ages)//2 - 1] + ages[len(ages)//2] // 2
print('Median:', median)


i = 0
sum = 0

while i < len(ages):
    sum += ages[i]
    i += 1

avg = sum / len(ages)
print('Average:', avg)

range = max_ages - min_ages
print(range)

min_difference = abs(min_ages - avg)
max_difference = abs(max_ages -  avg)

print('Min difference from average is: ', min_difference)
print('Max differnce from average is:', max_difference)

from countries import country
n = len(country)
print('Length of the countries:', n)

middle_country = n // 2
print('Middle country:', country[middle_country])

middle = (len(country) + 1 )// 2

first_half = country[:middle]
second_half = country[middle:]

print(first_half)
print(second_half)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
c, ru, us, *scandic = countries
print(c)
print(ru)
print(us)
print(scandic)
