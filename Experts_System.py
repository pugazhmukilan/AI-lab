def ask_symptoms():
    symptoms = {
        "high_temperature": False,
        "chills": False,
        "body_aches": False,
        "headache": False,
        "fatigue": False,
        "sweating": False
    }
    print("Please answer the following questions with 'yes' or 'no':")
    for symptom in symptoms:
        answer = input(f"Do you have {symptom.replace('_', ' ')}? ").lower()
        if answer == 'yes':
            symptoms[symptom] = True
    return symptoms

def check_fever(symptoms):
    if symptoms["high_temperature"]:
        print("You might have a fever.")
    elif (symptoms["chills"] and symptoms["body_aches"]) or \
         (symptoms["headache"] and symptoms["fatigue"]) or \
         (symptoms["sweating"] and symptoms["body_aches"]):
        print("You might have a mild fever.")
    else:
        print("You don't seem to have a fever.")

if __name__ == "__main__":
    symptoms = ask_symptoms()
    check_fever(symptoms)
