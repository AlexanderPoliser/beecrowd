salary = float(input())

if salary <= 400:
    salary_percentual = 15
elif salary <= 800:
    salary_percentual = 12
elif salary <= 1200:
    salary_percentual = 10
elif salary <= 2000:
    salary_percentual = 7
elif salary > 2000:
    salary_percentual = 4

salary_reajustment = (salary * salary_percentual) / 100
new_salary = salary_reajustment + salary
print(f"Novo salario: {new_salary:.2f}")
print(f"Reajuste ganho: {salary_reajustment:.2f}")
print(f"Em percentual: {salary_percentual} %")