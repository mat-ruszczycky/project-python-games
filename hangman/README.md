# Hangman Game Features Checklist

## Core Features
- [x] **Word Selection**: Randomly select a word from a predefined word list.
- [x] **Letter Guessing**: Players can input a letter to guess the word.
- [x] **Tries**: The player has 6 incorrect guess attempts.
- [x] **Game Replay**: Prompt the player to play again after each round.

## Future Release Features

### 1. Difficulty Levels
- [ ] **Easy**: Short words (4-5 letters) and 8 tries.
- [ ] **Medium**: Medium words (6-8 letters) and 6 tries.
- [ ] **Hard**: Long words (9+ letters) and 4 tries.

### 2. Hint System
- [ ] **Hints**: Allow the player to request a hint that reveals one letter (with a penalty of tries).

### 3. Score Tracking
- [ ] **Score**: Track and display the player's score based on remaining guesses and difficulty level.

### 4. Word Categories
- [ ] **Categories**: Add word categories like "Animals", "Countries", "Movies", etc.
- [ ] **Category Selection**: Allow the player to choose a word category before starting the game.

### 5. Multiplayer Mode
- [ ] **Player 1 Input**: One player can input a custom word.
- [ ] **Player 2 Guessing**: The other player tries to guess the word.
- [ ] **Hint Option**: Optionally allow Player 1 to provide a hint.

### 6. Hangman Visual Progress
- [ ] **ASCII Art**: Display a visual representation of the hangman figure with each incorrect guess.

### 7. Leaderboard
- [ ] **Top Scores**: Track high scores and display a leaderboard over multiple games.
- [ ] **Persistent Storage**: Save scores in a file (e.g., JSON or SQLite).

### 8. Time-Based Mode
- [ ] **Timed Guesses**: Players must guess within a set time limit, or they lose a try.

### 9. Word Definition or Fun Facts
- [ ] **Post-Game Info**: Display the word’s definition or fun trivia after the game ends.

### 10. Themed Games
- [ ] **Themes**: Add different themes (e.g., Halloween, space) that affect word selection and visuals.
- [ ] **Theme-Based ASCII Art**: Update hangman art and UI based on the selected theme.

### 11. Enhanced Input Validation
- [ ] **Invalid Input Feedback**: Provide detailed feedback for invalid guesses (e.g., non-letter characters, repeated guesses).
- [ ] **Repeated Guesses**: Notify players if they've guessed the same letter twice.

### 12. Streaks and Achievements
- [ ] **Win Streaks**: Track consecutive wins across games.
- [ ] **Achievements**: Implement unlockable achievements for milestones (e.g., "First Win", "10 Wins in a Row").

### 13. Random Event Cards
- [ ] **Extra Guesses**: Random event gives the player an extra guess.
- [ ] **Word Hints**: Random event reveals a letter.
- [ ] **Freeze Guess**: Next incorrect guess doesn't count as a penalty.

### 14. Customizable Settings
- [ ] **Tries Adjustment**: Let players adjust the number of tries.
- [ ] **Toggle Hints**: Allow players to enable/disable hints.
- [ ] **Difficulty Selection**: Let players choose the word difficulty before starting the game.
