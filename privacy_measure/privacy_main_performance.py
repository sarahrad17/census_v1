#Re-Written Privacy Measurement Functions for 1000X performance increase
import pandas as pd

races = ['White alone',
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

races2 = ['Total!!Population of one race!!White alone',
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

#re_id function re-written using pandas operations for massive performance improvements
#note this assumes that index keys are the same between the index vals
#validated aganist original privacy functions for accuracy
def re_id(D, P, M, theta_d, theta_p, indices, swapped):
    # D: de-identified dataset
    # P: public dataset
    # M: set of attributes shared between D and P
    # alpha: attribute set size limit in M. we only examine attribute tuples where at most alpha entries in M have that tuple
    # we remove alpha here and look at sets of all sizes, since runtime is not an issue
    # theta_d: attribute set size limit in D. we only examine attribute tuples with at most theta_d matching entries in D
    # theta_p: attribute set size limit in P.
    # theta_d, and theta_p are used to limit compute costs. we can set them to |D|
    # indices: list of index triples. a triple (i,j, k) indicates that attribute k in M corresponds to attribute i in D and attribute j in P
    # paper used alpha=7, theta_d = 10, theta_p = 5
    # D, P, and M must have attributes in the same order. matching attributes must come first in D and P
    # swapped: indicates whether D was anonymized via swapping
    num_vulnerable = 0
    num_identified = 0
    V = [] #list of vulnerable entries
    for row in M:
        #true case
        att_val_combos = D.loc[(D['age'] == row[0]) &
                               (D['race'] == row[1]) &
                               (D['household_size'] == row[2])]
        if len(att_val_combos) <= theta_d and len(att_val_combos) > 0:
            #false case - not using indices in theory fine
            p_matches = P.loc[(P['age'] == row[0]) &
                                   (P['race'] == row[1]) &
                                   (P['household_size'] == row[2])]
            if len(p_matches) <= theta_p and len(p_matches) > 0:
                if swapped:
                    count = att_val_combos[att_val_combos['SwapVal'] == False].shape[0]
                    num_vulnerable += count
                    if (len(p_matches) == 1):
                        num_identified += count
                else:
                    num_vulnerable += len(p_matches)
                    if (len(p_matches) == 1):
                        num_identified += len(p_matches)
                V.append([row, att_val_combos, p_matches])
    return V, num_vulnerable, num_identified


##########################################################################################################################
# CREATE PUBLIC DATA
# input: csv containing block data
# output: dataframe containing public dataset with age and sex
##########################################################################################################################

def create_public_data_age_sex(path, races):
    df = pd.read_csv(path)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    for col_name, data in df.items():
        if col_name == 'race':
            oof = 0
            for d in data:
                if d in races:
                    df.at[oof, 'race'] = races.index(d)
                oof += 1
            oof = 0
            for d in data:
                if d in races2:
                    df.at[oof, 'race'] = races2.index(d)
                oof += 1

    return df


def measure_privacy(county, races):
    # prints privacy value for each swap rate for the given county
    swap_rates = ['0.01', '0.060000000000000005', '0.11', '0.21000000000000002', '0.31000000000000005', '0.41000000000000003',
                  '0.51', '0.6100000000000001', '0.7100000000000001', '0.81', '0.91', '0.9600000000000001']

    indices = [['age', 'age', 0], ['race', 'race', 1], ['household_size', 'household_size', 2]]
    # Set up datasets

    # Common attributes
    M = []
    for age in range(90):
        for race in range(0, len(races)):
            for size in [1, 2, 3, 4]:
                M.append([age, race, size])

    # Original dataset
    P = create_public_data_age_sex('../homemade_data/' + county + '.csv', races)

    # create arrays where we will record privacy values
    stats1 = []
    stats2 = []

    # evaluate privacy for datasets of each swap rate
    for rate in swap_rates:
        print('swap rate: ' + str(rate))
        D1 = create_public_data_age_sex('../swapping/swap_runs/' + county + '/similar/swap_' + rate + '.csv', races)
        D2 = create_public_data_age_sex('../swapping/swap_runs/' + county + '/random/swap_' + rate + '.csv', races)
        V1, num_vulnerable1, num_identified1 = re_id(D1, P, M, 3, 3, indices, True)
        stats1.append([rate, num_vulnerable1, num_identified1])
        V2, num_vulnerable2, num_identified2 = re_id(D2, P, M, 3, 3, indices, True)
        stats2.append([rate, num_vulnerable2, num_identified2])
        print("Random: ", [rate, num_vulnerable2, num_identified2])
        print("Similar: ", [rate, num_vulnerable1, num_identified1])
    return stats1, stats2

counties = ['Alameda', 'Armstrong', 'Cibola', 'Fayette', 'GrandForks', 'Hawaii', 'Jefferson', 'Nantucket', 'Washington']
lines = []

for county in counties:
    lines.append(f'\n\n{county}\n----------------------------------------------')
    print('now analyzing ', county)
    wash1, wash2 = measure_privacy(county, races)
    print(county, ' similar:')
    print(wash1)
    lines.append(f'{county} Similar:\n{wash1}')
    print(county, ' random:')
    print(wash2)
    lines.append(f'{county} Random:\n{wash2}')

with open('privacy_results.txt', "w") as f:
    for l in lines:
        f.write(l + "\n")
