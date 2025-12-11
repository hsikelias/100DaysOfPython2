# Function Problem-Solving Worksheet — 20 Exercises (Beginner → Intermediate)

This worksheet helps you get comfortable decomposing problems into functions, using if/while control flow, handling state, and building small CLI projects incrementally. Read the "Techniques" section first, then work the exercises in order. Each exercise includes: goal, suggested function signatures, hints, and quick tests you can use as assertions.

---

SECTION A — Techniques: How to approach problems and design functions (human English)

1. Read the problem and restate it in one sentence (the goal).
2. Write a few example inputs and expected outputs (concrete examples).
3. Identify inputs (what the function needs) and outputs (what it should return).
4. Break the task into 2–6 small steps (one sentence per step). Each step often becomes a function.
5. For each step, choose data structures that match the task (numbers, lists, dicts).
6. Decide which functions should be "pure" (return values only) and which handle IO (print/input). Prefer pure logic functions so you can test them.
7. Implement the "happy path" first: assume valid inputs and no edge cases.
8. Add validation and edge-case handling next (e.g., empty lists, negative numbers, invalid strings).
9. Write small tests or use assert statements to verify each function works.
10. Refactor: if a function is doing two things, split it. Give clear names.
11. When stuck, write pseudocode or draw the flow (while? if? nested?). Convert each pseudocode line into a function call.

Quick debugging heuristics:
- Print intermediate values.
- Test smallest components individually.
- Replace complex expressions with multiple simple variables for clarity.
- Use early returns to avoid deep nesting:
  - if invalid: return / raise
  - else: continue

Naming conventions that help your logic:
- Actions: verbs (calculate_total, is_valid_bet, deal_card).
- Data retrieval: get_ prefix (get_input, get_choice).
- Mutations: update_ prefix (update_balance).

---

SECTION B — Exercises (20). Suggested order: do them sequentially. Time estimates are approximate.

Exercises 1–5: Fundamental function practice (10–20 minutes each)

1) Even or Odd
- Goal: Write a function that returns whether a number is even.
- Functions:
  - is_even(n: int) -> bool
- Hints: Use n % 2 == 0
- Tests:
  - assert is_even(2) is True
  - assert is_even(7) is False

2) Sum of Range
- Goal: Return sum of integers from a to b inclusive.
- Functions:
  - sum_range(a: int, b: int) -> int
- Hints: handle a > b by swapping or returning 0
- Tests:
  - assert sum_range(1, 5) == 15
  - assert sum_range(5, 1) == 15 or define behavior

3) Digit Sum
- Goal: Given an integer, return the sum of its digits.
- Functions:
  - sum_digits(n: int) -> int
- Hints: work with abs(n) then str(n) or use while n > 0
- Tests:
  - assert sum_digits(123) == 6
  - assert sum_digits(-12) == 3

4) Factorial (iterative)
- Goal: Iteratively compute n!
- Functions:
  - factorial(n: int) -> int
- Hints: handle 0! = 1, negative -> raise ValueError
- Tests:
  - assert factorial(5) == 120
  - assert factorial(0) == 1

5) Palindrome Checker
- Goal: Check if a string reads the same backward.
- Functions:
  - is_palindrome(s: str) -> bool
- Hints: normalize case and remove non-alphanumeric if desired
- Tests:
  - assert is_palindrome("racecar") is True
  - assert is_palindrome("Hello") is False

Exercises 6–10: Decomposition + control flow (20–40 minutes each)

6) Vowel Counter
- Goal: Count vowels in a string and return a dict of counts.
- Functions:
  - count_vowels(s: str) -> dict  # {'a': n, 'e': m, ...}
- Hints: iterate, lower, check membership in "aeiou"
- Tests: count_vowels("Hello") -> {'e':1, 'o':1, ...0}

