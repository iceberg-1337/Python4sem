'''
class Person:
    def __init__(self, arg_name, arg_age):
        self.name = arg_name
        self.age = arg_age

    def __str__(self):
        return 'Имя {}, Возраст {}'.format(self.name, self.age)


class Student(Person):
    def __init__(self, arg_name, arg_age, st_id):
        super().__init__(arg_name, arg_age)
        self.id = st_id
        self.marks = {}

    def new_marks(self, disc, mark):
        self.marks.update({disc: mark})

    def __str__(self):
        s = super().__str__()
        return s + '\n' + str(self.marks)


class Reader(Person):
    def __init__(self, arg_name, arg_age, lc_id):
        super().__init__(arg_name, arg_age)
        self.id = lc_id
        self.lc = {}

    def new_book(self, book_id, date):
        self.lc.update({book_id: date})

    def get_date(self, book_id):
        return self.lc.get(book_id)

    def print_lc(self):
        return self.lc

    def __str__(self):
        s = super().__str__()
        return s + '\n' + 'Номер читательского билета: ' + self.id


person1 = Person('Ivan', 20)
student1 = Student('Petr', 19, '912308')
student1.new_marks('Math', 5)
print(person1)
print(student1)

reader1 = Reader('Egor', 19, '41983567132')
reader1.new_book(1, '01.04.2021')
reader1.new_book(2, '03.02.2020')
print(reader1)
print(reader1.get_date(1))
print(reader1.print_lc())
'''

import struct


def create_d_struct(data, list_addr):
    res = []
    for addr in list_addr:
        d1 = struct.unpack('<b', data[addr:addr + 1])
        d2 = struct.unpack('<HI', data[addr + 1:addr + 7])
        d2 = list(struct.unpack('<' + 'h' * d2[0], data[d2[1]:d2[1] + 2 * d2[0]]))
        res.append({'D1': d1, 'D2': d2})
    return res


def f3(data):
    a1 = struct.unpack('<d', data[4:12])[0]
    a2 = struct.unpack('<f', data[12:16])[0]
    a4 = struct.unpack('<H', data[34:36])[0]
    a5 = struct.unpack('<I', data[36:40])[0]
    a6 = list(struct.unpack('<3H', data[40:46]))
    a6 = create_d_struct(data, a6)

    b1 = struct.unpack('<H', data[16:18])[0]
    b2 = struct.unpack('<H', data[18:20])[0]
    b3 = struct.unpack('<q', data[20:28])[0]
    b4 = struct.unpack('<IH', data[28:34])
    b44 = ''
    for i in range(int(b4[0])):
        b44 += struct.unpack('<' + 's' * b4[0], data[b4[1]:b4[1] + 1 * b4[0]])[i].decode('UTF-8')

    c1 = struct.unpack('<H', data[b2:b2 + 2])[0]
    c2 = struct.unpack('<IH', data[b2 + 2:b2 + 8])
    c22 = ''
    for i in range(int(c2[0])):
        c22 += list(struct.unpack('<' + 's' * c2[0], data[c2[1]:c2[1] + 1 * c2[0]]))[i].decode('UTF-8')
    c3 = struct.unpack('<i', data[b2 + 8:b2 + 12])[0]
    c4 = struct.unpack('<b', data[b2 + 12:b2 + 13])[0]
    c5 = struct.unpack('<q', data[b2 + 13:b2 + 21])[0]

    out_dict = {'A1': a1,
                'A2': a2,
                'A3': {
                    'B1': b1,
                    'B2': {
                        'C1': c1,
                        'C2': c22,
                        'C3': c3,
                        'C4': c4,
                        'C5': c5,
                    },
                    'B3': b3,
                    'B4': b44,
                },
                'A5': a5,
                'A6': a6
                }
    return out_dict


'''print(f31(b'SLBEJ8"R\xea\xa3\xe6?X\x81\x8a\xbeo\xf34\x00\x82\xd2H%\x124\xfb\xd6'
b'\x03\x00\x00\x00I\x00\xed\xa4\xaa\x91\xef\xe2V\x00g\x00v\x00sbyprm'
b'\xb6K\x06\x00\x00\x00.\x00R\xc0\x97\x0cAlN2\xd6\x96\xb3\x02[aqa\x93\xe2 \x9d'
b'\xb3\xe1\xbc\x1d,\x7f\xb4\x05\x00L\x00\x00\x00\xd3.p\xf2W6\xbc'
b'\x80\x80\xb5\xee\x05\x00]\x00\x00\x00\x12[.\xbe\xa3^\xdb\xabm\x04'
b'\x00n\x00\x00\x00'))'''


def f31(data):
    b11 = struct.unpack('>H', data[4:6])[0]
    b12 = struct.unpack('>B', data[6:7])[0]
    b13 = struct.unpack('>b', data[7:8])[0]
    b21 = struct.unpack('>H', data[8:10])[0]
    b22 = struct.unpack('>B', data[10:11])[0]
    b23 = struct.unpack('>b', data[11:12])[0]

    a2 = struct.unpack('>B', data[12:13])[0]
    a3 = struct.unpack('>i', data[13:17])[0]
    a4 = struct.unpack('>H', data[c1:c1+4])[0]
    a5 = struct.unpack('>i', data[19:23])[0]
    a6 = struct.unpack('>d', data[23:31])[0]

    c1 = struct.unpack('>I', data[32:])
    c2 = struct.unpack('>I', data[32:36])
    out_strict = {'A1':((b11, b12, b13),
                  (b21, b22, b23)),
                  'A2': a2,
                  'A3': a3,
                  'A4': a4,
                  'A5': a5,
                  'A6': a6,
                  'C1': c1,
                  'C2': c2
    }

    return out_strict

print(f31((b'ULAA\x1e\x8b\xa6\x9f\xa2\xfc\xcd\t\x15\xef\xbe\xeb\x11\x00Y$\x13e\xe6\xbf'
b'\xdd\x01\x10\xcd\x8eJX\xacZ\xd9\xcb>\xe1\x11y?LY\r?8\xb6s\xbf[\xa6\xed\xb7'
b'^k\xe2\x96\xbb\xb8\xf6\x17\x05Q\x1c\xb3\x94\xb3\xaa\x10\x19m\xea\x00'
b'\x00\x00\x04\x00#\x80\xe8_\x90\xe7N\\\xf7\x00\x02\x003?\x98J\n\x15\xd5\xa2'
b'\x885\xc5?\xac\x1f]\xc2\x84\x89\x80\xbf\xda\xea\x95\xdcQe\xf4\xde\r\x10\xc97'
b'6\x9f.Euv\x89\x97\xa4T\xef\x9c\xc6\x99\xa02\xf3l\xd6\x00\x02\x00\x1f\x007')))




