# RainfallProcessor.py
# Kyle:Connolly:A00371085:csc227107
# Submission 06
# Retrieving and Processing Rainfall Data Classes
"""
An event I hadn't planned for was if user input no year at all, in this
assignment I have the program terminate. I have also tried to open the data
file via `with - as` operators, which has saved me a bit of code. Also,
I've changed the list of month to a tuple of MONTHS; becuase those values
remain constant.

From sys, I'm using `platform` to try and test the general OS the programm
is running on and que the proper shell cmd based on the result. It's worked
for me on my Linux machine, please let me know if you've had trouble with it.

"""


class RainfallProcessor(object):
    def __init__(self, rainfall_file):
        self.rainfall_file = rainfall_file

    from sys import argv, exit, platform
    from os import system

    MONTHS = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November",
              "December"]

    def process_rainfall_file(self):
        self.clear()
        global year
        year = input("\nEnter year for which you want rainfall data: ")
        with open(self.rainfall_file) as infile:
            while year:
                current_line = infile.readline().strip()
                if year == current_line:
                    global rain_line
                    rain_line = infile.readline().strip()
                    self.title()
                    self.month_stats()
                    break
                if not current_line and current_line != year:
                    print("\nNo rainfall data found for year {}.".format(year))
                    self.pause()
                    self.repeat()

    def month_stats(self):
        global rain_line
        rain_float = [float(n) for n in rain_line.split()]
        months = """\
January..... {0}  July........ {6}
February.... {1}  August...... {7}
March....... {2}  September... {8}
April....... {3}  October..... {9}
May......... {4}  November.... {10}
June........ {5}  December.... {11}\
        """.format(*rain_float)
        total = sum(rain_float)
        avg = total / 12
        high = self.MONTHS[rain_float.index(max(rain_float))]
        low = self.MONTHS[rain_float.index(min(rain_float))]
        calc = [total, avg, high, low]
        stats = """\
===== Total rainfall for the year... {:.1f}
===== Average monthly rainfall...... {:.1f}
===== Month with highest rainfall... {}
===== Month with lowest rainfall.... {}\
        """.format(*calc)
        print(months)
        print(stats)
        self.pause()
        self.repeat()

    def clear(self):
        if self.platform.lower() is 'linux' or 'darwin':
            self.system("clear")
        elif self.platform.lower() is 'windows':
            self.system("cls")

    def ok(self):
        print("OK ... Program now terminating.")

    def repeat(self):
        ask = input("\nDo it again for another year? [[y]/n] ")
        if ask == "n":
            print()
            self.ok()
            self.pause()
            self.exit()
        else:
            self.process_rainfall_file()

    def pause(self):
        input("Press Enter to continue ... ")

    def title(self):
        "Prints the heading for rainfall data."
        print("\n===== Rainfall Summary for {}".format(year))
