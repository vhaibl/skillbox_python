file_name = 'events.txt'


class Parser:
    def __init__(self, file_name):
        self.i =0
        self.filtered = {}
        self.file_name = file_name
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                filter = line[1:17]
                self.create(filter, line)
        print('__________________MINUTE STATS___________________\n')


    def __iter__(self):
        return self

    def __next__(self):
        for line, xjin self.filtered.items():
            pass
        yield line, xjin


    def create(self, filter, line):
        if 'NOK' in line:
            if filter in line:
                if filter in self.filtered:
                    self.filtered[filter] += 1
                else:
                    self.filtered[filter] = 1
            else:
                self.filtered = {filter: 1}

grouped_events = Parser(file_name='events.txt')  # Итератор или генератор? выбирайте что вам более понятно
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
