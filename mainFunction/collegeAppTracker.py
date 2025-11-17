def display_welcome():
    """Display program header"""
    print("Welcome to the College Application Tracker!")

def get_college_count():
    """
    Get number of colleges user is applying to
    Return
        count (int)
    """
    count = input("How many colleges have you applied to? ")
    return int(count)

def get_application_costs(num_colleges):
    """
    Calculate total application costs

    Return
        total_cost (float)
    """
    total_cost = 50 * num_colleges
    return float(total_cost)

def get_sat_score():
    """
    Get user's SAT score

    Return
        score (int)
    """
    score = input("What was your SAT score? ")
    return int(score)

def analyze_sat(score):
    """
    Provide feedback on SAT score
    >= 1400 - Excellent
    >= 1200 - Good score
    >= 1000 - Solid foundation
    else - Consider retaking to improve college options.
    """
    if score >= 1400:
        print("Excellent!")
    elif score >= 1200:
        print("Good score!")
    elif score >= 1000:
        print("Solid foundation.")
    else:
        print("Consider retaking to improve college options.")

def display_summary(colleges, cost, sat_score, sat_feedback):
    """
    Display complete application summary with header
    """

def main():
    """Main function - orchestrates the entire program"""
    # Welcome the user
    display_welcome()

    # collect information
    num_colleges = get_college_count
    total_cost = get_application_costs(num_colleges)
    sat = get_sat_score()

    # Analyze data
    feedback = analyze_sat(sat)

    # Display results
    display_summary(num_colleges, total_cost, sat, feedback)

    print("\nGood luck with your applications!")

# entry point
if __name__ == __main__:
    main()