import random
from math import inf


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


class Automatic_BaseStrategy(BaseStrategy):

    def __init__(self, envelopes):
        super().__init__(envelopes)
        self.chosen_one = random.randint(0, len(self.envelopes))

    def perform_strategy(self, counter):
        """ chose the envelope numbered: self.chosen_one """
        return counter == self.chosen_one

    def display(self):
        return "Automatic Strategy"


class N_max_strategy(BaseStrategy):

    def __init__(self, envelopes):
        super().__init__(envelopes)
        self.N = 1
        self.maxes_counter = 0
        self.curr_max = -inf


    def perform_strategy(self, counter):
        """ chose the envelope numbered: self.chosen_one """
        if counter == 0:  # reset. allows for multiple runs with the same instance
            self.maxes_counter = 0
            self.curr_max = -inf
        m = self.envelopes[counter].money
        if m >= self.curr_max:
            self.maxes_counter += 1
            self.curr_max = m
        return self.maxes_counter == self.N

    def display(self):
        return "N max Strategy"
