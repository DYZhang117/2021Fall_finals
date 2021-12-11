# coding: utf-8
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from collections import Counter
from matplotlib.pyplot import MultipleLocator

# import statistics as st

# code reference https://github.com/Zainabzav/final_projects/blob/master/montecarlo_module.py
class Laundry:
    '''
    This class contains the basic and initial information of washing machines and dryers of the laundry.
    We only consider the operation of the laundry room for a week, including five working days and a weekends.
    '''

    def __init__(self, num_WashMachine, num_Dryer, num_resident, time_interval, interval_washORdry, washTime, dryTime,
                 frequency, times):
        '''
        This function assigns the initial value for the attributes.
        :param num_WashMachine: number of washing machines
        :param num_Dryer: number of dryers
        :param num_resident: number of residents
        :param time_interval: The Maximum time to wait for the user to take out the clothes each time the washing machine or dryer finishes its work (0 min< time< 15 mins)
        :param interval_washORdry: The Maximum time interval between two machine (end-beginning) [both washing machines and dryers](0 min< time< 15 mins)
        :param washTime: Each washing time of the washing machine (25 mins<time<70 mins)
        :param dryTime: Each working time of the dryer (35 mins<time<140 mins)
        :param frequency: The washing frequencnum_residenty of each unit.
        :param times: Number of repetitions
        '''
        self.num_WashMachine = num_WashMachine
        self.num_Dryer = num_Dryer
        self.num_resident = num_resident
        self.time_interval = time_interval
        self.interval_washORdry = interval_washORdry
        self.washTime = washTime
        self.dryTime = dryTime
        self.frequency = frequency
        self.times = times

    @classmethod
    def attribute_assign(cls):
        '''
        Call the class object within the function.
        :return: class object (Laundry)
        '''
        num_WashMachine = int(input("The Number of washing machines (Integer greater than 0):"))
        num_Dryer = int(input("The Number of dryers (Integer greater than 0):"))
        num_resident = int(input("The Number of resident (greater than 0):"))
        time_interval = int(input(
            "The Maximum time to wait for the user to take out the clothes each time the washing machine or dryer finishes its work (0 min< time< 15 mins):"))
        interval_washORdry = int(input(
            "The Maximum time interval between two machine [end-beginning & both washing machines and dryers](0 min< time< 15 mins):"))
        washTime = int(input("Each washing time of the washing machine (25 mins<time<70 mins):"))
        dryTime = int(input("Each working time of the dryer (35 mins<time<140 mins):"))
        frequency = int(input("The washing frequency of each unit (* times/a week):"))
        times = int(input("The times of simulation:"))

        return cls(num_WashMachine, num_Dryer, num_resident, time_interval, interval_washORdry, washTime, dryTime,
                   frequency, times)

    def num_assign(self):
        '''
        This function will simulate the number of people visiting the laundry room every day (when frequency equals to "1")
            according to "readme.md" -- The orchard downs contains almost same number of 2B2B and 1B1B. About 40% of 2B2B
            tenants are families (more than 3 people), about 20% are one person, and about 40% are two people. For 1B1B,
            about 50% are two people living, and about 50% are living alone.
        :return: the number of people in three different units per day (when frequency equals to "1")
        '''

        num_2b2b = math.floor(self.num_resident / 2)
        num_1b1b = self.num_resident - num_2b2b

        family = math.floor(0.4 * num_2b2b)
        solitude = math.floor(0.4 * num_2b2b + 0.5 * num_1b1b)
        couple = self.num_resident - family - solitude

        # Because people have a greater probability of doing laundry on weekends, suppose the probability of doing laundry on weekends is 0.7, and the probability of doing laundry on workdays is 0.3
        num_family_weekday, num_solitude_weekday, num_couple_weekday = \
            np.random.binomial(family, 0.3), np.random.binomial(solitude, 0.3), np.random.binomial(couple,
                                                                                                   0.3)  # Number of people doing laundry on weekdays
        num_family_weekend, num_solitude_weekend, num_couple_weekend = \
            family - num_family_weekday, solitude - num_solitude_weekday, couple - num_couple_weekday  # Number of people doing laundry on weekends

        # Random allocation Specific laundry days -- Workdays (Monday~Friday), Weekends (Saturday~Sunday)
        family_weekday_assign = dict(Counter((np.random.randint(1, 6, size=num_family_weekday))))
        solitude_weekday_assign = dict(Counter((np.random.randint(1, 6, size=num_solitude_weekday))))
        couple_weekday_assign = dict(Counter((np.random.randint(1, 6, size=num_couple_weekday))))
        family_weekend_assign = dict(Counter((np.random.randint(6, 8, size=num_family_weekend))))
        solitude_weekend_assign = dict(Counter((np.random.randint(6, 8, size=num_solitude_weekend))))
        couple_weekend_assign = dict(Counter((np.random.randint(6, 8, size=num_couple_weekend))))

        tmp = [family_weekday_assign, solitude_weekday_assign, couple_weekday_assign, family_weekend_assign,
               solitude_weekend_assign, couple_weekend_assign]
        for each in tmp:
            for i in range(1, 8):
                try:
                    each[i] = each[i]
                except:
                    each[i] = 0

        # for each list stores [family_num, solitude_num, couple_num]
        Monday_num = [family_weekday_assign[1], solitude_weekday_assign[1], couple_weekday_assign[1]]
        Tuesday_num = [family_weekday_assign[2], solitude_weekday_assign[2], couple_weekday_assign[2]]
        Wednesday_num = [family_weekday_assign[3], solitude_weekday_assign[3], couple_weekday_assign[3]]
        Thursday_num = [family_weekday_assign[4], solitude_weekday_assign[4], couple_weekday_assign[4]]
        Friday_num = [family_weekday_assign[5], solitude_weekday_assign[5], couple_weekday_assign[5]]
        Saturday_num = [family_weekend_assign[6], solitude_weekend_assign[6], couple_weekend_assign[6]]
        Sunday_num = [family_weekend_assign[7], solitude_weekend_assign[7], couple_weekend_assign[7]]

        return Monday_num, Tuesday_num, Wednesday_num, Thursday_num, Friday_num, Saturday_num, Sunday_num

    def total_num_of_eachday(self):
        '''
        This function will simulate the number of people visiting the laundry room every day (when frequency equals to "k")
        :return: the number of people in three different units per day (when frequency equals to "k")
        '''
        monday_num, tuesday_num, wednesday_num, thursday_num, friday_num, saturday_num, sunday_num = \
            np.array([0] * 3), np.array([0] * 3), np.array([0] * 3), np.array([0] * 3), np.array([0] * 3), np.array(
                [0] * 3), np.array([0] * 3)

        # The number of people in line according to "frequency"
        # frequency = k execute k times num_assign();
        for _ in range(self.frequency):
            m1, t1, w1, t2, f1, s1, s2 = self.num_assign()
            monday_num += np.sum([np.array(m1), monday_num], axis=0)
            tuesday_num += np.sum([np.array(t1), tuesday_num], axis=0)
            wednesday_num += np.sum([np.array(w1), wednesday_num], axis=0)
            thursday_num += np.sum([np.array(t2), thursday_num], axis=0)
            friday_num += np.sum([np.array(f1), friday_num], axis=0)
            saturday_num += np.sum([np.array(s1), saturday_num], axis=0)
            sunday_num += np.sum([np.array(s2), sunday_num], axis=0)

        return monday_num, tuesday_num, wednesday_num, thursday_num, friday_num, saturday_num, sunday_num

    def prob_users_arrive(self, total_num_of_users):
        '''
        This function only considers people use one washing machine to repeat washing
        :param total_num_of_users: The result of total_num_of_eachday()
        :return: arrive_df (dataframe)
        '''
        # from 8am to 10pm, total 14*60 mins
        family_prob_arrive = random.choices(np.arange(0, 14 * 60),
                                            weights=([1] * (10 * 60) + [3] * (3 * 60) + [1] * (60)),
                                            k=total_num_of_users[0])
        solitude_prob_arrive = random.choices(np.arange(0, 14 * 60),
                                              weights=([1] * (10 * 60) + [3] * (3 * 60) + [1] * (60)),
                                              k=total_num_of_users[1])
        couple_prob_arrive = random.choices(np.arange(0, 14 * 60),
                                            weights=([1] * (10 * 60) + [3] * (3 * 60) + [1] * (60)),
                                            k=total_num_of_users[2])

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

        arrive_df['Total_Wait_washing_duration'] = np.nan
        arrive_df['Got_washing_machine_time'] = np.nan
        arrive_df['finish_washing_minute'] = np.nan
        arrive_df['Got_dryer_time'] = np.nan
        arrive_df['finish_dry_minute'] = np.nan  # Got_dryer_time + n*dryer_time
        arrive_df['Total_Wait_dryer_duration'] = np.nan  # Got_dryer_time - finish _washing_minute

        arrive_df = arrive_df.sort_values(by=["arrive_time"]).reset_index().drop(["index"], axis=1)

        washer_no = [0] * self.num_WashMachine
        got_washer = []
        for i in range(arrive_df.shape[0]):
            got_washer.append(arrive_df["arrive_time"][i] + min(washer_no))
            washer_no[washer_no.index(min(washer_no))] = min(washer_no) + arrive_df["ned_washing_machine"][
                i] * self.washTime

            if i + 1 < arrive_df.shape[0]:
                time_diff = random.choices(np.arange(0, self.time_interval),
                                           weights=([0] * np.arange(0, self.time_interval).size),
                                           k=1)[0]
                interval = arrive_df["arrive_time"][i + 1] - arrive_df["arrive_time"][i] - time_diff
                for j in range(len(washer_no)):
                    if washer_no[j] <= interval:
                        washer_no[j] = 0
                    else:
                        washer_no[j] -= interval

        arrive_df["Got_washing_machine_time"] = got_washer
        arrive_df['Total_Wait_washing_duration'] = arrive_df['Got_washing_machine_time'] - arrive_df['arrive_time']
        arrive_df['finish_washing_minute'] = arrive_df['Got_washing_machine_time'] + arrive_df[
            'ned_washing_machine'] * self.washTime

        return arrive_df

    def update_method(self, total_num_of_users):
        '''
        This function considers people using any available washing machine, not repeat use one machine
        :param total_num_of_users: The result of total_num_of_eachday()
        :return: arrive_df (dataframe)
        '''
        # from 8am to 10pm, total 14*60 mins
        family_prob_arrive = random.choices(np.arange(0, 14 * 60),
                                            weights=([1] * (10 * 60) + [3] * (3 * 60) + [1] * (60)),
                                            k=total_num_of_users[0])
        solitude_prob_arrive = random.choices(np.arange(0, 14 * 60),
                                              weights=([1] * (10 * 60) + [3] * (3 * 60) + [1] * (60)),
                                              k=total_num_of_users[1])
        couple_prob_arrive = random.choices(np.arange(0, 14 * 60),
                                            weights=([1] * (10 * 60) + [3] * (3 * 60) + [1] * (60)),
                                            k=total_num_of_users[2])

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

        arrive_df['Total_Wait_washing_duration'] = np.nan
        arrive_df['Got_washing_machine_time'] = np.nan
        arrive_df['finish_washing_minute'] = np.nan
        arrive_df['Got_dryer_time'] = np.nan
        arrive_df['finish_dry_minute'] = np.nan  # Got_dryer_time + n*dryer_time
        arrive_df['Total_Wait_dryer_duration'] = np.nan  # Got_dryer_time - finish _washing_minute
        arrive_df['Total_Waiting_time'] = np.nan

        arrive_df = arrive_df.sort_values(by=["arrive_time"]).reset_index().drop(["index"], axis=1)

        # washing process
        mark = []
        arrival = []
        m = 10001
        for i in range(len(arrive_df["unit"])):
            if arrive_df["unit"][i] == "couple":
                mark.append(m)
                mark.append(m)
                m += 1
                arrival.append(arrive_df["arrive_time"][i])
                arrival.append(arrive_df["arrive_time"][i])
            elif arrive_df["unit"][i] == "solitude":
                mark.append(m)
                mark.append(m)
                mark.append(m)
                m += 1
                arrival.append(arrive_df["arrive_time"][i])
                arrival.append(arrive_df["arrive_time"][i])
                arrival.append(arrive_df["arrive_time"][i])
            else:
                mark.append(m)
                mark.append(m)
                mark.append(m)
                m += 1
                arrival.append(arrive_df["arrive_time"][i])
                arrival.append(arrive_df["arrive_time"][i])
                arrival.append(arrive_df["arrive_time"][i])

        new_arrive_df = pd.DataFrame({"Mark": mark,
                                      "arrive_time": arrival})

        washing_interval = random.choices(np.arange(0, self.interval_washORdry),
                                          weights=([1] * np.arange(0, self.interval_washORdry).size),
                                          k=1)[0]
        washer_no = [0] * self.num_WashMachine
        got_washer = []
        for i in range(new_arrive_df.shape[0]):
            got_washer.append(new_arrive_df["arrive_time"][i] + min(washer_no))
            washer_no[washer_no.index(min(washer_no))] = min(washer_no) + self.washTime  # running time

            if i + 1 < new_arrive_df.shape[0]:
                time_interval = new_arrive_df["arrive_time"][i + 1] - new_arrive_df["arrive_time"][i] - washing_interval
                for j in range(len(washer_no)):
                    if washer_no[j] <= time_interval:
                        washer_no[j] = 0
                    else:
                        washer_no[j] -= time_interval

        new_arrive_df["Got_washing_machine_time"] = got_washer
        new_arrive_df['Total_Wait_washing_duration'] = new_arrive_df['Got_washing_machine_time'] - new_arrive_df[
            'arrive_time']
        new_arrive_df['finish_washing_minute'] = new_arrive_df[
                                                     'Got_washing_machine_time'] + self.washTime  # running time

        arrive_df['Got_washing_machine_time'] = list(new_arrive_df.groupby("Mark")["Got_washing_machine_time"].min())

        new_arrive_df = new_arrive_df.groupby("Mark")[
            ["arrive_time", "Total_Wait_washing_duration", "finish_washing_minute"]].max().reset_index()
        arrive_df['Total_Wait_washing_duration'] = new_arrive_df['Total_Wait_washing_duration']
        arrive_df['finish_washing_minute'] = new_arrive_df['finish_washing_minute']
        time_diff = random.choices(np.arange(0, self.time_interval),
                                   weights=([1] * np.arange(0, self.time_interval).size),
                                   k=1)[0]
        arrive_dryer_time = list(arrive_df['finish_washing_minute'] + time_diff)

        # drying process
        mark = []
        arrival = []
        m = 10001
        for i in range(len(arrive_df["unit"])):
            if arrive_df["unit"][i] == "couple":
                mark.append(m)
                m += 1
                arrival.append(arrive_dryer_time[i])
            elif arrive_df["unit"][i] == "solitude":
                mark.append(m)
                mark.append(m)
                m += 1
                arrival.append(arrive_dryer_time[i])
                arrival.append(arrive_dryer_time[i])
            else:
                mark.append(m)
                mark.append(m)
                m += 1
                arrival.append(arrive_dryer_time[i])
                arrival.append(arrive_dryer_time[i])

        new_arrive_df = pd.DataFrame({"Mark": mark,
                                      "arrive_time": arrival})
        drying_interval = random.choices(np.arange(0, self.interval_washORdry),
                                         weights=([1] * np.arange(0, self.interval_washORdry).size),
                                         k=1)[0]
        # suppose there are 2 dryers and running time is 45 minutes
        dryer_no = [0] * self.num_Dryer
        got_dryer = []
        for i in range(new_arrive_df.shape[0]):
            got_dryer.append(new_arrive_df["arrive_time"][i] + min(dryer_no))
            dryer_no[dryer_no.index(min(dryer_no))] = min(dryer_no) + self.dryTime  # running time

            if i + 1 < new_arrive_df.shape[0]:
                time_interval = new_arrive_df["arrive_time"][i + 1] - new_arrive_df["arrive_time"][i] - drying_interval
                for j in range(len(dryer_no)):
                    if dryer_no[j] <= time_interval:
                        dryer_no[j] = 0
                    else:
                        dryer_no[j] -= time_interval

        new_arrive_df["Got_dryer_time"] = got_dryer
        new_arrive_df['Total_Wait_dryer_duration'] = new_arrive_df['Got_dryer_time'] - new_arrive_df['arrive_time']
        new_arrive_df['finish_dry_minute'] = new_arrive_df['Got_dryer_time'] + self.dryTime  # running time

        arrive_df['Got_dryer_time'] = list(new_arrive_df.groupby("Mark")["Got_dryer_time"].min())

        new_arrive_df = new_arrive_df.groupby("Mark")[
            ["arrive_time", "Total_Wait_dryer_duration", "finish_dry_minute"]].max().reset_index()
        arrive_df['Total_Wait_dryer_duration'] = new_arrive_df['Total_Wait_dryer_duration']
        arrive_df['finish_dry_minute'] = new_arrive_df['finish_dry_minute']
        arrive_df['Total_Waiting_time'] = arrive_df["Total_Wait_washing_duration"] + arrive_df[
            "Total_Wait_dryer_duration"]

        return arrive_df


