class BaseStrategy:

    def __init__(self, envelopes):
        self.envelopes = envelopes

    def play(self):
        for counter, envelope in enumerate(self.envelopes):
            if self.perform_strategy(counter) or counter == len(self.envelopes) - 1:
                # When the strategy chooses an envelope this will trigger causing the function to print the envelope
                # number and the money it contains.
                # note: reached the end => must choose
                print(f"Chose envelope number: {counter} \ncontaining: {envelope.money}$")
                self.envelopes[counter].used = True
                return

    def perform_strategy(self, counter):
        """ returns a boolean. should we choose envelope number counter """
        ans = ""
        while ans.lower() not in ["y", "n"]:
            print(f"Envelope number {counter} contains: \n ... \n ... \n ... \n{self.envelopes[counter].money}$!!!!\n "
                  f"Do you CHOOSE this ENVELOPE!?!? y/n")
            ans = input()
        return ans.lower() == 'y'

    def display(self):
        return "BASE STRA-TE-GY"
