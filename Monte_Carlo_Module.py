# coding: utf-8
import random

import numpy as np
import pandas as pd
import math
from collections import deque, OrderedDict
from collections import Counter


# import statistics as st

def num_assign(num_resident):
    # frequency = k execute k times num_assign();
    # according to "readme.md" -- The orchard downs contains almost same number of 2B2B and 1B1B. About 40% of 2B2B
    # tenants are families (more than 3 people), about 20% are one person, and about 40% are two people. For 1B1B,
    # about 50% are two people living, and about 50% are living alone.

    num_2b2b = math.floor(num_resident / 2)
    num_1b1b = num_resident - num_2b2b

    family = math.floor(0.4 * num_2b2b)
    solitude = math.floor(0.4 * num_2b2b + 0.5 * num_1b1b) ###???0.2* num_2b2b?
    couple = num_resident - family - solitude

    # Because people have a greater probability of doing laundry on weekends, suppose the probability of doing laundry on weekends is 0.7, and the probability of doing laundry on workdays is 0.3
    num_family_weekday, num_solitude_weekday, num_couple_weekday = \
        np.random.binomial(family, 0.3), np.random.binomial(solitude, 0.3), np.random.binomial(couple,
                                                                                               0.3)  # Number of people doing laundry on weekdays
    num_family_weekend, num_solitude_weekend, num_couple_weekend = \
        family - num_family_weekday, family - num_solitude_weekday, family - num_couple_weekday  # Number of people doing laundry on weekends

    # Random allocation Specific laundry days -- Workdays (Monday~Friday), Weekends (Saturday~Sunday)
    family_weekday_assign = dict(Counter((np.random.randint(1, 6, size=num_family_weekday))))
    solitude_weekday_assign = dict(Counter((np.random.randint(1, 6, size=num_solitude_weekday))))
    couple_weekday_assign = dict(Counter((np.random.randint(1, 6, size=num_couple_weekday))))
    family_weekend_assign = dict(Counter((np.random.randint(6, 8, size=num_family_weekend))))
    solitude_weekend_assign = dict(Counter((np.random.randint(6, 8, size=num_solitude_weekend))))
    couple_weekend_assign = dict(Counter((np.random.randint(6, 8, size=num_couple_weekend))))

    # for each list stores [family_num, solitude_num, couple_num]
    Monday_num = [family_weekday_assign[1], solitude_weekday_assign[1], couple_weekday_assign[1]]
    Tuesday_num = [family_weekday_assign[2], solitude_weekday_assign[2], couple_weekday_assign[2]]
    Wednesday_num = [family_weekday_assign[3], solitude_weekday_assign[3], couple_weekday_assign[3]]
    Thursday_num = [family_weekday_assign[4], solitude_weekday_assign[4], couple_weekday_assign[4]]
    Friday_num = [family_weekday_assign[5], solitude_weekday_assign[5], couple_weekday_assign[5]]
    Saturday_num = [family_weekend_assign[6], solitude_weekend_assign[6], couple_weekend_assign[6]]
    Sunday_num = [family_weekend_assign[7], solitude_weekend_assign[7], couple_weekend_assign[7]]

    # Return the number of people in three different units per day
    return Monday_num, Tuesday_num, Wednesday_num, Thursday_num, Friday_num, Saturday_num, Sunday_num


def total_num_of_eachday(num_resident, frequency=1):
    monday_num, tuesday_num, wednesday_num, thursday_num, friday_num, saturday_num, sunday_num = \
        np.array([0] * 3), np.array([0] * 3), np.array([0] * 3), np.array([0] * 3), np.array([0] * 3), np.array(
            [0] * 3), np.array([0] * 3)

    # The number of people in line according to "frequency"
    for _ in range(frequency):
        m1, t1, w1, t2, f1, s1, s2 = num_assign(num_resident)
        monday_num += np.sum([np.array(m1), monday_num], axis=0)
        tuesday_num += np.sum([np.array(t1), tuesday_num], axis=0)
        wednesday_num += np.sum([np.array(w1), wednesday_num], axis=0)
        thursday_num += np.sum([np.array(t2), thursday_num], axis=0)
        friday_num += np.sum([np.array(f1), friday_num], axis=0)
        saturday_num += np.sum([np.array(s1), saturday_num], axis=0)
        sunday_num += np.sum([np.array(s2), sunday_num], axis=0)

    return monday_num, tuesday_num, wednesday_num, thursday_num, friday_num, saturday_num, sunday_num


