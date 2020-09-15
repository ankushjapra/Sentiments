# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sqlite3
'''
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
'''
def import_db(db_name):
    try:
        conn = sqlite3.connect(db_name)
        print("Database opened successfully")
        cur=conn.cursor()
        records=cur.execute("SELECT * FROM Tweets where airline_sentiment='positive'")
        count_pos=0
        for row in records:
            count_pos=count_pos+1
        print("Positive Reviews :",count_pos)
        records=cur.execute("SELECT * FROM Tweets where airline_sentiment='negative'")
        count_neg=0
        for row in records:
            count_neg=count_neg+1
        print("Negative Reviews :",count_neg)
        records=cur.execute("SELECT * FROM Tweets where airline_sentiment='neutral'")
        count_neutral=0
        for row in records:
            count_neutral=count_neutral+1
        print("Neutral Reviews :",count_neutral)
    except Exception as e:
        print("Encountered error during connecting datasets: ",str(e))

    conn.close()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import_db('database.sqlite')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
