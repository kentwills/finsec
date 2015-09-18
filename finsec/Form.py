class Form(object):

    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)

    def financials(self, dictionary):
        self.financials = dictionary
