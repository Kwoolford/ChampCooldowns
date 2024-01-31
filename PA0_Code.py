import pandas as pd

df = pd.read_excel("Champ_Cooldowns_Fixed.xlsx")
allChamps = df["Champion"]
# Printing the dataframe to help users know what champions they can input
print(df)

def userInput(allChamps):
    user_ability = ""
    user_cdr = 5
    while True:
        print("Input X for champion to exit")
        user_champ = input("What champion would you like to calculate ability casts for? : ").title()
        if user_champ in allChamps.values or user_champ == "X":
            break
        else:
            print("Invalid input, try again")
    while True:
        if user_champ == "X":
            break
        user_ability = input("Will you max Q, W, or E first? : ").upper()
        if user_ability in ["Q", "W", "E"] or user_champ == "X":
            break
        else:
            print("Invalid Input")
    while True:
        if user_champ == "X":
            break
        user_cdr = input("What percent cooldown do you expect to have? Ex. 0, .1, or .2 (IN DECIMAL FORMAT)? : ")
        try:
            float(user_cdr)
        except ValueError:
            print("Could not convert into a float, try again")
        else:
            if 0 <= float(user_cdr) < 1:
                break

    return user_champ, user_ability, float(user_cdr)

# Retrieves the row from the dataframe of the champion that the user specifies
def champSearch(df, user_data):
    champ_data = df.loc[df["Champion"] == user_data[0]]
    return champ_data

# Gets the 5 values of cooldowns for the user specified ability
def abilityCooldowns(champ_frame, user_data, cooldowndata):

    cooldowndata.append(int(champ_frame[user_data[1] + "1"].iloc[0]))
    cooldowndata.append(int(champ_frame[user_data[1] + "2"].iloc[0]))
    cooldowndata.append(int(champ_frame[user_data[1] + "3"].iloc[0]))
    cooldowndata.append(int(champ_frame[user_data[1] + "4"].iloc[0]))
    cooldowndata.append(int(champ_frame[user_data[1] + "5"].iloc[0]))

# Gets the base numerical, and string values of the abilities not being upgraded.
    if user_data[1] == "Q":
        spare1 = "W"
        spare2 = "E"
        cooldowndata.append(int(champ_frame["W1"].iloc[0]))
        cooldowndata.append(int(champ_frame["E1"].iloc[0]))

    elif user_data[1] == "W":
        spare1 = "Q"
        spare2 = "E"
        cooldowndata.append(int(champ_frame["Q1"].iloc[0]))
        cooldowndata.append(int(champ_frame["E1"].iloc[0]))
    elif user_data[1] == "E":
        spare1 = "Q"
        spare2 = "W"
        cooldowndata.append(int(champ_frame["Q1"].iloc[0]))
        cooldowndata.append(int(champ_frame["W1"].iloc[0]))
    cooldowndata.append(int(champ_frame["R1"].iloc[0]))

    return cooldowndata, spare1, spare2 

def cooldownCalculation(cooldowndata, user_data):
    iterator = 0
    totalMainCast = 0
    spareCast1 = 0
    spareCast2 = 0
    cooldownlist = cooldowndata[0]

    ultimateCast = 390//(cooldownlist[7]-(cooldownlist[7]*user_data[2]))
    # This statement calculates the total cast time with the introduction of the cooldown bias specified by the user after 312 seconds
    while iterator != 5:
        if iterator < 3:
            totalMainCast += 156//cooldownlist[iterator]
            spareCast1 += 156//cooldownlist[5]
            spareCast2 += 156//cooldownlist[6]
        else:
            totalMainCast += 156//(cooldownlist[iterator]-(cooldownlist[iterator]*user_data[2]))
            spareCast1 += 156//(cooldownlist[5]-(cooldownlist[5]*user_data[2]))
            spareCast2 += 156//(cooldownlist[6]-(cooldownlist[6]*user_data[2]))
        iterator += 1


    return totalMainCast, spareCast1, spareCast2, ultimateCast


while True:
    cooldownlist = []
    cooldowndata = []
    print("This program will calculate the total amount of ability casts for a champion")
    user_data = userInput(allChamps)
    if user_data[0] == "X":
        break
    champ_frame = champSearch(df, user_data)
    # print(champ_frame)

    cooldowndata = abilityCooldowns(champ_frame, user_data, cooldowndata)
    # print(cooldowndata)

    cooldownCalc = cooldownCalculation(cooldowndata, user_data)
    # print(cooldownCalc)

    print(f"\nBased on your input, you would be able to cast,\n{user_data[1]}: {cooldownCalc[0]}\n{cooldowndata[1]}: {cooldownCalc[1]}\n{cooldowndata[2]}: {cooldownCalc[2]}\nUltimate Ability: {cooldownCalc[3]} ")


    print(f"With a cooldown reduction of {user_data[2] * 100}%\n\n")
print("\nThank you for choosing Woolford Calculations!")