7) Simple Shopping Cart
- Goal: Given items with prices, compute subtotal, tax, and total.
- Functions:
  - calculate_subtotal(items: list[float]) -> float
  - calculate_tax(subtotal: float, rate: float) -> float
  - calculate_total(subtotal: float, tax: float) -> float
- Hints: separate pure calculations from printing receipts
- Tests:
  - subtotal = calculate_subtotal([10, 5]) -> 15
  - tax = calculate_tax(15, 0.08) -> 1.2

8) Bank Account (stateful)
- Goal: Simulate simple account with deposit and withdraw.
- Functions:
  - create_account(start_balance=0) -> dict
  - deposit(account: dict, amount: float) -> None
  - withdraw(account: dict, amount: float) -> bool  # returns success
  - get_balance(account: dict) -> float
- Hints: account can be {"balance": 100.0}
- Tests:
  - acc = create_account(50); deposit(acc, 20); assert get_balance(acc) == 70

9) Number Guessing Game (CLI)
- Goal: Randomly choose a number; player has N attempts to guess.
- Functions:
  - choose_number(low: int, high: int) -> int
  - get_player_guess() -> int  # wrapper for input
  - play_guessing_game(low, high, attempts) -> str  # returns "win"|"lose"
- Hints: use random.randint, loop while attempts > 0
- Tests: Test logic functions separately: check compare_result(secret, guess)

10) Running Average (streaming)
- Goal: Maintain a running average for numbers given one-by-one.
- Functions:
  - RunningAverage class with add(number) and average() methods
- Hints: keep count and sum fields to avoid storing all numbers
- Tests:
  - r = RunningAverage(); r.add(2); r.add(4); assert r.average() == 3

Exercises 11–15: Combining functions, branching, loops, and validation (30–60 minutes each)

11) Simple Quiz Engine
- Goal: Run a multiple-choice quiz stored as list of dicts and score user.
- Functions:
  - run_quiz(questions: list[dict]) -> int
  - ask_question(q: dict) -> bool
- Hints: q = {"text": "...", "choices": ["a","b"], "answer": 1}
- Tests: Build a dummy quiz and assert run_quiz returns expected score for mocked answers (or separate out scoring logic)

12) Prime Sieve Slice
- Goal: Return primes up to n using Sieve of Eratosthenes.
- Functions:
  - primes_up_to(n: int) -> list[int]
- Hints: Good exercise with lists and loops
- Tests:
  - assert primes_up_to(10) == [2,3,5,7]

13) Simple File-based Contact Book (in-memory with save/load)
- Goal: Add/search contacts and save to a CSV.
- Functions:
  - add_contact(book: list[dict], name, phone) -> None
  - find_contact(book, name) -> list[dict]
  - save_book(book, filename) -> None
  - load_book(filename) -> list[dict]
- Hints: Use csv module for save/load; keep logic functions separate from CLI
- Tests:
  - book = []; add_contact(book, "Bob", "123"); assert find_contact(book, "Bob")

14) Rock-Paper-Scissors Best-of-N
- Goal: Play best-of-N rounds against computer.
- Functions:
  - rps_winner(a: str, b: str) -> "a"|"b"|"tie"
  - play_rps_best_of(n: int) -> dict  # returns summary
- Hints: Use straightforward conditionals for winner logic
- Tests:
  - assert rps_winner("rock", "scissors") == "a"

15) Text-based Menu Loop (small management CLI)
- Goal: Build a CLI menu that repeats until user quits.
- Functions:
  - display_menu(options: list[str]) -> None
  - get_choice(num_options: int) -> int
  - run_menu_loop(options, handlers)  # handlers is list of callables
- Hints: This teaches separation of IO and logic; handlers do the actual work
- Tests: Write handlers that set flags; call run_menu_loop in a test-friendly way by replacing get_choice

Exercises 16–20: Project-style, multiple functions & state (60–180 minutes)

16) Word Scramble Game
- Goal: Randomly scramble letters of a word; user guesses original.
- Functions:
  - scramble(word: str) -> str
  - pick_word(word_list: list[str]) -> str
  - play_scramble_game(word_list)
