import sys
import csv
from datetime import datetime

def spend_points(points_to_spend, transactions):
    # Sort transactions by timestamp
    transactions = sorted(transactions, key=lambda x: x["timestamp"])
    
    # Create a dictionary to track payer balances
    payer_balances = {}
    
    # Calculate initial total balances for every single payer
    for transaction in transactions:
        payer = transaction["payer"]
        points = transaction["points"]
        if payer not in payer_balances:
            payer_balances[payer] = 0
        payer_balances[payer] += points
    
    # Calculate initial total balances for every single payer
    for trancs in transactions:
        payer = trancs["payer"]
        points = trancs["points"]
        points_to_spend = points_to_spend - points
        if points_to_spend < 0:
            payer_balances[payer] = -1 * points_to_spend
            break
        else:
            payer_balances[payer] = payer_balances[payer] - points
        
    return(payer_balances)

if __name__ == '__main__':
    # get command-line arguments
    points_to_spend = int(sys.argv[1])
    transactions_file = sys.argv[2]

    # read transactions from CSV file
    transactions = []
    with open(transactions_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # convert timestamp string to datetime object
            timestamp_str = row['timestamp'].replace('Z', '')
            row['timestamp'] = datetime.fromisoformat(timestamp_str)
            # convert points string to int
            row['points'] = int(row['points'])
            transactions.append(row)

    # spend points and return payer balances
    balances = spend_points(points_to_spend, transactions)
    print(balances)