# code reference https://github.com/Zainabzav/final_projects/blob/master/montecarlo_module.py
class Laundry:
    '''
    This class contains the basic and initial information of washing machines and dryers of the laundry.
    We only consider the operation of the laundry room for a week, including five working days and a weekends.
    '''

    def __init__(self, num_WashMachine, num_Dryer, num_resident, time_interval, washTime, dryTime, frequency):
        '''
        This function assigns the initial value for the attributes.
        :param num_WashMachine: number of washing machines
        :param num_Dryer: number of dryers
        :param num_resident: number of residents
        :param time_interval: The time to wait for the user to take out the clothes each time the washing machine or dryer finishes its work (0 min< time< 15 mins)
        :param washTime: Each washing time of the washing machine (25 mins<time<70 mins)
        :param dryTime: Each working time of the dryer (35 mins<time<140 mins)
        :param frequency: The washing frequencnum_residenty of each unit.
        '''
        self.num_WashMachine = num_WashMachine
        self.num_Dryer = num_Dryer
        self.num_resident = num_resident
        self.time_interval = time_interval
        self.washTime = washTime
        self.dryTime = dryTime
        self.frequency = frequency

    @classmethod
    def attribute_assign(cls):
        '''
        Call the class object within the function.
        :return: class object (Laundry)
        '''
        num_WashMachine = int(input("The Number of washing machines (Integer greater than 0):"))
        num_Dryer = int(input("The Number of dryers (Integer greater than 0):"))
        num_resident = int(input("The Number of resident (greater than 0):"))
        time_interval = input(
            "The time to wait for the user to take out the clothes each time the washing machine or dryer finishes its work (0 min< time< 15 mins):")
        washTime = input("Each washing time of the washing machine (25 mins<time<70 mins):")
        dryTime = input("Each working time of the dryer (35 mins<time<140 mins):")
        frequency = input("The washing frequency of each unit (* times/a week):")

        return cls(num_WashMachine, num_Dryer, num_resident, time_interval, washTime, dryTime, frequency)

    def prob_users_arrive(self, total_num_of_users):
        '''
        This function
        :param total_num_of_users: amount of residents plan to use washing machines and dryers (
        Monday_num, Tuesday_num, Wednesday_num, Thursday_num, Friday_num, Saturday_num, Sunday_num) [family_num, solitude_num, couple_num]
        :return:
        '''
        # First, we plan to divide each day into several intervals every half hour, assuming that a new batch of
        # users will come every half hour (notice that the washing room is open from 8 am - 10 pm):
        #   -> 29 time points
        family_prob_arrive = random.choices(np.arange(1, 30), weights=([1] * 20 + [3] * 7 + [1] * 2),
                                            k=total_num_of_users[0])
        solitude_prob_arrive = random.choices(np.arange(1, 30), weights=([1] * 20 + [3] * 7 + [1] * 2),
                                              k=total_num_of_users[1])
        couple_prob_arrive = random.choices(np.arange(1, 30), weights=([1] * 20 + [3] * 7 + [1] * 2),
                                            k=total_num_of_users[2])
        waiting_washing = 0
        waiting_dryer = 0
        hour = 1

        arrive_df = pd.DataFrame(family_prob_arrive, columns=['arrive_time']).sort_values(['arrive_time'])
        arrive_df["unit"] = "family"
        arrive_df["ned_washing_machine"] = 3 if self.frequency == 1 else 2
        arrive_df["ned_dryer"] = 2 if self.frequency == 1 else 1
        tmp1 = pd.DataFrame(solitude_prob_arrive, columns=['arrive_time']).sort_values(['arrive_time'])
        tmp1["unit"] = "solitude"
        tmp1["ned_washing_machine"] = 3 if self.frequency == 1 else 2
        tmp1["ned_dryer"] = 2 if self.frequency == 1 else 1
        tmp2 = pd.DataFrame(couple_prob_arrive, columns=['arrive_time']).sort_values(['arrive_time'])
        tmp2["unit"] = "couple"
        tmp2["ned_washing_machine"] = 2 if self.frequency == 1 else 1
        tmp2["ned_dryer"] = 1 if self.frequency == 1 else 1

        arrive_df = arrive_df.append(tmp1)
        arrive_df = arrive_df.append(tmp2)

        arrive_df['Got_washing_machine_time'] = np.nan
        arrive_df['finish_washing_minute'] = np.nan
        arrive_df['Got_dryer_time'] = np.nan
        arrive_df['finish_dry_minute'] = np.nan
        arrive_df['Wait_washing_duration'] = np.nan
        arrive_df['Wait_dryer_duration'] = np.nan
        arrive_df['finish_washing_queue'] = np.nan
        arrive_df['finish_drying_queue'] = np.nan
        arrive_df = arrive_df.reset_index().drop(["index"], axis=1)

        counts = arrive_df['arrive_time'].value_counts()
        washing_machine_in_use = 0
        washing_dryer_in_use = 0
        for minute in range(1, 30):
            if minute not in counts.index.values:
                patrons_this_minute = 0
            else:
                patrons_this_minute = counts[minute]

            # for washing process
            while waiting_washing > 0 and (washing_machine_in_use < self.num_WashMachine):
                current_available = self.num_WashMachine - washing_machine_in_use
                while current_available > 0:
                    oldest_arrive_min = arrive_df['arrive_time'][
                        (arrive_df['Got_washing_machine_time'].isnull() == True) & (
                                arrive_df['finish_washing_queue'].isnull() == True)].min()
                    if oldest_arrive_min <= minute:
                        nulls = arrive_df.loc[lambda x: (x['Got_washing_machine_time'].isnull() == True) & (
                                x['arrive_time'] == oldest_arrive_min)]

                        pass

            # for drying process
            pass
        return
