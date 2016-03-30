from words_set import x, xx, xxx, bignumbers

def NumbToWords(number):
    word = ''
    str_number = str(number)
    if number >= 0 and number < 20:
        word = x[number]
        return word
    if number >= 20 and number < 100:
        word = xx[(number//10)-2] + ' ' + x[int(str_number[-1])]
        return word
    if number >= 100 and number < 1000:
        div_number = divmod(number,100)
        if div_number[1] < 20:
            word = xxx[number//100-1] + ' ' +  x[div_number[1]]
            return word
        else:
            word = xxx[number//100-1] + ' ' + xx[int(str_number[1])-2] + ' ' + x[int(str_number[2])]
            return word

a = NumbToWords(123)