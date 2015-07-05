function HoldEm_Part1

dealN = 2;
deck = randperm(52);
suits = {'Hearts','Diamonds','Clubs', 'Spades'};
ranks = [strtrim(cellstr(num2str([2:10]'))'), 'Jack', 'Queen', 'King', 'Ace'];

  function [topCard] = popCard(nPop)
      topCard = [];
      if nargin < 1 nPop = 1; end
      for tx = 1:nPop
      topCard = [topCard deck(1)];
      deck(1) = [];
     end
  end 

  function [cardName] = nameCard(in)
     in = in-1;
     rank = mod(in,13)+1;
     suit = fix(in/13)+1;
     cardName = strcat(ranks(rank),{' of '},suits(suit));
  end

  function printHand(hand, header)
  fprintf(1,header);
  for cx = 1:numel(hand)
          fprintf(1,char(strcat(nameCard(hand(cx)))));
          if cx ~= numel(hand)
             fprintf(1,', ');
          end
  end
  fprintf(1,'\n');
  end

playersN = 0;
while playersN < 2 || playersN > 8
  playersN = input("How many players (2-8)? ");
end

for kx = 1:playersN
  players(kx).name = ['CPU #' num2str(kx)];
  players(kx).hand = [];
end
players(1).name = 'Your ';

for dx = 1:dealN
  for px = 1:playersN
    players(px).hand = [players(px).hand popCard()];
  end
end

for px = 1:playersN
  printHand(players(px).hand, char(strcat(players(px).name,{' Hand: '})));
end

% Burn a card.
popCard();
fprintf(1,'\n\n')

printHand(popCard(3),'Flop: ');
printHand(popCard(), 'Turn: ');
printHand(popCard(), 'River: ');

end