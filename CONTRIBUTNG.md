# Contributors Guide

Welcome, and thank you for contributing to our project! To ensure smooth collaboration and maintain code quality, please adhere to the following guidelines:

---

## Tools to Use
- Use **PyCharm Community Edition** (PyCharm for Professional is also alright) or **JetBrains Fleet**, or Visual Studio Code (VSCode) as your Integrated Development Environment (IDE) for consistency across contributions.
---

## Coding Standards
1. **Testing**
   - Always test your changes locally before submitting a Pull Request (PR). This helps ensure functionality and avoids introducing bugs to the bot.

2. **Prior Discussions**
   - For large or significant changes, please discuss your plans with the developers before starting. DM, or email the developers.

3. **Command Structure**
   - Use the `@bot.tree.command` structure to implement Discord bot commands.
   - You also MUST use

4. **Python Version**
   - Use **Python 3.12** (3.12.3) exclusively. Do not use a lower or higher version to maintain compatibility.

5. **Comments**
   - Add **#COMMENTs** to your code to make it easy for all contributors to understand. Clear and concise comments are essential for collaboration, so we don't have to ask you every single time. Please use ALL CAPITALS in all comments.

6. **Variables**
   - Please do not change any of the existing variables. It's alright to create new ones, with new commands, but it's not okay to change the already existing variables, and renaming them, etc.
   - If you did create a new variable, please comment before submitting a PR.
   - If you've added a lot of new variables, please DM wndx2 on Discord, to make the developers aware of the newly added variables.

7. **Pycord**
   - Please **do not** use Pycord, as it will make the code unable to execute due to it's incompatibility with discord.py. I'm not explaining more about this, so if you would like to learn more about this, don't ask me please.
   - If your code does not run at all, please check if you have Pycord installed. If you do have it downloaded on your device, please delete the Pycord library, and use discord.py's latest version.
---

## Art Guidelines
1. **Sizing**
   - If you are submitting any art, please only submit 16x16 pixel arts; resolution must be over 400x400, and below 700x700.

2. **Tools**
   - There are many options out there, but I tend to use Piskel a lot.

3. **Glows**
   - If you are ever wanting to add glowing effects, use Lunacy by Icons8.
   - Here are the settings below:\
     X: 0\
     Y: 0\
     Blur: 50\
     Spread: 0\
     Color: *Depends*\
     Opacity: 100%

---
  
## Pull Request Guidelines
- Submit meaningful PRs only. Do not just remove a single space, and think that you've made a change.
- Avoid creating PRs for trivial or unnecessary changes.
- Ensure your PR includes a clear description of what changes were made and why.
- Follow the **coding standards** listed above.

---

We appreciate your contributions! If you have questions, feel free to reach out to wndx2 on Discord.
