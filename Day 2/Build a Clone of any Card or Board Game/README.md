## ⚫⚪ Othello Game ⚪⚫

### Game Play

▪ Othello is a turn-based two-player strategy board game. The players take turns placing pieces--one player white and the other player black--on an 8x8 board in such a way that captures some of the opponent's pieces, with the goal of finishing the game with more pieces of their color on the board.

▪ Every move must capture one more more of the opponent's pieces. To capture, player A places a piece adjacent to one of player B's pieces so that there is a straight line (horizontal, vertical, or diagonal) of adjacent pieces that begins with one of player A's pieces, continues with one more more of player B's pieces, and ends with one of player A's pieces.

### Programming the Game

Factors that require constant attention:

1. Checking moves: A move must be both valid and legal: it must refer to a real square, and it must form a bracket with another piece of the same color with pieces of the opposite color in between.

2. Making moves: When the player makes a move, we need to update the board and flip all the bracketed pieces.

3. Monitoring players: Maintain a list of all legal moves for the players.

Each round consists of:

1. Get a move from the current player.

2. Apply it to the board.

3. Switch players. If the game is over, get the final score.

### Use of MinMax Search Algorithm

▪ Minimax Algorithm is a recursive or backtracking algorithm.

▪ It is used in decision-making and game theory. 

▪ It provides an optimal move for the player assuming that opponent is also playing optimally.

▪ Two Opponent Players: MAX and MIN.

▪ MAX with maximum values and MIN with minimum values.

▪ The minimax algorithm proceeds with depth-first search algorithm then backtracks the tree as in recursion.

### Use of Alpha-Beta Pruning

▪ Optimisation technique for minimax algorithm.

▪ Applied at any depth of tree.

▪ ALPHA: The highest-value choice found so far at any point along the path of Maximizer. The initial value of alpha is -∞.

▪ BETA: The lowest-value choice found so far at any point along the path of Minimizer. The initial value of beta is +∞.

▪ It removes all the nodes which are not affecting the final decision. 

▪ Pruning makes the algorithm fast.

### Functions Used

**update:** Update the board to the screen.

**boardMove:** Move the discs of player and computer on the screen.

**drawScoreBoard:** Display the score on the screen.

**passTest:** Check if the player passes or not

**dumbMove:** Computer’s turn to move disc with difficulty level 1.

**slightlyLessDumbMove:** Computer’s turn to move disc with difficulty level 2.

**decentMove:** Computer will play at an equal level with player with difficulty level 3.

**minimax:** This function contains the minimax algorithm for the game.

**alphaBeta:** This function will apply alpha beta pruning on the minimax tree.

**move:** This function moves the disc in the variables. 

**drawGridBackground:** Draw a check board for the game.

**dumbScore:** Heuristically compares the count of tiles of both the players and returns the score.

**slightlyLessDumbScore:** Gives extra weightage to tiles on the edges and in the corners.

**decentHeuristic:** Weighs corner tiles and edge tiles as positive, adjacent to corners (if the corner is not yours) as negative and counts other tiles as one point.

**finalHeuristic:** Depending upon the stage where the game is (early/mid/end), makes use of heuristics to return the score.

**valid:** Checks if the moves are valid or not.

**clickHandle:** If the move is valid, it make the move. Keeps a track on mouse’s position.

**keyHandle:** Executes restart or quit game depending on which button is clicked.

**create_buttons:** (for UI) Sets the position, colour and size of all the buttons.

**runGame:** (for UI) Sets the game’s starting page’s layout.

**playGame:** Displays the grid background, initializes the starting tokens and now the game is ready to be played.

### Othello Layout
