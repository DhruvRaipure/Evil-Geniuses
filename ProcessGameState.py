import pickle
import pandas as pd
file = open('./data/game_state_frame_data.pickle', 'rb')

# dump information to that file
data = pd.read_pickle(file)
file.close()
roundStats = {}
columnNames = data.columns.tolist()
# for item in data:
#     print('The data is', item)
# for index, row in data.iterrows():
#     # print(type(row))
#     # break
#     print(index)
#     if row['round_num'] in roundStats:
#         roundStats[row['round_num']] = roundStats[row['round_num']]._append(row)
#     else:
#         # df = pd.DataFrame(row, columns=columnNames)
#         df = pd.DataFrame([row])
#         roundStats[row['round_num']] = df
grouped = data.groupby('round_num')
# Create separate dataframes for unique values of 'round_num'
unique_dataframes = [group for _, group in grouped]

for data in unique_dataframes:
    data.set_index(['Round', 'Player'], inplace=True)

# df.set_index(['Round', 'Player'], inplace=True)