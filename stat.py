import pandas as pd
import matplotlib.pyplot as plt

# import dataset
df = pd.read_csv('train.csv')

# clean dataset

# name is not needed, drop it
# ticket is not needed, drop it
# cabin irregular, drop it
df = df.drop(columns=['Name', 'Ticket', 'Cabin'])

# convert male and female to numerical values
sex_df = df['Sex']
sex_list_num = []
for i in sex_df:
    if i == 'male':
        sex_list_num.append(0)
    elif i == 'female':
        sex_list_num.append(1)
print(len(sex_list_num))

# convert embarked port to numerical values
embarked_df = df['Embarked']
embarked_list_num = []
for i in embarked_df:
    if i == 'C':
        embarked_list_num.append(0)
    elif i == 'Q':
        embarked_list_num.append(1)
    else:
        embarked_list_num.append(2)

# update df
new_df = pd.DataFrame({'Sex':sex_list_num, 'Embarked':embarked_list_num})
df.update(new_df)

print(df.describe)
