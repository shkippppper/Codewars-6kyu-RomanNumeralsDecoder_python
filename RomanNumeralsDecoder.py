
def solution(roman):
    input = list(roman)
    print(input)
    values = ["M","D","C","L","X","V","I"]
    numbers = [1000,500,100,50,10,5,1]
    givenNumber = 0
    numberToGive = 0
    notLastOne = True

    if len(input)<2:
        for x in range(len(values)):
            givenNumber = numbers[values.index(roman)]
        return givenNumber
    else:
        for y in range(len(roman)):
            if y + 1 > len(roman):
                notLastOne = False
                  
            if notLastOne and y > 0:
                if numbers[values.index(input[y])] > numbers[values.index(input[y-1])]:
                    givenNumber = numbers[values.index(input[y])] - 2*(numbers[values.index(input[y-1])])
                else:
                    givenNumber = numbers[values.index(input[y])]

            else:
                givenNumber = numbers[values.index(input[y])]
            numberToGive = numberToGive + givenNumber
        return numberToGive




