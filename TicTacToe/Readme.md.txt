# Tic Tac Toe

This is a simple tic tac toe game complete with difficulty levels that can be set using the minimax algorithm

   
   |   |   
---|---|---
   |   |   
---|---|---
   |   |   
   
## Rules
---

The game is played on a 3x3 grid.

Player X and player O take turns placing their symbol (X or O) on an empty cell.

The game ends when either:
- One player places three of their symbols in a row, either horizontally, vertically, or diagonally, in which case that player wins.
- All cells are filled with symbols and no player has three in a row, in which case the game is a draw.

Players take turns in placing their symbols until the game ends.

Have fun!



## Minimax Algorithm

Minimax (sometimes MinMax, MM[1] or saddle point[2]) is a decision rule used in artificial intelligence, decision theory, game theory, statistics, and philosophy for minimizing the possible loss for a worst case (maximum loss) scenario. When dealing with gains, it is referred to as "maximin" – to maximize the minimum gain. Originally formulated for several-player zero-sum game theory, covering both the cases where players take alternate moves and those where they make simultaneous moves, it has also been extended to more complex games and to general decision-making in the presence of uncertainty.
Read more [Here](https://en.wikipedia.org/wiki/Minimax)

![Minimax Algorithm image](https://www.gstatic.com/education/formulas2/472522532/en/minimax.svg)

Where: 
- ![](https://www.gstatic.com/education/formulas2/472522532/en/minimax_minimax_var_1.svg) = index of the player of interest
- ![](https://www.gstatic.com/education/formulas2/472522532/en/minimax_minimax_var_2.svg) = denotes all other players except player i
- ![](https://www.gstatic.com/education/formulas2/472522532/en/minimax_minimax_var_3.svg) = action taken by player i
- ![](https://www.gstatic.com/education/formulas2/472522532/en/minimax_minimax_var_4.svg) = actions taken by all other players
- ![](https://www.gstatic.com/education/formulas2/472522532/en/minimax_minimax_var_5.svg) = value function of player i
