import pandas as pd
from csv import reader
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.neighbors import KNeighborsRegressor

with open('data.log', 'r') as training_data:

    csv_reader = reader(training_data)

    for df in csv_reader:
        print(df[3], "--------")
        dfHand = pd.DataFrame()
        dfHand['thumb-proximal'] = df[2]
        dfHand['thumb-intermediate'] = df[3]
        dfHand['thumb-distal'] = df[4]
        dfHand['fthumb'] = float(df[3]) / 90

        dfHand['index-proximal'] = df[6]
        dfHand['index-intermediate'] = df[7]
        dfHand['index-distal'] = df[8]
        dfHand['findex'] = df[7].values / 90

        dfHand['middle-proximal'] = df[10]
        dfHand['middle-intermediate'] = df[11]
        dfHand['middle-distal'] = df[12]
        dfHand['fmiddle'] = df[11].values / 90


        dfHand['ring-proximal'] = df[14]
        dfHand['ring-intermediate'] = df[15]
        dfHand['ring-distal'] = df[16]
        dfHand['fring'] = df[15].values / 90

        dfHand['pinky-proximal'] = df[18]
        dfHand['pinky-intermediate'] = df[19]
        dfHand['pinky-distal'] = df[20]
        dfHand['fpinky'] = df[19].values / 90

        dfHand['fall'] = dfHand.findex + dfHand.fmiddle + dfHand.fring + dfHand.fpinky


        dfHand.index = df[0]

# dfHand['fist'] = 0
# dfHand.loc[(dfHand.index = 1621202301496) & (dfHand.index <= 1621202304737) , "fist" ] = 1
# dfHand.loc[(dfHand.index = 1621202311402) & (dfHand.index <= 1621202312323) , "fist" ] = 1
# dfHand.loc[(dfHand.index = 1621202313577) & (dfHand.index <= 1621202314631) , "fist" ] = 1
# dfHand.loc[(dfHand.index = 1621202317046) & (dfHand.index <= 1621202317835) , "fist" ] = 1