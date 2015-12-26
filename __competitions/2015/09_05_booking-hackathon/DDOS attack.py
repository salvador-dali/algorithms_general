"""
                ===============================
                =   Assumptions and problems  =
                ===============================

First of all detecting DDOS is hard. Just a time-series of data is not enough, because the big spike
of requests can be due to:
 - the marketing campaign
 - some high-traffic resource have a discussion about booking.com (there will be huge traffic if
 the most popular reddit thread will be  speaking about booking.com)
 - some error on the site (your developers messed up with redirects or something similar)
 - a lot of other things

=== So the first assumption we have is that we trust a time-series.  ===

Second, time-series will give us only historical data, so we will be able to figure out that
"yesterday from 6-20 to 6-22 there was a DDOS attack". This is still helpful, but more helpful would
be to have a real-time analytics that would tell, "hey admin, NOW we are on DDOS attack". For this
we would need an online algorithm https://en.wikipedia.org/wiki/Online_algorithm

=== So the second assumption is that we can just use historical data ===

Third how often do we analyse the time-series. Mostly this is needed to figure out whether the data
fits in ram (space complexity) and how much time will it take (time complexity).

=== So the third assumption is that we can analyse the data once per day (or at intervals close to this) ==
Having this assumption, the data we have 86400 (seconds in a day) will easily fit the RAM.


                ===============================
                =   Idea for an algorithm     =
                ===============================


Having these assumption, the important question is: "What do we consider a DDOS attack". Because
DDOS for one host (booking.com) is just a tiny traffic for another host (google.com). We need to
make an "intelligent guess" from the data we have. We can manipulate the whole data in memory to
calculate some statistic and use it as our guess.

Statistics should be 'robust' (https://en.wikipedia.org/wiki/Robust_statistics) and Median
Absolute Deviation (https://en.wikipedia.org/wiki/Median_absolute_deviation) is a good choice.

It is easy to calculate and to understand (think about it as a robust standard deviation) it. Also
one can use statistical theory to get outliers knowing it.

Using an idea of 6-sigma (https://en.wikipedia.org/wiki/Six_Sigma), which is in 'layman term'
means that an event bigger than mean + 6 std will have a probability of occurrence less than
0.0005%, one can come up with a similar robust metric

mean + 6 * mad
This will be our threshold. Everything above it will be considered an outlier (we do not care
about small outliers (why we had received such low traffic) , so will not even consider the idea
of mean - 6 * mad).

If we see and outliers, this means that this is a potential DDOS attack and should be recorder.
Recording is straight forward and I will not focus on it


                ===============================
                =   Complexity                =
                ===============================

The only dependency I have is only to shorten the code. It is straight-forward to rewrite it without
numpy.

Space complexity.
The data fits in memory and one will need less than 86400 * 10 * bigInt < 7 MB of RAM

Time complexity.
median, median absolute deviation and detecting the DDOS takes linear amount of time. So it will
be blazingly fast.


                ===============================
                =   Thoughts                  =
                ===============================
It is not hard to convert it to online algorithm using a sliding window approach.
http://stackoverflow.com/q/8269916/1090562
"""

import numpy as np

def medianAbsoluteDeviation(arr):
    """ MAD: https://en.wikipedia.org/wiki/Median_absolute_deviation
    Robust version of standard deviation

    :param arr: numpy array
    :return:    MAD (one number)
    """
    med = np.median(arr)
    return np.median(np.abs(arr - med))

def detectDDOS(timeSeries, sigma=6):
    """ Identifies spikes of potential DDOS attacks
    Takes an array of elements in the format [<epoch>, <number of requests>] and
    returns an array of [epoch_start, epoch_end]

    :param timeSeries:  array of [<epoch>, <number of requests>]
    :param sigma:       positive number. https://en.wikipedia.org/wiki/Six_Sigma
    :return:            array of DDOS attacks [ts_start, ts_end]
    """
    req_num = np.array([i[1] for i in timeSeries])      # extract number of requests, store as NP
    median = np.median(req_num)                         # get median

    mad = medianAbsoluteDeviation(req_num)              # get median absolute deviation
    threshold = median + sigma * mad                    # everything above is a DDOS

    have_started, attacks = False, []
    for ts, req in timeSeries:
        if req > threshold:
            if not have_started:
                have_started = True
                start, last_ts = ts, ts
            else:
                last_ts += 1
        elif have_started:
            have_started = False
            attacks.append([start, last_ts])

    return attacks


timeSeries = [[123456, 45],[123457, 46],[123458, 1000],[123459, 1129],[123460, 999],[123461, 47],[123462, 50],[123463, 67],[123464,35],[123465, 50],[123466, 10000],[123467, 5000],[123468,60]]
attacks = detectDDOS(timeSeries)
print attacks