#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import stuff

import csv
import pandas as pd
import numpy as np
import random
from collections import Counter
import sys


# In[404]:
races = ['Total!!Population of one race!!White alone',
       'Total!!Population of one race!!Black or African American alone',
       'Total!!Population of one race!!American Indian and Alaska Native alone',
       'Total!!Population of one race!!Asian alone',
       'Total!!Population of one race!!Native Hawaiian and Other Pacific Islander alone',
       'Total!!Population of one race!!Some Other Race alone',
       'Total!!Two or More Races!!Population of two races!!White; Black or African American',
       'Total!!Two or More Races!!Population of two races!!White; American Indian and Alaska Native',
       'Total!!Two or More Races!!Population of two races!!White; Asian',
       'Total!!Two or More Races!!Population of two races!!White; Native Hawaiian and Other Pacific Islander',
       'Total!!Two or More Races!!Population of two races!!White; Some Other Race',
       'Total!!Two or More Races!!Population of two races!!Black or African American; American Indian and Alaska Native',
       'Total!!Two or More Races!!Population of two races!!Black or African American; Asian',
       'Total!!Two or More Races!!Population of two races!!Black or African American; Native Hawaiian and Other Pacific Islander',
       'Total!!Two or More Races!!Population of two races!!Black or African American; Some Other Race',
       'Total!!Two or More Races!!Population of two races!!American Indian and Alaska Native; Asian',
       'Total!!Two or More Races!!Population of two races!!American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander',
       'Total!!Two or More Races!!Population of two races!!American Indian and Alaska Native; Some Other Race',
       'Total!!Two or More Races!!Population of two races!!Asian; Native Hawaiian and Other Pacific Islander',
       'Total!!Two or More Races!!Population of two races!!Asian; Some Other Race',
       'Total!!Two or More Races!!Population of two races!!Native Hawaiian and Other Pacific Islander; Some Other Race',
       'Total!!Two or More Races!!Population of three races!!White; Black or African American; American Indian and Alaska Native',
       'Total!!Two or More Races!!Population of three races!!White; Black or African American; Asian',
       'Total!!Two or More Races!!Population of three races!!White; Black or African American; Native Hawaiian and Other Pacific Islander',
       'Total!!Two or More Races!!Population of three races!!White; Black or African American; Some Other Race',
       'Total!!Two or More Races!!Population of three races!!White; American Indian and Alaska Native; Asian',
       'Total!!Two or More Races!!Population of three races!!White; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander',
       'Total!!Two or More Races!!Population of three races!!White; American Indian and Alaska Native; Some Other Race',
       'Total!!Two or More Races!!Population of three races!!White; Asian; Native Hawaiian and Other Pacific Islander',
       'Total!!Two or More Races!!Population of three races!!White; Asian; Some Other Race',
       'Total!!Two or More Races!!Population of three races!!White; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'Total!!Two or More Races!!Population of three races!!Black or African American; American Indian and Alaska Native; Asian',
       'Total!!Two or More Races!!Population of three races!!Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander',
       'Total!!Two or More Races!!Population of three races!!Black or African American; American Indian and Alaska Native; Some Other Race',
       'Total!!Two or More Races!!Population of three races!!Black or African American; Asian; Native Hawaiian and Other Pacific Islander',
       'Total!!Two or More Races!!Population of three races!!Black or African American; Asian; Some Other Race',
       'Total!!Two or More Races!!Population of three races!!Black or African American; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'Total!!Two or More Races!!Population of three races!!American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander',
       'Total!!Two or More Races!!Population of three races!!American Indian and Alaska Native; Asian; Some Other Race',
       'Total!!Two or More Races!!Population of three races!!American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'Total!!Two or More Races!!Population of three races!!Asian; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'Total!!Two or More Races!!Population of four races!!White; Black or African American; American Indian and Alaska Native; Asian',
       'Total!!Two or More Races!!Population of four races!!White; Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander',
       'Total!!Two or More Races!!Population of four races!!White; Black or African American; American Indian and Alaska Native; Some Other Race',
       'Total!!Two or More Races!!Population of four races!!White; Black or African American; Asian; Native Hawaiian and Other Pacific Islander',
       'Total!!Two or More Races!!Population of four races!!White; Black or African American; Asian; Some Other Race',
       'Total!!Two or More Races!!Population of four races!!White; Black or African American; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'Total!!Two or More Races!!Population of four races!!White; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander',
       'Total!!Two or More Races!!Population of four races!!White; American Indian and Alaska Native; Asian; Some Other Race',
       'Total!!Two or More Races!!Population of four races!!White; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'Total!!Two or More Races!!Population of four races!!White; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'Total!!Two or More Races!!Population of four races!!Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander',
       'Total!!Two or More Races!!Population of four races!!Black or African American; American Indian and Alaska Native; Asian; Some Other Race',
       'Total!!Two or More Races!!Population of four races!!Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'Total!!Two or More Races!!Population of four races!!Black or African American; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'Total!!Two or More Races!!Population of four races!!American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'Total!!Two or More Races!!Population of five races!!White; Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander',
       'Total!!Two or More Races!!Population of five races!!White; Black or African American; American Indian and Alaska Native; Asian; Some Other Race',
       'Total!!Two or More Races!!Population of five races!!White; Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'Total!!Two or More Races!!Population of five races!!White; Black or African American; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'Total!!Two or More Races!!Population of five races!!White; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'Total!!Two or More Races!!Population of five races!!Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'Total!!Two or More Races!!Population of six races!!White; Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race']

