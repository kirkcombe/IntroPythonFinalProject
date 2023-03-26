import csv
import matplotlib.pyplot as plt
import pandas as pd
from statistics import mean  # importing mean function


def read_data():
    data = []
    with open('sales.csv', 'r') as sales_csv:  # reading csv file
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data


def run():
    data = read_data()
    sales = []  # creating arrays
    expenditure = []
    profit = []
    percent = [0]
    months=[]
    for row in data:  # looping through the data
        sale = int(row['sales'])  # turning sales into integer
        sales.append(sale)  # adding each sale row
        exp = int(row['expenditure'])
        expenditure.append(exp)
        indsale = int(row['sales'])  # getting each sale
        indexpenditure = int(row['expenditure'])  # getting each expenditure
        indprofit = indsale - indexpenditure  # calculating each profit
        row['indprofit'] = indprofit  # adding on profit
        profit.append(indprofit)
    total = sum(sales)
    Maxsales = max(sales)
    total2 = round(mean(expenditure),2)
    total3 = sum(profit)
    total4= round(mean((profit)),2)
    print('Total sales: £{}'.format(total))
    print('\nMax sales: £{}'.format(Maxsales))
    print('\nMean expenditure is: £{} '.format(total2))
    print('\nTotal profit is: £{}'.format(total3))
    print('\nMean profit is: £{}'.format(total4))
    #print(data)
    for singlerow in data:
        if Maxsales == int(singlerow['sales']):
           print('\nThe month with max sales is:{} with £{}\n'.format(singlerow['month'], singlerow['sales']))


    for i in range(1, 12):
        row['percent'] = percent
        percent.append(((sales[i] - sales[i - 1]) / sales[i - 1]) * 100)

    #for i in percent:
        #if i > 0:
            #print("The sales increased by", round(i, 2), "%")
        #else:
            #print("The sales decreased by", round(-i, 2), "%")
    for d, p in zip(data, percent):
        d["percent"] = p
    #print(data)
    #loop round each row get it to check whether + or - change then print month and value
    for singlerow in data:
        if singlerow['percent'] >0:
           print('In {} the sales increased by {}%'.format(singlerow['month'], round(singlerow['percent'],2)))
        else:
            print('In {} the sales decreased by {}%'.format(singlerow['month'], round(singlerow['percent'],2)))
    # writing new csv file to include profit
    field_names = ['year', 'month', 'sales', 'expenditure', 'indprofit', 'percent']

    with open('newdata.csv', 'w+') as csv_file:
        spreadsheet1 = csv.DictWriter(csv_file, fieldnames=field_names)
        spreadsheet1.writeheader()
        spreadsheet1.writerows(data)

    # Load data for graph
    data1 = pd.read_csv('newdata.csv')
    # checking data is in file
    print('\n',data1)
    # Ask used which graph they want
    chooseY=input('\nWould you like to plot sales or profit or both? ' )
    #setting x axis
    x = range(len(data1['month']))
    #if loop to determine y axis and turn input to lower case
    if chooseY.lower()=='sales':
        ax=data1['sales']
        lab='Sales'
        title='Sales per month'
        plt.plot(x, ax, "-b", label=lab)
    elif chooseY.lower()=='profit':
        ax=data1['indprofit']
        lab='Profit'
        title='Profit per month'
        plt.plot(x, ax, "-b", label=lab)

    elif chooseY.lower()=='both':

        lab=' '
        title='Sales and profit per month'
        plt.plot(x, data1['indprofit'], "-b", label="Profit")
        plt.plot(x, data1['sales'], "-g", label="Sales")
    # error message and exit if something else entered
    else:
        print("not a valid input")
        quit()
    #graph formatting
    plt.xticks(x, data1['month'])
    plt.xlabel('Month')
    plt.ylabel(f'{lab} in £')
    plt.legend(loc="upper left")
    plt.title(title)
    plt.show()


run()