if __name__ == '__main__':
    laundry = Laundry.attribute_assign()

    day_list = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    fig, ax = plt.subplots(figsize=(20, 20))
    fig1, ax1 = plt.subplots(figsize=(20, 20))
    for times in range(laundry.times):
        monday_num, tuesday_num, wednesday_num, thursday_num, friday_num, saturday_num, sunday_num = laundry.total_num_of_eachday()

        mon = laundry.update_method(monday_num)
        tue = laundry.update_method(tuesday_num)
        wed = laundry.update_method(wednesday_num)
        thu = laundry.update_method(thursday_num)
        fri = laundry.update_method(friday_num)
        sat = laundry.update_method(saturday_num)
        sun = laundry.update_method(sunday_num)

        for day in day_list:
            ###############first plot##############
            if day in ["sat", "sun"]:
                scatter = ax.scatter(x=eval(day + '["arrive_time"]'), y=eval(day + '["Total_Waiting_time"]'), alpha=0.2,
                                     s=10, c='r')
            else:
                scatter = ax.scatter(x=eval(day + '["arrive_time"]'), y=eval(day + '["Total_Waiting_time"]'), alpha=0.2,
                                     s=10, c='b')

            y_major_locator = MultipleLocator(120)
            # 把y轴的刻度间隔设置为10，并存在变量里
            ax = plt.gca()
            ax.yaxis.set_major_locator(y_major_locator)
            plt.ylim(0, 3700)

            ###############second plot##############


        #每天 / 每周 total平均等待时间 / washing平均等待时间 / drying平均等待时间
        # 每天washing平均等待时间 - sum所有"Total_Wait_washing_duration"/今天访问人数
        # 每天drying平均等待时间 - sum所有"Total_Wait_dryer_duration"/今天访问人数
        print("\nThe results of {0} times:".format(times))
        day_list = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        tmp_list = []
        for eachday in day_list:
            num_user_eachday = eval(eachday + ".shape[0]")
            waiting_eachday_washing = eval(eachday + '["Total_Wait_washing_duration"].sum()')
            waiting_eachday_drying = eval(eachday + '["Total_Wait_dryer_duration"].sum()')

            avg_waiting_washing = waiting_eachday_washing / num_user_eachday
            print("avg mins of waiting washing machines in {0}: {1}mins ({2}hs)".format(eachday,
                                                                                        round(avg_waiting_washing, 0),
                                                                                        round(avg_waiting_washing / 60,
                                                                                              0)))
            avg_waiting_drying = waiting_eachday_drying / num_user_eachday
            print("avg mins of waiting dryers in {0}: {1}mins ({2}hs)".format(eachday, round(avg_waiting_drying, 0),
                                                                              round(avg_waiting_drying / 60, 0)))
            avg_waiting = (waiting_eachday_washing + waiting_eachday_drying) / num_user_eachday
            print("avg time of waiting in laundry in {0}: {1}mins ({2}hs)".format(eachday, round(avg_waiting, 0),
                                                                                  round(avg_waiting / 60, 0)))

            tmp_list.append([avg_waiting_washing, avg_waiting_drying, avg_waiting])
        # 每周平均等待时间
        avg_waiting_week_washing = sum(list(map(lambda x: x[0], [y for y in tmp_list]))) / 7
        print("avg mins of waiting washing machines for a week: {0}mins ({1}hs)".format(
            round(avg_waiting_week_washing, 0), round(avg_waiting_week_washing / 60, 0)))
        avg_waiting_week_drying = sum(list(map(lambda x: x[1], [y for y in tmp_list]))) / 7
        print("avg mins of waiting dryers for a week: {0}mins ({1}hs)".format(round(avg_waiting_week_drying, 0),
                                                                              round(avg_waiting_week_drying / 60, 0)))
        avg_waiting_week = sum(list(map(lambda x: x[2], [y for y in tmp_list]))) / 7
        print("avg time of waiting in laundry for a week: {0}mins ({1}hs)".format(round(avg_waiting_week, 0),
                                                                                  round(avg_waiting_week / 60, 0)))
    ax.axhline(y=120, color='black', linestyle='--')