races2 = ['White alone',
       'Black or African American alone',
       'American Indian and Alaska Native alone',
       'Asian alone',
       'Native Hawaiian and Other Pacific Islander alone',
       'Some Other Race alone',
       'White; Black or African American',
       'White; American Indian and Alaska Native',
       'White; Asian',
       'White; Native Hawaiian and Other Pacific Islander',
       'White; Some Other Race',
       'Black or African American; American Indian and Alaska Native',
       'Black or African American; Asian',
       'Black or African American; Native Hawaiian and Other Pacific Islander',
       'Black or African American; Some Other Race',
       'American Indian and Alaska Native; Asian',
       'American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander',
       'American Indian and Alaska Native; Some Other Race',
       'Asian; Native Hawaiian and Other Pacific Islander',
       'Asian; Some Other Race',
       'Native Hawaiian and Other Pacific Islander; Some Other Race',
       'White; Black or African American; American Indian and Alaska Native',
       'White; Black or African American; Asian',
       'White; Black or African American; Native Hawaiian and Other Pacific Islander',
       'White; Black or African American; Some Other Race',
       'White; American Indian and Alaska Native; Asian',
       'White; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander',
       'White; American Indian and Alaska Native; Some Other Race',
       'White; Asian; Native Hawaiian and Other Pacific Islander',
       'White; Asian; Some Other Race',
       'White; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'Black or African American; American Indian and Alaska Native; Asian',
       'Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander',
       'Black or African American; American Indian and Alaska Native; Some Other Race',
       'Black or African American; Asian; Native Hawaiian and Other Pacific Islander',
       'Black or African American; Asian; Some Other Race',
       'Black or African American; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander',
       'American Indian and Alaska Native; Asian; Some Other Race',
       'American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'Asian; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'White; Black or African American; American Indian and Alaska Native; Asian',
       'White; Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander',
       'White; Black or African American; American Indian and Alaska Native; Some Other Race',
       'White; Black or African American; Asian; Native Hawaiian and Other Pacific Islander',
       'White; Black or African American; Asian; Some Other Race',
       'White; Black or African American; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'White; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander',
       'White; American Indian and Alaska Native; Asian; Some Other Race',
       'White; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'White; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander',
       'Black or African American; American Indian and Alaska Native; Asian; Some Other Race',
       'Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'Black or African American; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'White; Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander',
       'White; Black or African American; American Indian and Alaska Native; Asian; Some Other Race',
       'White; Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'White; Black or African American; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'White; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race',
       'White; Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race']