- Hints: Use random.sample to scramble; loop until correct or attempts exhausted
- Tests:
  - assert sorted(scramble("hello")) == sorted("hello")

17) Tic-Tac-Toe (console)
- Goal: Two-player CLI tic-tac-toe with win detection.
- Functions:
  - create_board() -> list[list[str]]
  - display_board(board) -> None
  - make_move(board, row, col, mark) -> bool
  - check_winner(board) -> "X"|"O"|None
  - play_ttt() -> str
- Hints: Represent board as 3x3 list; check rows/cols/diags
- Tests:
  - create a board state and assert check_winner returns expected result

18) Blackjack components (focus on functions & dealer logic)
- Goal: Implement several Blackjack functions and combine them into a round. (Not full betting yet.)
- Functions:
  - create_deck() -> list[str]
  - shuffle_deck(deck)
  - deal_card(deck) -> str
  - hand_value(hand: list[str]) -> int
  - player_hit_loop(deck, player_hand) -> list[str]
  - dealer_play(deck, dealer_hand) -> list[str]
  - decide_winner(player_hand, dealer_hand) -> "win"|"lose"|"push"
- Hints: Reuse hand_value logic from earlier worksheet; handle Aces carefully
- Tests:
  - assert hand_value(["A♠", "K♦"]) == 21
  - simulate deck and hands, assert decide_winner returns correct result

19) Guess-the-Word (Hangman precursor)
- Goal: Implement letter-guessing mechanics (reveal letters, track remaining attempts), without full UI niceties.
- Functions:
  - mask_word(word: str, guessed_letters: set[str]) -> str  # e.g. "_ e _ _ o"
  - guess_letter(word, guessed_letters, letter) -> tuple(new_guessed_set, hit:bool)
  - play_guess_loop(word, max_attempts) -> "win"|"lose"
- Hints: This is a stepping stone to Hangman: keep it pure and testable
- Tests:
  - assert mask_word("hello", {"e","o"}) == "_ e _ _ o"

20) Hangman (full CLI)
- Goal: Build a playable Hangman game: choose a word, show masked word, accept letter guesses, allow repeated plays, and track letters used and remaining attempts.
- Functions:
  - load_word_list(filename) -> list[str]
  - pick_word(words) -> str
  - mask_word(...) as in 19
  - play_hangman(words, max_attempts) -> dict  # stats of games
- Hints:
  - Separate core logic (masking, guess handling) from IO (input/print)
  - Validate input: single letter, not guessed before
  - Use sets for guessed letters and for unique letters in the word
- Tests:
  - Unit-test mask_word and guess_letter thoroughly; simulate a sequence of guesses and check end result

---

SECTION C — Hints & practice habits

- Start each exercise by writing the function signatures and docstrings first.
- Use assert statements at the bottom of your file to self-test small behaviors; they act as unit tests.
- Keep IO (input/print) in wrapper functions so you can test logic functions without user interaction.
- For games, store the sequence of events (a list of states) if you want to write tests that assert on states.
- Timeboxing: try an exercise for 30–60 minutes; if stuck, write pseudocode and post it here — I'll help refactor into functions.
- When implementing complex loops, log the loop invariants: what changes each iteration, what condition ends the loop.

---

SECTION D — Example small test snippet to include in your files

At the bottom of your Python file while developing, temporarily add:
```python
if __name__ == "__main__":
    # quick tests
    assert is_even(2) is True
    assert sum_digits(123) == 6
    print("Quick tests passed")
```
This helps you run the file and catch obvious errors before adding CLI interactions.

---

Good next step: pick one exercise from the list (or paste code you currently have), and I’ll:
- help you decompose it into functions,
- suggest a test plan,
- or review and refactor your implementation into clearer functions.

When you finish an exercise, paste your code and tell me where you struggled (naming, loops, conditionals, state). I’ll give targeted refactors and explanations.