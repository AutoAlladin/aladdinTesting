class AuctionRate:
    def __init__(self, positionId, rate=None):
        self.positionId = positionId
        if rate is not None:
            self.rate = rate


class AuctionParticipent:
    def __init__(self, name, email, rates=None):
        self.name = name
        self.email = email
        if rates is not None:
            self.rates = rates

