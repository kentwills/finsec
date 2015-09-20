"""
Function name and input names should match the financial variable exatly,
these functions are automatically imported and matched by name and argument.
"""
# Activity Ratios
from __future__ import absolute_import
from __future__ import unicode_literals


def receivables_turnover(total_revenue, receivable):
    return total_revenue / receivable


def days_of_sales_outstanding(receivables_turnover):
    return 365 / receivables_turnover


def inventory_turnover(cost_of_goods_sold, inventories):
    return cost_of_goods_sold / inventories


def days_of_inventory_on_hand(inventory_turnover):
    return 365 / inventory_turnover


def payables_turnover(total_expenses, accounts_payable):
    return total_expenses / accounts_payable


def days_of_payables(payables_turnover):
    return 365 / payables_turnover


def total_asset_turnover(total_revenue, total_assets):
    return total_revenue / total_assets


def working_capital(total_current_assets, total_current_liabilities):
    return total_current_assets - total_current_liabilities


def working_capital_turnover(total_revenue, working_capital):
    return total_revenue / working_capital


# Liquidity Ratios
def current_ratio(total_current_assets, total_current_liabilities):
    return total_current_assets / total_current_liabilities


def quick_ratio(cash_and_short_term_investments, receivable, total_current_liabities):
    return (cash_and_short_term_investments - receivable) / total_current_liabities


def cash_ratio(cash_and_short_term_investments, total_current_liabilities):
    return cash_and_short_term_investments / total_current_liabilities


def cash_conversion_cycle(days_of_sales_outstanding, days_of_inventory_on_hand, days_of_payables):
    return days_of_sales_outstanding + days_of_inventory_on_hand - days_of_payables


# Solvency Ratios
def total_debt(short_term_debt, long_term_debt):
    return short_term_debt + long_term_debt


def total_capital(total_debt, total_shareholder_equity):
    return total_debt + total_shareholder_equity


def debt_to_equity_ratio(total_debt, total_shareholder_equity):
    return total_debt / total_shareholder_equity


def debt_to_capital_ratio(total_debt, total_capital):
    return total_debt / total_capital


def debt_to_assets_ratio(total_debt, total_assets):
    return total_debt / total_assets


def financial_leverage_ratio(total_assets, total_shareholder_equity):
    return total_assets / total_shareholder_equity


def interest_coverage_ratio(operating_income, interest_expense):
    return operating_income / interest_expense


# profitability ratios
def net_profit_margin(net_income, total_revenue):
    return net_income / total_revenue


def gross_profit_margin(gross_profit, total_revenue):
    return gross_profit / total_revenue


def operating_profit_margin(operating_income, total_revenue):
    return operating_income / total_revenue


def return_on_assets(net_income, interest_expense, total_assets):
    return (net_income + .65 * interest_expense) / total_assets


def operating_return_on_assets(operating_income, total_assets):
    return operating_income / total_assets


def return_on_capital(operating_income, total_capital):
    return operating_income / total_capital


def return_on_equity(net_income, total_shareholder_equity):
    return net_income / total_shareholder_equity


def cash_flow_to_revenue(cash_flow_from_operating_activities, total_revenue):
    return cash_flow_from_operating_activities / total_revenue


def cash_return_on_assets(cash_flow_from_operating_activities, total_assets):
    return cash_flow_from_operating_activities / total_assets


def debt_coverage_ratio(cash_flow_from_operating_activities, total_debt):
    return cash_flow_from_operating_activities / total_debt


def dividend_payment_coverage_ratio(cash_flow_from_operating_activities, dividends_paid):
    return cash_flow_from_operating_activities / dividends_paid


def investing_and_financing_coverage_ratio(cash_flow_from_operating_activities,
                                           cash_flow_from_investing_activities,
                                           cash_flow_from_financing_activities):
    return cash_flow_from_operating_activities / (cash_flow_from_investing_activities + cash_flow_from_financing_activities)


def net_tangible_asset_value(book_value, goodwill, intangible_assets):
    return book_value - goodwill - intangible_assets


def book_value(total_assets, total_liabilities):
    return total_assets - total_liabilities


# Other computed values
def cash_and_short_term_investments(marketable_securities, cash_and_cash_equivalents):
    return marketable_securities + cash_and_cash_equivalents


def total_liabilities_and_equity(total_assets):
    return total_assets


def total_liabilities(total_liabilities_and_equity, total_shareholder_equity):
    return total_liabilities_and_equity - total_shareholder_equity


# can also do total_expenses + operating_income
def total_revenue(cost_of_goods_sold, gross_profit):
    return cost_of_goods_sold + gross_profit
