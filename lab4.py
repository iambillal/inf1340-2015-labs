#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015
    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it

PROVINCIAL_TAX = 0.05
FEDERAL_TAX = 0.025
TOTAL_TAX = 0.075
TOTAL_SALE = 1.075

def calc_provincial_tax(amount):
    provincial_tax = amount * PROVINCIAL_TAX_RATE
    return provincial_tax

def calc_federal_tax(amount):
    federal_tax = amount * FEDERAL_TAX_RATE
    return federal_tax

def calc_total_tax(provincial_tax, federal_tax):
    total_tax = provincial_tax + federal_tax
    return total_tax

def calc_subtotal(amount, total_tax):
    sub_total = amount + total_tax
    return sub_total

def bill_of_sale(purchase):

    provincial_tax = calc_provincial_tax(purchase)
    federal_tax = calc_federal_tax(purchase)
    total_tax = calc_total_tax(provincial_tax, federal_tax)
    subtotal = calc_subtotal(purchase, total_tax)

def print_your_bill(purchase, prov_tax, fed_tax, all_tax, sale_price):
    with open(file_name, "a") as output_file:
        output_file.write("\n\nAmount of purchase: {0:.2f}".format(purchase))
        output_file.write("\nProvincial tax: {0:.2f}".format(prov_tax))
        output_file.write("\nFederal tax: {0:.2f}".format(fed_tax))
        output_file.write("\nTotal tax: {0:.2f}".format(all_tax))
        output_file.write("\nTotal sale: {0:.2f}".format(sale_price))

def bill_of_sale(purchase):

    print ("Amount of purchase: {0:.2f}".format(purchase))
    print ("Provincial tax: {0:.2f}".format(purchase * .05))
    print ("Federal tax: {0:.2f}".format(purchase * .025))
    print ("Total tax: {0:.2f}".format(purchase * .075))
    print ("Total sale: {0:.2f}".format(purchase * 1.075))

bill_of_sale(100)
