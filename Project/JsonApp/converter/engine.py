from words_set import x, xx, xxx, bignumbers

class NumbToWords(object):
    def __init__(self, my_numb):
        self.my_numb = my_numb

    def NumbToWords(self, number):
        word = ''
        str_number = str(number)
        if number >= 0 and number < 20:
            word = x[number]
        if number >= 20 and number < 100:
            word = xx[(number // 10) - 2] + ' ' + x[int(str_number[-1])]
        if number >= 100 and number < 1000:
            div_number = divmod(number, 100)
            if div_number[1] < 20:
                word = xxx[number // 100 - 1] + ' ' + x[div_number[1]]
            else:
                word = xxx[number // 100 - 1] + ' ' + xx[int(str_number[1]) - 2] + ' ' + x[int(str_number[2])]
        return word

    def generate_000(self):
        self.my = self.my_numb
        self.my_list = []
        while True:
            self.my_list.append(self.my[-3:])
            self.my = self.my[:-3]
            if self.my == '':
                break
        return self.my_list

    def finally_string(self):
        finally_string = []
        z = 0
        for elem in self.my_list:
            z += 1
            if elem != '000':
                temp = self.NumbToWords(int(elem))
                finally_string.append(str(temp) + ' ' + bignumbers[z - 1])
        return (' - ').join(finally_string[::-1])