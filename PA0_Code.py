import pandas as pd

df = pd.read_excel("Champ_Cooldowns_Fixed.xlsx")
print(df)

def userInput():
    user_champ = input("What is the name of the Champion? : ").title()
    user_ability = input("Will you max Q, W, or E first? : ")
    user_cdr = input("How much ability haste do you anticipate to have? : ")
    return user_champ, user_ability, user_cdr

def champSearch(df, user_champ):
    champ_data = df.query(df[user_champ])
    return champ_data

user_data = userInput()
print(user_data[0])

print(df.loc[df["Champion"] == user_data[0]])
# champ_data = champSearch(df, user_data[0])
# print(champ_data)