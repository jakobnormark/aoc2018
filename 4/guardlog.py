#!/usr/local/bin/python3

''' Advent of code 2018-12-04 '''

class GuardLog:
    def __init__(self, input_file):
        self.input_file = input_file
        self.logs = []

    def parse_input(self):
        logs = []
        with open(self.input_file, 'r') as f:
            rows = f.readlines()
            self.parse_logs(rows)

    def parse_logs(self, rows):
        sorted_dates = []
        logs = []
        # First loop over parse all entries
        for line in rows:
            log_date = line[1:17]
            guard_id = None
            event = None
            if line.find('#') != -1:
                i = 26 # Guard ID first character columnt
                guard_id = line[i]
                i = i + 1
                while line[i] != ' ':
                    guard_id = guard_id + line[i]
                    i = i + 1
                event = 'begins shift'
            elif line.find('wakes up') != -1:
                event = 'wakes up'
            elif line.find('falls asleep') != -1:
                event = 'falls asleep'
            logs.append([log_date, guard_id, event])

        # Then sort with lambda function
        self.logs = sorted(logs, key=lambda log:log[0])

    def get_guard_ids(self):
        guard_ids = list(set([ log[1] for log in self.logs if log[1] is not None]))
        return guard_ids

    def get_guard_id_most_asleep(self):
        ''' Return guard id of the guard that spends the most time sleeping '''
        guard_id_most_asleep = None
        record_time_slept = 0
        guard_ids = self.get_guard_ids()
        for guard_id in guard_ids:
            minutes = sum(self.get_sleep_array(guard_id))
            if minutes > record_time_slept:
                print('Guard ' + str(guard_id) + ' has slept for ' + str(minutes) + ' minutes which is lponger than' + str(record_time_slept))
                guard_id_most_asleep = guard_id
                record_time_slept = minutes

        print('Guard: ' + str(guard_id_most_asleep) + ' is the sleepiest')
        return guard_id_most_asleep

    def get_sleep_array(self, guard_id):
        ''' Returns an array containing sleep per minute for a guard '''
        print('Getting minutes for guard: ' + str(guard_id))
        sleep_per_minute = [0] * 60
        correct_guard = False
        start_sleep = 0
        end_sleep = 0
        for log in self.logs:
            if log[1] is not None and int(log[1]) == int(guard_id):
                correct_guard = True
            elif log[1] is not None:
                correct_guard = False
            if correct_guard == True:
                if log[2] == 'falls asleep':
                    start_sleep = int(log[0][14:16])
                elif log[2] == 'wakes up':
                    end_sleep = int(log[0][14:16])
                    for i in range(start_sleep, end_sleep):
                        sleep_per_minute[i] = sleep_per_minute[i] + 1

        print('Guard ' + str(guard_id) + ' slept for ' + str(sum(sleep_per_minute)) + ' minutes')
        return sleep_per_minute

    def get_most_minute_slept(self, guard_id):
        ''' Return the minute the given guard is most likely to be asleep '''
        sleep_array = self.get_sleep_array(guard_id)
        print('Guard: ' + str(guard_id) +  ' Sleep array  ' + str(sleep_array))
        max = 0
        for i in range(0, len(sleep_array)):
            if sleep_array[i] > sleep_array[max]:
                print('array[i]: ' + str(sleep_array[i]) + ' is greater than max ' + str(sleep_array[max]))
                max = i

        print('Looks like most minute slept for guard_id: ' + str(guard_id + ' is minute ' + str(max)))
        return max, sleep_array[max]

    def get_id_minute(self):
        ''' Return guard id multiplied by minute '''
        guard_id = 0
        minute = 0
        #Get which guard sleeps the most
        guard_id = self.get_guard_id_most_asleep()

        #Get which minute the guard sleeps the most
        minute, _ = self.get_most_minute_slept(guard_id)
        
        return int(guard_id) * minute

    def get_id_minute_most_frequent(self):
        ''' Return guard id multiplied by minute for the most frequent minute '''
        high_guard_id = 0
        high_minute = 0
        max = 0

        for guard in self.get_guard_ids():
            minute, minutes_slept = self.get_most_minute_slept(guard)
            if minutes_slept > max:
                high_guard_id = guard
                high_minute = minute
                max = minutes_slept
        
        return int(high_guard_id) * high_minute