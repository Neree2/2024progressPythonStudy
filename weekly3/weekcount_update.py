class WeekCount:

    def ask_dayinyear(self):
        count=0
        year=int(input('how many years do you want to count? : '))
        ask=str(input('whole year? '))
        if ask=='no':
            for _ in range(year):
                total=int(input('365 or 366 days?: '))
                ask2=str(input('Do you wanna count the day that have passed or left: '))
                if ask2=='passed':
                    til=int(input('how many days passed: '))
                    count+=(til)
                elif ask2=="left":
                    gone=int(input('how many days passed: '))
                    count+=(total-gone)
            return count
        elif ask=='yes':
            ask2=str(input('all?: '))
            if ask2=='yes':
                for _ in range(year):
                    total=int(input('how many days in year: '))
                    count+=(total)
                return count
            elif ask2=='no':
                year2=int(input('how many year?: '))
                for _ in range(year2):
                    total=int(input('365 or 366 days?: '))
                    ask2=str(input('Do you wanna count the day that have passed or left: '))
                    if ask2=='passed':
                        til=int(input('how many days passed: '))
                        count+=(til)
                    elif ask2=="left":
                        gone=int(input('how many days passed: '))
                        count+=(total-gone)
                return count
        else:
            print('no')

    def week_count(self):
        toal=self.ask_dayinyear()
        a=toal/7
        print(a)

weekthn=WeekCount()
weekthn.week_count()