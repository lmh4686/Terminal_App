from module import ascii_magic, landing, joint_prompt, farm_choice, b, c, s, r

ascii_magic.to_terminal(landing)
print(f"{b.LIGHTYELLOW_EX}{c.BLACK}{s.DIM}Welcome to farming game!{r}\n"
      f"{c.GREEN}Harvest ingredients from 2 different farms and cook them at home!{r}")
joint_prompt()
farm_choice()
