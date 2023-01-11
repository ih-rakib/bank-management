""" All about mankind """

class Human : 
    def __init__(self, gender, height, weight) -> None:
        self.gender = gender
        self.height = height
        self.weight = weight
    
class Police(Human) : 
    def __init__(self, gender, height, weight, cases, nationality) -> None:
        super().__init__(gender, height, weight)
        self.cases = cases
        self.nationality = nationality
    
class CsEngineer(Human) : 
    def __init__(self, gender, height, weight, love_to_code, have_passion) -> None:
        super().__init__(gender, height, weight)
        self.love_to_code = love_to_code
        self.have_passion = have_passion

if __name__ == '__main__' :   
    # police = Police('male', 87, 70, True, 'Bangladeshi')
    # print(police.height)

    eng = CsEngineer('male', 78, 57, True, False)
    print(eng.have_passion)

    print('Eng 2')
    eng2 = CsEngineer(gender='male', love_to_code=False, weight=56, height=65,have_passion=False)
    print(eng2)