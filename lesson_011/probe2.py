class PrimeNumbers:

    def __init__(self, n, zfilter):
        self.a = []
        self.n = n
        self.b = 1
#        self.zfilter = zfilter
        self.checklist = {'1': self.is_pal, '2': self.hasthreenines, '3': self.is_lucky,
                          '4': self.is_luckynines, '5': self.is_palnines, '6': self.is_luckypal}
        self.check = self.checklist[zfilter]

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
                if self.check(): return self.b

    def sum_digits(self, numn):
        return sum(map(int, numn))

    def hasthreenines(self):
        if '999' in str(self.b):
            return True

    def is_lucky(self):
        self.strnumber = str(self.b)
        center = len(self.strnumber) // 2
        return self.sum_digits(self.strnumber[:center]) == self.sum_digits(self.strnumber[-center:])

    def is_luckynines(self):
        self.strnumber = str(self.b)
        center = len(self.strnumber) // 2
        return self.sum_digits(self.strnumber[:center]) == self.sum_digits(self.strnumber[-center:]) \
               and '999' in str(self.b)

    def is_luckypal(self):
        self.strnumber = str(self.b)
        center = len(self.strnumber) // 2
        return self.sum_digits(self.strnumber[:center]) == self.sum_digits(self.strnumber[-center:]) \
               and str(self.b) == str(self.b)[::-1] and int(self.b) > 10

    def is_pal(self):
        return str(self.b) == str(self.b)[::-1] and int(self.b) > 10

    def is_palnines(self):
        return str(self.b) == str(self.b)[::-1] and int(self.b) > 10 and '999' in str(self.b)

    def nocheck(digit):
        return True


prime_number_iterator = PrimeNumbers(n=100000, zfilter='1')
print('Фильтры: 1 - Палиндромное, 2 - 999 в номере, 3 - Счастливое, 4 - Счастливое и 999, 5 - Палиндромное и 999,'
      ' 6 - Палиндромное и Счастлтивое')
for number in prime_number_iterator:
    print(number)
