# 변수, 자료형, 함수, 조건문, 반복문

professor_wizards = [
    {'name': '덤블도어', 'age': 116},
    {'name': '맥고나걸', 'age': 85},
    {'name': '스네이프', 'age': 60},
]

for wizard in professor_wizards:
    if wizard['age'] > 100:
        print(wizard['name'])