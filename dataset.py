
class LinesDataset():
    def __init__(self, n, turns=8): 
        self.n = n
        self.turns = turns

    def __len__(self):
        return self.turns ** self.n
        
    def __getitem__(self, index):
        if not (0 <= index < self.__len__()):
            raise IndexError("Dataset index out of range")
     
        decisions = []
        temp_index = index
        for i in range(self.n):
            power_of_turns = self.turns ** (self.n - 1 - i)
            
            decision_value_0_indexed = temp_index // power_of_turns
            decisions.append(str(decision_value_0_indexed + 1)) 
            temp_index %= power_of_turns 
        return decisions
            
