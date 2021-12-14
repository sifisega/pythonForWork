EMPLOYEES = {
    'Kane':[],
    'Allan':[],
    'Fraser':[]
}
JOBS = []

class Job():
    # defines a job that is a collection of shifts
    def __init__(self):
        self.shifts = []

    def add_shift(self, shift):
        self.shifts.append(shift)


class Shift():
    # defines a period of time an employee worked towards a specific job
    def __init__(self, start_time = 0, end_time = 0, date = 0, job = False, employee = ''):
        if job == False:
            self.prompt()
        else:
            self.start_time = start_time
            self.end_time = end_time
            self.length = end_time - start_time
            self.date = date
            self.employee = employee
        job.add_shift(self)
        EMPLOYEES[employee].append(self)

    def prompt(self):
        start_time = int('0o' + input('Start of shift? in 0700 format'))
        end_time = int('0o' + input('End of shift? In 1530 format'))
        date = input('Date of shift?')
        employee = input('Who worked the shift?')
        self.start_time = start_time
        self.end_time = end_time
        self.length = end_time - start_time
        self.date = date
        self.employee = employee




def new_job():
    print('woah a new job')

def new_shift():
 shift = Shift()

def main():
    while True:
        action = input("New Job?   |   New Shift?\n     J     |      S      ")
        actioin = action.lower()
        if action == 'e' or action == 'exit' or action == 'stop':
            return
        elif action == 'j':
            new_job()
        elif action == 's':
            new_shift()
        else:
            print('Sorry, unknown input, please try again :/')


main()