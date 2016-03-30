from words_set import x, xx, xxx, bignumbers


class NumbToWords(object):
    def __init__(self, my_numb):
        self.my_numb = my_numb

    def NumbToWords(self, number):
        '''
        This method converts unique 0-999 numbers to string label
        :param number: get each [000] number to convert
        :return: return each converted 0-999 number to label
        '''
        
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
        '''
        It splits given number to a three digits blocks: 1543543 = [154,354,003]
        :return: list of thousandths from given number
        '''

        self.my_list = []
        while True:
            self.my_list.append(self.my_numb[-3:])
            self.my_numb = self.my_numb[:-3]
            if self.my_numb == '':
                break
        return self.my_list

    def finally_string(self):
        '''
        In this method Id of elements [123,123,123] is assigns to Id of ['tysiac','milion','miliard','trylion'].
        :return: returns string of numbers labels
        '''

        finally_string = []
        z = 0
        for elem in self.my_list:
            z += 1
            # Skip zeros in given number (avoid: "one milion zero zero zero zero zero fifty")
            if elem != '000':
                temp = self.NumbToWords(int(elem))
                finally_string.append(str(temp) + ' ' + bignumbers[z - 1])
        return (' - ').join(finally_string[::-1])