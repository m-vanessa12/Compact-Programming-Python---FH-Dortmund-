phones = [
    {'make': 'Google', 'model': 216, 'color':'Black'},
    {'make': 'Mi Max', 'model': '2', 'color':'Gold'},
    {'make': 'Google', 'model': 7, 'color':'Blue'}
]

sorted_phones = sorted(
    phones,
    key=lambda phone: int(phone['model']),
    reverse=True
)

print(sorted_phones)