from datetime import datetime
import jsonpickle as jsonpickle


class Culture:
    UA = "uk"
    EN = "en"
    RU = "ru"
class LabelType:
    TITLE = "title"
    DESCRIPTION = "description"

class Label:
    def __init__(self,culture,type,value):
        self.culture = culture,
        self.type = type,
        self.value = value

class Label_UA:
    def __init__(self,type,value):
        self.culture = Culture.UA,
        self.type = type
        self.value = value
class Label_UA_Title:
    def __init__(self,value):
        self.culture = Culture.UA
        self.type = LabelType.TITLE
        self.value = value
class Label_UA_Description:
    def __init__(self,value):
        self.culture = Culture.UA
        self.type = LabelType.DESCRIPTION
        self.value = value

class Label_EN:
    def __init__(self,type,value):
        self.culture = Culture.EN
        self.type = type
        self.value = value
class Label_EN_Title:
    def __init__(self,value):
        self.culture = Culture.EN
        self.type = LabelType.TITLE
        self.value = value
class Label_EN_Description:
    def __init__(self,value):
        self.culture = Culture.EN
        self.type = LabelType.DESCRIPTION
        self.value = value

class Label_RU:
    def __init__(self, type,value):
        self.culture = Culture.RU
        self.type = type
        self.value = value
class Label_RU_Title:
    def __init__(self,value):
        self.culture = Culture.RU
        self.type = LabelType.TITLE
        self.value = value
class Label_RU_Description:
    def __init__(self,value):
        self.culture = Culture.RU
        self.type = LabelType.DESCRIPTION
        self.value = value



class Position:
    def __init__(self, minimalStep, maximalStep, labels, idd):
        self.minimalStep = minimalStep
        self.maximalStep = maximalStep
        self.labels =labels
        self.idd = idd


class AuctionRegistration:

    def __init__(self,
                 type, reverse,
                 budget, currency,
                 dateStart, dateEnd,
                 additionalStepTime, additionalStepLimit,
                 labels,
                 positions,
                 ownerEmail):
        self.type = type
        self.reverse = reverse
        self.budget = budget
        self.currency = currency
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.additionalStepTime = additionalStepTime
        self.additionalStepLimit = additionalStepLimit
        self.labels = labels
        self.positions = positions
        self.ownerEmail = ownerEmail

    def add_position(self,  minimalStep, maximalStep, labels, idd=None):
        self.positions.append(Position( minimalStep, maximalStep, labels, idd=None))

if __name__ == "__main__":

    au_labels = [Label_UA_Title("auction ua title"),
                      Label_UA_Description("auction ua label description"),
                      Label_EN_Title("auction en label title"),
                      Label_EN_Description("auction en label description"),
                      ]

    pos_labels = [Label_UA_Title("position ua title"),
                 Label_UA_Description("position ua label description"),
                 Label_EN_Title("position en label title"),
                 Label_EN_Description("position en label description"),
                 ]

    ar = AuctionRegistration(
            type = "SmartClose",
            reverse = True,
            budget = 10000,
            currency= "UAH",
            dateStart = datetime.strptime("2018-03-14T10:30:47+0200",'%Y-%m-%dT%H:%M:%S%z'),
            dateEnd = datetime.strptime("2018-03-14T13:30:47+0200",'%Y-%m-%dT%H:%M:%S%z'),
            additionalStepTime = 2,
            additionalStepLimit = 4,
            labels = au_labels,
            positions=[],
            ownerEmail="owner@mail.com"

    )

    for i in range(50):
        ar.add_position(20+i,30+i, pos_labels)


    print(jsonpickle.encode(ar, unpicklable=False))