#ordered race & nonhispanic/hispanic data based on frequency in general US population -
# generated from ../dp/create_all_usdistribution.csv
real_order = [124, 116, 118, 123, 115, 117, 125, 51, 59, 111, 32, 102, 
              108, 42, 62, 37, 99, 44, 103, 48, 26, 96, 31, 106, 95, 
              45, 105, 38, 41, 107, 119, 97, 33, 43, 30, 94, 13, 79, 
              15, 83, 80, 27, 29, 12, 88, 76, 11, 78, 4, 17, 81, 75, 
              19, 74, 14, 6, 67, 68, 1, 10, 65, 5, 64, 63, 0, 66, 69, 
              71, 70, 2, 73, 8, 7, 84, 3, 72, 91, 77, 85, 20, 82, 21,
              24, 9, 18, 28, 104, 22, 110, 87, 25, 86, 89, 92, 35, 90,
              40, 36, 100, 50, 47, 16, 93, 39, 23, 98, 34, 56, 114, 57, 
              101, 113, 54, 46, 52, 49, 60, 55, 120, 53, 58, 109, 112, 61, 122, 121]
#print(real_order.index(48+63))


# In[405]:


############################################################################################################################
#This method imports county data from csv file to pandas df and reformats race data numerically
############################################################################################################################
def import_countydata(county):
    #import csv file as dataframe
    df = pd.read_csv (r'../homemade_data/'+county+'.csv')
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    #transfer race representation to include hispanic data:
    #if not hispanic: index is 0-62
    #if hispanic: index is 63-126
        #so, if hispanic, add 63 to the existing race value
    for index, row in df.iterrows():
        d = row['race']
        h = row['hispanic']
        if d in races and h==0:
            df.at[index, 'race'] = real_order.index(races.index(d))
        elif d in races and h==1:
            df.at[index, 'race'] = real_order.index((races.index(d))+63)

    return df


# In[406]:


############################################################################################################################
#This method imports state data from csv file to pandas df and reformats race data numerically
#------------------------------
#INPUT:
    #state: state to import and organize data for
#------------------------------
#OUTPUT:
#final_dfs: list containing occurences of each real_order race index
    #ex. final_dfs[race]= rows in state dataset that have the same real order value 
############################################################################################################################
def import_statedata(state):
    #import csv file as dataframe
    df = pd.read_csv (r'state_data/'+state+'.csv')
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
   
    for index, row in df.iterrows():        
    #transfer race representation to include hispanic data:
        #if not hispanic: index is 0-62
        #if hispanic: index is 63-126
            #so, if hispanic, add 63 to the existing race value    
        d = row['race']
        h = row['hispanic']
        if d in races2 and h==0:
            df.at[index, 'race'] = real_order.index(races2.index(d))
        elif d in races2 and h==1:
            df.at[index, 'race'] = real_order.index(races2.index(d)+63)

    final_dfs = {}

    #create list of occurence count in df for each real_order race value, sort values inside each by age
    for race_realorder in range(0,126):
        final_dfs[race_realorder] = (df[df['race'] == race_realorder]).sort_values(by='age')

    #returns list of real_orders with corresponding values in dataset  
    return final_dfs


# In[408]:


############################################################################################################################
#GET ROWS PRIORITIZED FOR SWAPPING
#Get variables prioritized to be swapped 
#This method returns rows based upon whether they are unique in the dataset
############################################################################################################################

def pick_swapvars(df):
    #all v is collection of all row values
    all_v = []

    #add all rows to list all_v
    for i, row in df.iterrows():
        all_v.append([[row['age'], row['sex'], row['race']], row['id']])
        
    #drop duplicates based upon age, sex, and race from df
    df_drop = df.drop_duplicates(subset = ['age', 'sex', 'race'])
        
    #the list of ids of all rows that contain unique entries
    swap = []
    
    #for each item in uniques, check how many times it occurs in original data
    for i, row in df_drop.iterrows():
        #list containing age, sex, race
        check = [row['age'], row['sex'], row['race']]
        dcount = 0 
        #for all rows in the dataframe
        for a in all_v:
            #check if the age, sex, and races match the row
            if a[0]==check:
                #if they do match, incremement by 1
                dcount +=1
        #if only present once, add to swaps
        if dcount == 1:
            swap.append(row['id']-1)
            
               
    return swap


