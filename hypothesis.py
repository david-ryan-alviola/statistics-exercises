# Helper function to evaluate hypothesis
def evaluate_hypothesis(null_hypothesis, alternative_hypothesis, alpha, p_value, t_value, tails = "two"):
    print(f"t:  {t_value}, p:  {p_value}, a:  {alpha}")
    print()

    def print_null_hypothesis():
        print(f"We fail to reject the null hypothesis:  {null_hypothesis}")

    def print_alt_hypothesis():
        print("We reject the null hypothesis.")
        print(f"We move forward with the alternative hypothesis:  {alternative_hypothesis}")

    if tails == "two":

        if p_value < alpha:
            print_alt_hypothesis()
        else:
            print_null_hypothesis()
    else:

        if (p_value / 2) < alpha:

            if (tails == "greater"):
                if (t_value > 0):
                    print_alt_hypothesis()
            else:
                if (t_value < 0):
                    print_alt_hypothesis()
        else:
            print_null_hypothesis()