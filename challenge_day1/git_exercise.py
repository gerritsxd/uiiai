from challenge_day1 import leopoldo_gerrit, Mies_Haenen, nadz, Keitaro_Indradjit

def print_team_members():
    team_name = "uiiai"  # You can change this to your actual team name
    print(f"This is Team {team_name}. We are:")
    print(f"- {leopoldo_gerrit.get_name()}")
    print(f"- {Mies_Haenen.get_name()}")
    print(f"- {nadz.get_name()}\n")
    print(f"- {Keitaro_Indradjit.get_name()}\n")

def print_story():
    print("--- The Story of UIIAI ---\n")
    team_modules = [leopoldo_gerrit, Mies_Haenen, nadz, Keitaro_Indradjit]

    # Print Act 1 from all contributors
    print("--- Act 1 ---")
    for module in team_modules:
        if hasattr(module, 'get_paragraph_act1'):
            print(module.get_paragraph_act1() + "\n")

    # Print Act 2 from all contributors
    print("--- Act 2 ---")
    for module in team_modules:
        if hasattr(module, 'get_paragraph_act2'):
            print(module.get_paragraph_act2() + "\n")

    # Print Act 3 from all contributors
    print("--- Act 3 ---")
    for module in team_modules:
        if hasattr(module, 'get_paragraph_act3'):
            print(module.get_paragraph_act3() + "\n")

if __name__ == "__main__":
    print_team_members()
    print_story()
