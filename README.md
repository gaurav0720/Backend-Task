# Backend-Task
An Back-end Development Task assigned by a company for the evaluation of the coding skills and the understandings regarding the development.

This program tracks point balances for different payers and allows users to spend points based on a set of rules.

Usage:
To use the program, you will need to have Python 3 installed on your computer. You can then run the program from the command line by typing the following:

python3 spend_points.py <points_to_spend> <transactions_file>
Replace <points_to_spend> with the number of points you want to spend, and <transactions_file> with the name of the CSV file containing the transactions.

For example, if you want to spend 5000 points and the transactions file is called transactions.csv, you would run the following command:

python3 spend_points.py 5000 transactions.csv

The program will then output a dictionary containing the final point balances for each payer.

Input Format:
The transactions file should be a CSV file with the following columns:

payer: the name of the payer (string)
points: the number of points earned or spent (integer)
timestamp: the timestamp of the transaction in ISO 8601 format (string)

For example:

payer,points,timestamp
DANNON,1000,2020-11-02T14:00:00Z
UNILEVER,200,2020-10-31T11:00:00Z
DANNON,-200,2020-10-31T15:00:00Z
MILLER COORS,10000,2020-11-01T14:00:00Z
DANNON,300,2020-10-31T10:00:00Z

Output Format:
The program will output a dictionary in JSON format containing the final point balances for each payer.
For example:
{
    "DANNON": 1000,
    "UNILEVER": 0,
    "MILLER COORS": 5300
}

Rules:
When spending points, the program follows the following rules:

The oldest points should be spent first (based on the timestamp of the transaction).
No payer's points should go negative.
License
This program is licensed under the MIT License. See the LICENSE file for more information.

Acknowledgments
This program was created by Gaurav Rathi as a coding exercise.