# In[409]:


############################################################################################################################
#GET ALL ROWS TO SWAP
#----------------------------------------------------
#INPUT
    #dframe: full pandas dataset
    #swaprate: % to swap at
    #swap: the list of ids of all rows that contain unique entries
#----------------------------------------------------
#OUTPUT
    #returns list of rows to swap, list of rows to not swap, & # of rows to b swapped
############################################################################################################################

def get_rows_to_swap(dframe, swaprate, swap):
    
    #number of rows we need to swap in the dataset, based upon the given swap rate 
    rows_to_swap = swaprate*dframe.shape[0]
    rows_to_swap = round(rows_to_swap)
    
    #rows to be swapped and not swapped
    swaps = []
    not_swaps = []
    
    #if more rows need to be swapped than there are unique rows present in swap
    if rows_to_swap > len(swap):
        #add all unique rows to swaps
        swaps = swap
        #all rows in dataset to choose from to supplementally swap
        rows = np.arange(0,dframe.shape[0], 1)        
        #find one not already in swaps and add it to swaps
        while len(swaps) < rows_to_swap:
            random_s = random.choice(rows)
            if random_s not in swaps:
                swaps.append(random_s)

    # else if number of rows needed to be swapped is less than or equal to unique rows present in swap
    else:
        #all unique rows in dataset to choose from to swap
        rows2 = np.arange(0,len(swap), 1)
        #find one not already in swaps and add it to swaps 
        while len(swaps) < rows_to_swap:
            random_s = swap[random.choice(rows2)]
            if random_s not in swaps:
                swaps.append(random_s)

    #if not present in swaps, add to not_swaps 
    for i in range(0,dframe.shape[0]):
        if i not in swaps:
            not_swaps.append(i)

    #returns list of rows to swap, list of rows to not swap, & # of rows to b swapped
    return swaps, not_swaps, rows_to_swap


# In[410]:


############################################################################################################################
#FIND THE SWAP
#INPUT 
#dframe = dataset containing r 
#r = row to swap
#thresholds for each variable type
#------------------
#OUTPUT
#return row to be swapped, and the thresholds at which this match was made
############################################################################################################################

def find_swap(dframe, r, threshold_age, threshold_sex, threshold_race):
    
    #find similar row in state dataframe
        
    #get data from normal dataframe for r
    age = dframe.at[r, 'age']
    sex = dframe.at[r, 'sex']
    race = dframe.at[r, 'race']
    

    complete = False
    
    #find someone similar in state
    while complete == False:
            
        #filter for race
        new_data = df_state[race]
        i=1            
        while i <=threshold_race:
            if(race-i >= 0):
                new_data = new_data.append(df_state[race-i], ignore_index=True)
            if(race+i < len(real_order)):
                new_data = new_data.append(df_state[race+i], ignore_index=True)
                i+=1
                
        #filter for age
        new_data = new_data[new_data['age']>= int(age-threshold_age)]       
        new_data = new_data[new_data['age']<=int(age+threshold_age)]     

        #filter for sex
        if threshold_sex == 0:
            new_data = new_data[new_data['sex']==sex]

        #check if done (if there are any matches)
        if new_data.shape[0] > 0:
            final = new_data.sample()
            complete = True
            break
                
        #else increment thresholds and try again
        else: 
            threshold_race = threshold_race + 2
            threshold_age = threshold_age + 2

    #return row to be swapped, and the thresholds at which this match was made
    return final, threshold_race, threshold_age


# In[411]:


############################################################################################################################
#DO THE SWAP
#INPUT 
#final = row in state dataset to swap
#r = row in block dataset to swap
#df_county = county dataset
#------------------
#OUTPUT
#dframe: new county dataset
############################################################################################################################

def do_swap(dframe, r, final):

    #set new values
    dframe.at[r, 'age'] = final['age']
    dframe.at[r, 'sex'] = final['sex'].values[0]
    dframe.at[r, 'hispanic'] = final['hispanic']
    dframe.at[r, 'race'] = final['race'].values[0]
    dframe.at[r, 'SwapVal'] = True        
    dframe.at[r, 'household_size'] = final['household_size']
    dframe.at[r, 'household_tenure'] = final['household_tenure'].values[0]
    
    return dframe


