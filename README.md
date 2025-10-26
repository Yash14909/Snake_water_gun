
## 🐍 Snake, Water, Gun — Python Game

### 🎮 Overview

This is a simple **Python console game** based on the popular childhood game **Snake, Water, Gun**, similar to *Rock, Paper, Scissors*.
You play against the computer, which randomly selects one of the three options.

---

### ⚙️ How It Works

#### Game Rules

| Your Choice | Computer Choice | Result     |
| ----------- | --------------- | ---------- |
| Snake 🐍    | Water 💧        | You Win ✅  |
| Snake 🐍    | Gun 🔫          | You Lose ❌ |
| Water 💧    | Snake 🐍        | You Lose ❌ |
| Water 💧    | Gun 🔫          | You Win ✅  |
| Gun 🔫      | Snake 🐍        | You Win ✅  |
| Gun 🔫      | Water 💧        | You Lose ❌ |

If both make the same choice → it's a **Draw** 🤝

---

### 💻 Code Explanation

```python
import random

'''
1 = Snake
-1 = Water
0 = Gun
'''

computer = random.choice([-1, 0, 1])
youStr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")

yrDict = {"s": 1, "w": -1, "g": 0}
you = yrDict[youStr]

reverseDict = {1: "s", -1: "w", 0: "g"}

print(f"Your choice is {reverseDict[you]} and computer choice is {reverseDict[computer]}")

if computer == you:
    print("It's a draw!")
else:
    if (computer == -1 and you == 1):
        print("You won!")
    elif (computer == -1 and you == 0):
        print("You lose!")
    elif (computer == 1 and you == -1):
        print("You lose!")
    elif (computer == 1 and you == 0):
        print("You won!")
    elif (computer == 0 and you == 1):
        print("You lose!")
    elif (computer == 0 and you == -1):
        print("You won!")
    else:
        print("Something went wrong!")
```

---

### ▶️ How to Run

1. **Save** the code as `snake_water_gun.py`
2. **Open Terminal / Command Prompt**
3. Navigate to the folder containing the file:

   ```bash
   cd path/to/your/folder
   ```
4. Run the game:

   ```bash
   python snake_water_gun.py
   ```
5. Enter your choice:

   ```
   s for Snake
   w for Water
   g for Gun
   ```

---

### 🧠 Example Output

```
Enter your choice: s
Your choice is s and computer choice is w
You won!
```

---

### 📁 File Info

* File name: `snake_water_gun.py`
* Language: Python
* Author: YR
* Version: 1.0

---
