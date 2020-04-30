class PrimeNumbers:

    def __init__(self, n, zfilter):
        self.a = []
        self.n = n
        self.b = 1
        self.zfilter = zfilter

    def __iter__(self):
        self.b = 1
        return self

    def __next__(self):
        while True:
            self.b += 1
            self.strnumber = str(self.b)
            if self.b >= self.n:
                raise StopIteration()
            for number in self.a:
                if self.b % number == 0:
                    break
            else:
                self.a.append(self.b)
                if self.zfilter == '1':
                    if self.is_pal():
                        return self.b
                elif self.zfilter == '2':
                    if self.hasthreenines():
                        return self.b
                elif self.zfilter == '3':
                    if self.is_lucky():
                        return self.b
                elif self.zfilter == '4':
                    if self.is_lucky() and self.is_pal():
                        return self.b
                elif self.zfilter == '5':
                    if self.is_lucky() and self.hasthreenines():
                        return self.b
                elif self.zfilter == '5':
                    if self.is_pal() and self.hasthreenines():
                        return self.b
                else:
                    return self.b

    def sum_digits(self, numn):
        return sum(map(int, numn))

    def hasthreenines(self):
        if '999' in str(self.b):
            return True

    def is_lucky(self):
        center = len(self.strnumber) // 2
        return self.sum_digits(self.strnumber[:center]) == self.sum_digits(self.strnumber[-center:])

    def is_pal(self):
        return str(self.b) == str(self.b)[::-1] and int(self.b) > 10

    def nocheck(digit):
        return True


prime_number_iterator = PrimeNumbers(n=100000, zfilter='5')
print('Фильтры: 1 - Палиндромное, 2 - 999 в номере, 3 - Счастливое, 4 - Счстливе и палиндромное, 5 - Счастливое и 999,'
      ' 6 - Палиндромное и 999')
for number in prime_number_iterator:
    print(number)