# In[418]:


############################################################################################################################
#SWAPPING IMPLEMENTATION - SIMILARITY BASED --> given a county block dataset and state dataset, swaps at a given 
                                                #swaprate and threshold    
#INPUT:
#dfr = county block dataset 
#swaprate = rate of data to swap out from county block
#swap = list of unique entries prioritized for swapping
#df_state = state dataset
#thresholds: limit to neighboring values we can draw from for similarity
#-----------------------------------
#OUTPUT: 
#dframe = new de-identified county block dataset
############################################################################################################################
def swap(dfr, swaprate, swap, df_state, threshold_age, threshold_sex, threshold_race):
    
    #num_of_swaps: number of swaps remaining to do
    num_of_swaps = 0
    #import dataframe, set all rows to swapval of false
    dframe = dfr.copy()
    dframe['SwapVal'] = 'False'
    
    #get rows to swap, rows to not swap, and number of rows to be swapped
    swaps, not_swaps, rows_to_swap = get_rows_to_swap(dframe, swaprate, swap)

    #while still swaps available to make
    while num_of_swaps < rows_to_swap:
        
        #choose a row from swaps to swap, and then remove from swap list
        rows = np.arange(0,len(swaps), 1)
        r = swaps[random.choice(rows)]
        swaps.remove(r)
    
        
        #get row from state distribution to swap with r, and thresholds that returned this val
        final, finalt_r, finalt_a = find_swap(dframe, r, threshold_age, threshold_sex, threshold_race)
        
        #swap row from state distribution with r
        dframe = do_swap(dframe, r, final)

        #increment swap count
        num_of_swaps = num_of_swaps +1
     
    #reset race to their original values 
    for index, row in dframe.iterrows():
        #change from real_order indexes to actual race values
        dframe.at[index, 'race'] = real_order[row['race']]
        #if hispanic, reset race values to 0-63
        if dframe.at[index, 'race'] >62:
            dframe.at[index, 'race'] = int(dframe.at[index, 'race'])-63

    return dframe


# In[413]:











################################################### RUNNING THE CODE #####################################################










# In[414]:


# state = 'test_state'
# county = 'test_county'


# df = import_countydata(county)
# df_state = import_statedata(state)


# In[415]:


# swaprates = [.1]

# threshold_age = 5
# threshold_sex = 1
# threshold_race = 3

# for s in swaprates:
#     print(s)
#     s = float(s)
#     swapped = pick_swapvars(df)           
#     dframe = swap(df, s, swapped, df_state, threshold_age, threshold_sex, threshold_race) 
#     #print(dframe)
#     filename = "swap_runs/"+county+"/similar/swap_"+str(s)+"_a"+str(k)+".csv"
#     csv_orig_data = dframe.to_csv(filename, index = True)
#     k+=1


# In[ ]:























# In[419]:


states = ["california", "pennsylvania", "newmexico", "georgia", "northdakota", "hawaii", "missouri", "massachussets", "vermont"]
counties = ['alameda', 'armstrong', 'cibola', 'fayette', 'grandforks', 'hawaii', 'jefferson', 'nantucket', 'washington']

states = ['california']
counties = ['alameda']


# In[420]:


swaprates = np.arange(.01, 1.0, .01, float)

k = int(sys.argv[1])
k2 = int(sys.argv[2])


threshold_age = 5
threshold_sex = 1
threshold_race = 3


for i in range(0,len(states)):
    county = counties[i]
    state = states[i]
    print(county, state)
    df = import_countydata(county)
    df_state = import_statedata(state)
    swapped = pick_swapvars(df)
    while k < k2:
        print(k)
        for s in swaprates:
            s = float(s)          
            swappers = swapped.copy()
            dframe = swap(df, s, swappers, df_state, threshold_age, threshold_sex, threshold_race) 
            #print(dframe)
            filename = "swap_runs/"+county+"/similar/swap_"+str(s)+"_"+str(k)+".csv"
            csv_orig_data = dframe.to_csv(filename, index = True)
        k+=1


# In[ ]:




