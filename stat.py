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


# convert embarked port to numerical values
embarked_df = df['Embarked']
embarked_list_num = []
for i in embarked_df:
    if i == 'C':
        embarked_list_num.append(0)
    elif i == 'Q':
        embarked_list_num.append(1)
    elif i == 'S':
        embarked_list_num.append(2)
    else:
        embarked_list_num.append(sum(embarked_list_num)//len(embarked_list_num))

# fill in gaps in age by replacing them with mean age
age_df = df['Age']
age_list_temp = []
for i in age_df:
    if i > 0:
        age_list_temp.append(i)
age_avg = sum(age_list_temp)/len(age_list_temp)
age_list = []
for i in age_df:
    if i > 0:
        age_list.append(i)
    else:
        age_list.append(age_avg)

# update df
new_df = pd.DataFrame({'Sex':sex_list_num, 'Embarked':embarked_list_num, 'Age': age_list})
df.update(new_df)

print(age_df)
