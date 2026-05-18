import random

patient_name = input('Nhập tên bệnh nhân: ')

gender = input('Nhập giới tính: ')

birth_year = int(input('Nhập năm sinh: '))

phone_number = (input('Nhập số điện thoại: '))

email = input('Nhập email: ')

initial_symptoms = input('Nhập triệu chứng: ')

examination_cost = float(input('Nhập chi phí: '))

random_number = random.randint(100,999)

print('\n---THẺ BỆNH NHÂN')
print('Mã BN      :', 'BN' + str(birth_year) + str(random_number))
print('Tên        :', patient_name)
print('Giới tính  :', gender)
print('Năm sinh   :', birth_year)
print('Điện thoại :', phone_number)
print('Email      :', email)
print('Triệu chứng:', initial_symptoms)
print('Chi phí    :', examination_cost)