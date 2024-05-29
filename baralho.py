import collections
from random import choice

Card = collections.namedtuple('Card',['rank','suit'])

class FrencDeck:
    ranks = [str(n) for n in range(2,11)] + list ('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self) -> None:
        self._cards = [Card(rank,suit) for suit in self.suits
                                        for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self,position):
        return self._cards[position]
    

    
deck = FrencDeck()
print(len(deck))

#print(deck[0])
#print(deck[-1])

print(choice(deck))


for card in deck: 
    print(card)