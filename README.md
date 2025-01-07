# Star War Name 🚀

## Description
Embark on an intergalactic adventure with this Star Wars-inspired game! This project generates a unique Star Wars name based on your personal inputs.

## Features
- 🌟 Generates a Star Wars-style name using fun combinations.
- 🛡️ Simple and user-friendly interface.
- 🎮 Quick and engaging process for fans and creators alike.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Game Code](#game-code)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/Zainab-Mehmood/python-game.git
   ```
2. Navigate to the project directory:
   ```
   cd python-game
   ```
3. Install the required dependencies (if any):
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the game:
   ```
   python game.py
   ```
2. Follow the prompts to enter your details and generate your Star Wars name!

### Example Screenshot:
![Game Screenshot](screenshot.png)

## Game Code
```python
import time, os

def STAR_WAR_NAME(first_name, last_name, mum_maiden, city):
  first_slice = first_name[:3]
  second_slice = last_name[:3]
  third_slice = mum_maiden[:2]
  forth_slice = city[-3:][::-1]
  print()
  print("Generating your Star War name...")
  full_name = f"{first_slice}{second_slice} {third_slice}{forth_slice}"
  print(f"> Your Star Wars✨ name is {full_name}.")


def main():
  print("STAR WARS NAME GENERATOR⭐")
  print()
  first_name = input("Enter your first name: ").capitalize().strip()
  last_name = input("Enter your last name: ").lower().strip()
  mum_maiden = input("Enter your Mum's maiden name: ").capitalize().strip()
  city = input("Enter the city where you were born: ").capitalize().strip()

  STAR_WAR_NAME(first_name, last_name, mum_maiden, city)

main()
```

## Contributing
Contributions are welcome! Here's how you can help:
- Report bugs by opening an issue.
- Suggest new features or improvements.
- Submit a pull request with your changes.

Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Author
**Zainab**
- GitHub: [@Zainab-Mehmood](https://github.com/Zainab-Mehmood)
- Twitter: [@ZainabGames](https://twitter.com/username)
