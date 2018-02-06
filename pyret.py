# pyret module - basic python functions for retail application
#
#   ---------------------------------------------------------------------------
#
#   list of functions: 
#
#   ---------------------------------------------------------------------------
#
#   function margin(cost, retail, units=[]):
#      'Calculates % margin based on cost and retail. Calculares weighted % margin based on cost, retail, unit sales.'
#    
#   function markup(cost, retail, units=[]):
#      'Calculates % markup based on cost and retail. Calculares weighted % markup based on cost, retail, unit sales.'
#    
#   function newret_mrgn(cost, margin):
#      'Calculates new retail based on cost and target % margin.'
#    
#   function newret_mkup(cost, markup):
#      'Calculates new retail based on cost and target % markup.'
#    
#   function cost_mrgn(retail, margin):
#      'Calculates cost based on retail and % margin.'
#    
#   function cost_mkup(retail, markup):
#      'Calculates cost based on retail and % markup.'
#    
#   function change_newret(old_retail, new_retail):
#      'Calculates retail % change based on current retail and target (new) retail.'
#    
#   function newret_change(retail, change):
#      'Calculates new retail based on current retail and % change.'
#    
#   function priceindex(base_retail, retail, units=[]):
#      'Calculates Price Index for retail versus base_retail. Calculates weighted Price Index for retails versus base_retails based on unit sales.'
#    
#   function retail_units_corr(retail, units):
#      'Calculates correlation coefficient between price and unit sold.'
#    
#   function elast_arc(old_volume, new_volume, old_retail, new_retail):
#      'Calculates arc price elasticity of demand based on old volume, new volume, old retail, new retail.'
#    
#   function elast_pt(old_volume, new_volume, old_retail, new_retail):
#      'Calculates point price elasticity of demand based on old volume, new volume, old retail, new retail.'
#    
#   function elast(retail, units, segment_begin, segment_end):
#      'Calculates coefficient and intercept for linear regression model.'
#    
#   function opt_retail(retail, units, elast_coef, range=0.1):
#      'Calculates opimal retails (max dollar sales) based on current retails, unit sales, elastisity.'
#    
#   function breakeven_ret(cost, retail, discount):
#      'Calculates % break even based on cost, retail and % discount.'
#    
#   function breakeven_mkup(markup, discount):
#      'Calculates % break even based on % markup and % discount.'
#    
#   function breakeven_mrgn(margin, discount):
#      'Calculates % break even based on % margin and % discount.'
#    
#   function retail_distr(retail, precision=1):
#      'Creates and show retails distribution.'
#    
#   function show_depend(retail, units):
#      'Creates and show price/units dependency scatter.'
#    
#   function smart_round(retail, temp='*.**', align='fair'):
#      'Smart rounding: number of decimals, ending digits.'
#
#   ---------------------------------------------------------------------------
#
#   functions descriptions: 
# 
#   ---------------------------------------------------------------------------
#
#   function margin(cost, retail, units=[])
#
#       Calculates % margin based on cost and retail. Calculares weighted % margin based on cost, retail, unit sales.
#
#       Arguments: 
#
#           cost - scalar value, list, ndarray, pd.Series or pd.DataFrame with cost(s) in int or float format
#           retail - scalar value, list, ndarray, pd.Series or pd.DataFrame with retail(s) in int or float format
#           units - list, ndarray, pd.Series or pd.DataFrame with units sold in int or float format, length of units should be equal to the length of cost and retail
#
#       Returns:
#
#           % margin as float,
#           list, ndarray, pd.Series, pd.DataFrame of % margins as floats
#           weighted % margin as float
#
#       Samples:
#
#           >>> margin(2.35, 4.70)
#           out: 0.5
#
#           >>> margin(4.36, 5.45)
#           out: 0.19999999999999996
#
#           >>> margin([2.35, 4.36], [4.70, 5.45], units=[100, 300])
#           out: 0.2669833729216152
#
#   ---------------------------------------------------------------------------
#
#   function markup(cost, retail, units=[]) 
#           
#       Calculates % markup based on cost and retail. Calculares weighted % markup based on cost, retail, unit sales.
#
#       Arguments:
#
#           cost - scalar value, list, ndarray, pd.Series or pd.DataFrame with cost(s) in int or float format
#           retail - scalar value, list, ndarray, pd.Series or pd.DataFrame with retail(s) in int or float format
#           units - list, ndarray, pd.Series or pd.DataFrame with units sold in int or float format, length of units should be equal to the length of cost and retail
#
#       Returns:
#
#           % markup as float,
#           list, ndarray, pd.Series, pd.DataFrame of % markups as floats
#           weighted % markup as float
#
#       Samples:
#
#           >>> markup(2.35, 4.70)
#           out: 1.0
#
#           >>> markup(4.36, 5.45)
#           out: 0.24999999999999994
#
#           >>> markup([2.35, 4.36], [4.70, 5.45], units=[100, 300])
#           out: 0.3642255346727155
#
#   ---------------------------------------------------------------------------
#
#   function newret_mrgn(cost, markup):
#       
#       Calculates new retail based on cost and target % margin.
#
#       Arguments:
#
#           cost - scalar value, list, ndarray, pd.Series or pd.DataFrame with cost(s) in int or float format
#           markup - scalar value, list, ndarray, pd.Series or pd.DataFrame with % markup(s) in int or float format
#
#       Returns:
#
#           new retail as float,
#           list, ndarray, pd.Series, pd.DataFrame of new retails as floats
#
#       Samples:
#
#           >>> newret_mrgn(2.35, 0.5)
#           out: 4.7
#
#           >>> newret_mrgn([2.35, 4.36], [0.50, 0.20])
#           out: [4.7, 5.45]
#
#   ---------------------------------------------------------------------------
#
#   function newret_mkup(cost, markup):
#       
#       Calculates new retail based on cost and target % markup.
#
#       Arguments:
#
#           cost - scalar value, list, ndarray, pd.Series or pd.DataFrame with cost(s) in int or float format
#           markup - scalar value, list, ndarray, pd.Series or pd.DataFrame with % markup(s) in int or float format
#
#       Returns:
#
#           new retail as float,
#           list, ndarray, pd.Series, pd.DataFrame of new retails as floats
#
#       Samples:
#
#           >>> newret_mkup(2.35, 1.0)
#           out: 4.7
#
#           >>> newret_mkup([2.35, 4.36], [1.00, 0.25])
#           out: [4.7, 5.45]
#
#   ---------------------------------------------------------------------------
#
#   function cost_mrgn(retail, margin):
#    
#       Calculates cost based on retail and % margin.
#
#       Arguments:
#
#           retail - scalar value, list, ndarray, pd.Series or pd.DataFrame with retail(s) in int or float format
#           margin - scalar value, list, ndarray, pd.Series or pd.DataFrame with % margin(s) in int or float format
#
#       Returns:
#
#           cost as float,
#           list, ndarray, pd.Series, pd.DataFrame of costs as floats
#
#       Samples:
#
#           >>> cost_mrgn(4.00, 0.5)
#           out: 2.0
#
#           >>> cost_mrgn([4.00, 4.00], [0.50, 0.25])
#           out: [2.0, 3.0]
#
#   ---------------------------------------------------------------------------
#
#   function cost_mkup(retail, markup):
#    
#       Calculates cost based on retail and % markup.
#
#       Arguments:
#
#           retail - scalar value, list, ndarray, pd.Series or pd.DataFrame with retail(s) in int or float format
#           markup - scalar value, list, ndarray, pd.Series or pd.DataFrame with % markup(s) in int or float format
#
#       Returns:
#
#           cost as float,
#           list, ndarray, pd.Series, pd.DataFrame of costs as floats
#
#       Samples:
#
#           >>> cost_mkup(4.00, 1.0)
#           out: 2.0
#
#           >>> cost_mkup([4.00, 4.00], [1.00, 0.33])
#           out: [2.0, 3.007518796992481]
#
#   ---------------------------------------------------------------------------
#
#   function change_newret(old_retail, new_retail):
#
#       Calculates % change based on current retail and target (new) retail.
#
#       Arguments:
#
#           old_retail - scalar value, list, ndarray, pd.Series or pd.DataFrame with old (current) retail(s) in int or float format
#           new_retail - scalar value, list, ndarray, pd.Series or pd.DataFrame with new (target) retail(s) in int or float format
#
#       Returns:
#
#           % change as float,
#           list, ndarray, pd.Series, pd.DataFrame of % changes as floats
#
#       Samples:
#
#           >>> change_newret(2.49, 2.99)
#           out: 0.2008032128514056
#
#           >>> change_newret([2.49, 4.36], [2.99, 4.79])
#           out: [0.2008032128514056, 0.0986238532110091]
#
#   ---------------------------------------------------------------------------
#
#   function newret_change(retail, change):
#
#       Calculates new retail based on current retail and % change.
#
#       Arguments:
#
#           retail - scalar value, list, ndarray, pd.Series or pd.DataFrame with old (current) retail(s) in int or float format
#           change - scalar value, list, ndarray, pd.Series or pd.DataFrame with % change(s) in int or float format
#
#       Returns:
#
#           new retail as float,
#           list, ndarray, pd.Series, pd.DataFrame of new retails as floats
#
#       Samples:
#
#           >>> newret_change(2.49, 0.20)
#           out: 2.988
#
#           >>> change_newret([2.49, 4.70], [0.2, -0.10])
#           out: [2.988, 4.23]
#
#   ---------------------------------------------------------------------------
#
#   function priceindex(base_retail, retail, units=[]):
#
#       Calculates Price Index for retail versus base_retail. Calculates weighted Price Index for retails versus base_retails based on unit sales.
#
#       Arguments:
#
#           base_retail - scalar value, list, ndarray, pd.Series or pd.DataFrame with retails used as a base in int or float format
#           retail - scalar value, list, ndarray, pd.Series or pd.DataFrame with retail(s) in int or float format
#           units - list, ndarray, pd.Series or pd.DataFrame with units sold in int or float format, length of units should be equal to the length of base_retail and retail
#
#       Returns:
#
#           priceindex as float,
#           list, ndarray, pd.Series, pd.DataFrame of priceindexes as floats
#           weighted priceindex as float
#
#       Samples:
#
#           >>> priceindex(2.49, 2.99)
#           out: 1.2008032128514057
#
#           >>> priceindex([2.49, 3.29], [2.99, 2.99])
#           out: [1.2008032128514057, 0.9088145896656535]
#
#           >>> priceindex([2.49, 3.29], [2.99, 2.99], units=[100, 300])
#           out: 0.9676375404530745
#
#   ---------------------------------------------------------------------------
#
#   function retail_units_corr(retail, units):
#
#       Calculates correlation coefficient between price and unit sold.
#
#       Arguments:
#
#           retail - list, ndarray, pd.Series or pd.DataFrame with retails in int or float format
#           units - list, ndarray, pd.Series or pd.DataFrame with unit sales in int or float format
#
#       Returns:
#
#           correlation coefficient as float
#
#       Samples:
#
#           >>> retail_units_corr([1.99, 2.49, 2.99, 3.99], [50, 40, 30, 20])
#           out: -0.98270762982399062
#
#   ---------------------------------------------------------------------------
#
#   function elast_arc(old_unit, new_unit, old_retail, new_retail):
#
#       Calculates arc price elasticity of demand based on old unit sales, new unit sales, old retail, new retail.
#
#       Arguments:
#
#           old_unit - scalar value, list, ndarray, pd.Series or pd.DataFrame with old (current) unit sales in int or float format
#           new_unit - scalar value, list, ndarray, pd.Series or pd.DataFrame with new unit sales in int or float format
#           old_retail - scalar value, list, ndarray, pd.Series or pd.DataFrame with old (current) retail(s) in int or float format
#           new_retail - scalar value, list, ndarray, pd.Series or pd.DataFrame with new retail(s) in int or float format
#
#       Returns:
#
#           arc elastisity on demand as float or
#           list, ndarray, pd.Series, pd.DataFrame of arc elastisities on demand as floats
#
#       Samples:
#
#           >>> elast_arc(20, 30, 2.49, 2.29)
#           out: -4.779999999999996
#
#           >>> elast_arc([20, 40], [30, 30],[2.49, 3.99],[2.29, 4.49])
#           out: [-4.779999999999996, -2.422857142857143]
#
#   ---------------------------------------------------------------------------
#
#   function elast_pt(old_unit, new_unit, old_retail, new_retail):
#
#       Calculates point price elasticity of demand based on old unit sales, new unit sales, old retail, new retail.
#
#       Arguments:
#
#           old_unit - scalar value, list, ndarray, pd.Series or pd.DataFrame with old (current) unit sales in int or float format
#           new_unit - scalar value, list, ndarray, pd.Series or pd.DataFrame with new unit sales in int or float format
#           old_retail - scalar value, list, ndarray, pd.Series or pd.DataFrame with old (current) retail(s) in int or float format
#           new_retail - scalar value, list, ndarray, pd.Series or pd.DataFrame with new retail(s) in int or float format
#
#       Returns:
#
#           point elastisity on demand as float or
#           list, ndarray, pd.Series, pd.DataFrame of point elastisities on demand as floats
#
#       Samples:
#
#           >>> elast_pt(20, 30, 2.49, 2.29)
#           out: -6.224999999999995
#
#           >>> elast_pt([20, 40], [30, 30],[2.49, 3.99],[2.29, 4.49])
#           out: [-6.224999999999995, -1.9950000000000003]
#
#   ---------------------------------------------------------------------------
#
#   function elast(retail, units, segment_begin=0, segment_end=0):
#
#       Calculates coefficient and intercept for linear regression model in the segment.
#
#       Arguments:
#
#           retail - scalar value, list, ndarray, pd.Series or pd.DataFrame with retails in int or float format
#           units - scalar value, list, ndarray, pd.Series or pd.DataFrame with unit sales in int or float format
#           segment_begin - scalar value with beginning point of price segment in int or float format (if segment_begin == 0 then segment_begin = min(retail))
#           segment_end - scalar value with ending point of price segment in int or float format (if segment_end == 0 then segment_end = max(retail))
#
#       Returns:
#
#           tuple contains:
#           - regression coefficient
#           - regression intercept
#           - R^2
#           - F-statistic
#           - DW-statistic
#
#       Samples:
#
#           >>> elast([2.49, 2.99, 3.99], [40, 30, 20])
#           out: (-12.857142857142856,
#                 70.585714285714289,
#                 0.9642857142857143,
#                 27.000000000000014,
#                 2.9285714285714284)
#
#           >>> elast([1.99, 2.49, 2.99, 3.99], [50, 40, 30, 20], segment_begin=2.49)
#           out: (-12.857142857142856,
#                 70.585714285714289,
#                 0.9642857142857143,
#                 27.000000000000014,
#                 2.9285714285714284)
#
#   ---------------------------------------------------------------------------
# 
#   function opt_retail(retail, units, elast_coef, range=0.1):
#
#       Calculates opimal (max dollar sales) retails based on current retails, unit sales, elastisity.
#
#       Arguments:
#
#           retail - scalar value, list, ndarray, pd.Series or pd.DataFrame with retails in int or float format
#           units - scalar value, list, ndarray, pd.Series or pd.DataFrame with unit sales in int or float format
#           elast_coef - scalar value, list, ndarray, pd.Series or pd.DataFrame with elasticity coefficients in int or float format
#           range - scalar value, list, ndarray, pd.Series or pd.DataFrame with % range of possible retail change in int or float format
#
#       Returns:
#
#           retails that deliver maximum $ sales in float format
#
#       Samples:
#
#           >>> opt_retail([2.5], [50], [-.5], range=0.1)
#           out: array([ 2.74])
#
#   ---------------------------------------------------------------------------
# 
#   function breakeven_ret(cost, retail, discount):
#
#       Calculates % break even based on cost, retail and % discount.
#
#       Arguments:
#
#           cost - scalar value, list, ndarray, pd.Series or pd.DataFrame with costs in int or float format
#           retail - scalar value, list, ndarray, pd.Series or pd.DataFrame with retails in int or float format
#           discount - scalar value, list, ndarray, pd.Series or pd.DataFrame with % discount in int or float format
#
#       Returns:
#
#           scalar value, list, ndarray, pd.Series or pd.DataFrame (depends on input) with % of unit sales increase required to retain $ margin
#
#       Samples:
#
#           >>> breakeven_ret(1.00, 2.00, .25)
#           out: 1.0
#
#   ---------------------------------------------------------------------------
#   
#   function breakeven_mkup(markup, discount):
#
#       Calculates % break even based on % markup and % discount.
#
#       Arguments:
#
#           markup - scalar value, list, ndarray, pd.Series or pd.DataFrame with % markup in int or float format
#           discount - scalar value, list, ndarray, pd.Series or pd.DataFrame with % discount in int or float format
#
#       Returns:
#
#           scalar value, list, ndarray, pd.Series or pd.DataFrame (depends on input) with % of unit sales increase required to retain $ margin
#
#       Samples:
#
#           >>> breakeven_mkup(.20, .10)
#           out: 2.499999999999998
#
#   ---------------------------------------------------------------------------
#  
#   function breakeven_mrgn(margin, discount):
#
#       Calculates % break even based on % margin and % discount.
#
#       Arguments:
#
#           margin - scalar value, list, ndarray, pd.Series or pd.DataFrame with % margin in int or float format
#           discount - scalar value, list, ndarray, pd.Series or pd.DataFrame with % discount in int or float format
#
#       Returns:
#
#           scalar value, list, ndarray, pd.Series or pd.DataFrame (depends on input) with % of unit sales increase required to retain $ margin
#
#       Samples:
#
#           >>> breakeven_mrgn(.20, .10)
#           out: 1.0
#
#   ---------------------------------------------------------------------------
#    
#   function retail_distr(retail, precision=1):
#
#       Creates and show retails distribution.
#
#       Arguments:
#
#           retail - list, ndarray, pd.Series or pd.DataFrame with retails in int or float format
#           precision - scalar value with the size of bin
#
#       Returns:
#
#           histogram with prices divided into bins
#
#   ---------------------------------------------------------------------------
#    
#   function show_depend(retail, units):
#
#       Creates and show price/units dependency scatter.
#
#       Arguments:
#
#           retail - list, ndarray, pd.Series or pd.DataFrame with retails in int or float format
#           units - list, ndarray, pd.Series or pd.DataFrame with units in int or float format
#
#       Returns:
#
#           scatter with retail prices on the x axis and units sold on the y axis
#
#   ---------------------------------------------------------------------------
#   
#   function smart_round(retail, temp='*.**', align='fair'):
#
#       Smart rounding: number of decimals, ending digits.
#
#       Arguments:
#
#           retail - list, ndarray, pd.Series or pd.DataFrame with retails in int or float format
#           temp - template that describes amount of decimals and ending digits
#           align - general approach to the alignment in case of ending digits, options available: 'down', 'fair', 'up'
#
#       Returns:
#
#           ndarray with rounded retails
#
#       Samples:
#
#           >>> smart_round([12.567, 3.421])
#           out: array([ 12.57,   3.42])
#
#           >>> smart_round([12.456], temp='*.*9')
#           out: array([ 12.49])
#
#           >>> smart_round([12.567, 3.40], temp='*.95', align='down')
#           out: array([ 11.95,   2.95])
#
#           >>> smart_round([12.567, 3.40], temp='*.95', align='up')
#           out: array([ 12.95,   3.95])
#
#   ---------------------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# calculates % margin based on cost and retail
def margin(cost, retail, units=[]):
    'Calculates % margin based on cost and retail. Calculares weighted % margin based on cost, retail, unit sales.'
    if len(units) != 0:
        if (isinstance(cost, list) and isinstance(retail, list) and isinstance(units, list)):
            if len(cost) == len (retail) and len(cost) == len(units):
                t_list_1 = [retail[i] * units[i] for i in range(len(cost))]
                t_list_2 = [cost[i] * units[i] for i in range(len(cost))]
                t_list = (sum(t_list_1) - sum(t_list_2)) / sum(t_list_1)
                return float(t_list)
            else:
                print('Cost, retail and units lists should have the same length.')
        elif (isinstance(cost, pd.core.series.Series) or isinstance(cost, pd.core.frame.DataFrame)) and (isinstance(retail, pd.core.series.Series) or isinstance(retail, pd.core.frame.DataFrame)) and (isinstance(units, pd.core.series.Series) or isinstance(units, pd.core.frame.DataFrame)):
            t_var = ((units * retail).sum() - (units * cost).sum()) / (units * retail).sum()
            return float(t_var)
        elif (isinstance(cost, np.ndarray) and isinstance(retail, np.ndarray) and isinstance(units, np.ndarray)):
            t_var = ((units * retail).sum() - (units * cost).sum()) / (units * retail).sum()
            return float(t_var)
        elif (isinstance(cost,int) or isinstance(cost,float)) and (isinstance(retail,int) or isinstance(retail,float)):
            t_var = (retail - cost) / retail
            return float(t_var)
        else:
            print('Unsupported data type or combination of data types.')
    else:
        if type(cost) == list and type(retail) == list:
            t_list = [(retail[i] - cost[i]) / retail[i] for i in range(len(cost))]
            return t_list
        else:
            t_var = (retail - cost) / retail
            return t_var

# calculates % markup based on cost and retail
def markup(cost, retail, units=[]):
    'Calculates % markup based on cost and retail. Calculares weighted % markup based on cost, retail, unit sales.'
    if len(units) != 0:
        if (isinstance(cost, list) and isinstance(retail, list) and isinstance(units, list)):
            if len(cost) == len (retail) and len(cost) == len(units):
                t_list_1 = [retail[i] * units[i] for i in range(len(cost))]
                t_list_2 = [cost[i] * units[i] for i in range(len(cost))]
                t_list = (sum(t_list_1) - sum(t_list_2)) / sum(t_list_2)
                return float(t_list)
            else:
                print('Cost, retail and units lists should have the same length.')
        elif (isinstance(cost, pd.core.series.Series) or isinstance(cost, pd.core.frame.DataFrame)) and (isinstance(retail, pd.core.series.Series) or isinstance(retail, pd.core.frame.DataFrame)) and (isinstance(units, pd.core.series.Series) or isinstance(units, pd.core.frame.DataFrame)):
            t_var = ((units * retail).sum() - (units * cost).sum()) / (units * cost).sum()
            return float(t_var)
        elif (isinstance(cost, np.ndarray) and isinstance(retail, np.ndarray) and isinstance(units, np.ndarray)):
            t_var = ((units * retail).sum() - (units * cost).sum()) / (units * cost).sum()
            return float(t_var)
        elif (isinstance(cost,int) or isinstance(cost,float)) and (isinstance(retail,int) or isinstance(retail,float)):
            t_var = (retail - cost) / cost
            return float(t_var)
        else:
            print('Unsupported data type or combination of data types.')
    else:
        if type(cost) == list and type(retail) == list:
            t_list = [(retail[i] - cost[i]) / cost[i] for i in range(len(cost))]
            return t_list
        else:
            t_var = (retail - cost) / cost
            return t_var

# calculates new retail based on target % margin
def newret_mrgn(cost, margin):
    'Calculates new retail based on cost and target % margin.'
    if type(cost) == list and type(margin) == list:
        t_list = [cost[i] / (1 - margin[i]) for i in range(len(cost))] 
        return t_list    
    else:
        t_var = cost / (1 - margin)
        return t_var
    
# calculates new retail based on cost and target % markup
def newret_mkup(cost, markup):
    'Calculates new retail based on cost and target % markup.'
    if type(cost) == list and type(markup) == list:
        t_list = [cost[i] * (1 + markup[i]) for i in range(len(cost))] 
        return t_list  
    else:
        t_var = cost * (1 + markup)
        return t_var
    
# Calculates cost based on retail and % margin.
def cost_mrgn(retail, margin):
    'Calculates cost based on retail and % margin.'
    if isinstance(retail, list) and isinstance(margin, list):
        t_list = [retail[i] * (1 - margin[i]) for i in range(len(retail))] 
        return t_list   
    else:
        t_var = retail * (1 - margin)
        return t_var
        
# Calculates cost based on retail and % markup.
def cost_mkup(retail, markup):
    'Calculates cost based on retail and % markup.'
    if isinstance(retail, list) and isinstance(markup, list):
        t_list = [retail[i] / (1 + markup[i]) for i in range(len(retail))] 
        return t_list   
    else:
        t_var = retail / (1 + markup)
        return t_var
    
# calculates % change based on current retail and target (new) retail
def change_newret(old_retail, new_retail):
    'Calculates retail % change based on current retail and target (new) retail.'
    if type(old_retail) == list and type(new_retail) == list:
        t_list = [(new_retail[i] - old_retail[i]) / old_retail[i] for i in range(len(old_retail))]
        return t_list
    else:
        t_var = (new_retail - old_retail) / old_retail
        return t_var
    
# calculates new retail based on current retail and % change
def newret_change(retail, change):
    'Calculates new retail based on current retail and % change.'
    if type(retail) == list and type(change) == list:
        t_list = [retail[i] * (1 + change[i]) for i in range(len(retail))] 
        return t_list   
    else:
        t_var = retail * (1 + change)
        return t_var

# calculates price index and weighted price index
def priceindex(base_retail, retail, units=[]):
    'Calculates Price Index for retail versus base_retail. Calculates weighted Price Index for retails versus base_retails based on unit sales.'
    if len(units) != 0:
        if (isinstance(base_retail, list) and isinstance(retail, list) and isinstance(units, list)):
            if len(base_retail) == len (retail) and len(base_retail) == len(units):
                t_list_1 = [retail[i] * units[i] for i in range(len(retail))]
                t_list_2 = [base_retail[i] * units[i] for i in range(len(base_retail))]
                t_list = sum(t_list_1) / sum(t_list_2)
                return float(t_list)
            else:
                print('Cost, retail and units lists should have the same length.')
        elif (isinstance(base_retail, pd.core.series.Series) or isinstance(base_retail, pd.core.frame.DataFrame)) and (isinstance(retail, pd.core.series.Series) or isinstance(retail, pd.core.frame.DataFrame)) and (isinstance(units, pd.core.series.Series) or isinstance(units, pd.core.frame.DataFrame)):
            t_var = (units * retail).sum() / (units * base_retail).sum()
            return float(t_var)
        elif (isinstance(base_retail, np.ndarray) and isinstance(retail, np.ndarray) and isinstance(units, np.ndarray)):
            t_var = (units * retail).sum() / (units * base_retail).sum()
            return float(t_var)
        elif (isinstance(base_retail,int) or isinstance(base_retail,float)) and (isinstance(retail,int) or isinstance(retail,float)):
            t_var = retail / base_retail
            return float(t_var)
        else:
            print('Unsupported data type or combination of data types.')
    else:
        if type(base_retail) == list and type(retail) == list:
            t_list = [retail[i] / base_retail[i] for i in range(len(retail))]
            return t_list
        else:
            t_var = retail / base_retail
            return t_var
    
# calculates correlation between price and unit sold
def retail_units_corr(retail, units):
    'Calculates correlation coefficient between price and unit sold.'
    t_retail = np.array(retail).flatten()
    t_units = np.array(units).flatten()
    return np.corrcoef(t_retail, t_units)[0][1]
     
# calculates arc price elasticity of demand based on old volume, new volume, old retail, new retail
def elast_arc(old_volume, new_volume, old_retail, new_retail):
    'Calculates arc price elasticity of demand based on old volume, new volume, old retail, new retail.'
    if type(old_volume) == list and type(new_volume) == list and type(old_retail) == list and type(new_retail) == list:
        t_list = [((new_volume[i] - old_volume[i]) / (new_retail[i] - old_retail[i])) * (((new_retail[i] + old_retail[i]) / 2) / ((new_volume[i] + old_volume[i]) / 2)) for i in range(len(old_volume))]
        return t_list
    else:
        t_var = ((new_volume - old_volume) / (new_retail - old_retail)) * (((new_retail + old_retail) / 2) / ((new_volume + old_volume) / 2))
        return t_var      

# calculates point price elasticity of demand based on old volume, new volume, old retail, new retail
def elast_pt(old_volume, new_volume, old_retail, new_retail):
    'Calculates point price elasticity of demand based on old volume, new volume, old retail, new retail.'
    if type(old_volume) == list and type(new_volume) == list and type(old_retail) == list and type(new_retail) == list:
        t_list = [((new_volume[i] - old_volume[i]) * old_retail[i]) / ((new_retail[i] - old_retail[i]) * old_volume[i]) for i in range(len(old_volume))]
        return t_list
    else:
        t_var = ((new_volume - old_volume) * old_retail) / ((new_retail - old_retail) * old_volume)
        return t_var

# linear regression in the segment
def elast(retail, units, segment_begin=0, segment_end=0):
    'Calculates coefficient and intercept for linear regression model in the segment.'

    def F_test(r_sq, obs_num, param_num):
        return (r_sq / (1 - r_sq)) * ((obs_num - param_num - 1) / param_num)
    
    def Durbin_Watson_stat(t_resid):
        t_len = t_resid.size
        t_sum = 0
        t_et = 0
        for i in range(t_len):
            if i > 0: t_sum = t_sum + (t_resid[i] - t_resid[i - 1])**2
            t_et = t_et + t_resid[i]**2
        # return test value
        return t_sum / t_et

    t_retail = np.array(retail)
    t_units = np.array(units)

    if segment_begin == 0: segment_begin = t_retail.min()
    if segment_end == 0: segment_end = t_retail.max()
    
    t_units = t_units[(t_retail >= segment_begin)&(t_retail <= segment_end)]
    t_retail = t_retail[(t_retail >= segment_begin)&(t_retail <= segment_end)]
    
    t_retail = t_retail.reshape(-1, 1)
    t_units = t_units.flatten()
    
    t_clf = linear_model.LinearRegression()
    t_clf.fit(t_retail, t_units)
    
    t_r_sq = t_clf.score(t_retail,t_units)
    t_F_test = F_test(t_r_sq, t_retail.size, 1)
    t_predict = t_clf.predict(t_retail)
    t_residuals = (t_units - t_predict)
    t_DW_test = Durbin_Watson_stat(t_residuals)
    
    return (t_clf.coef_[0], t_clf.intercept_, t_r_sq, t_F_test, t_DW_test)

# calculates optimal retails
def opt_retail(retail, units, elast_coef, range=0.1):
    'Calculates opimal retails (max dollar sales) based on current retails, unit sales, elastisity.'
    
    t_retail = np.array(retail)
    t_units = np.array(units)
    t_elast_coef = np.array(elast_coef)
    
    t_opt_retails = []
    
    t_min_ret = t_retail * (1 - range)
    t_max_ret = t_retail * (1 + range)
    
    for i in np.arange(t_retail.size):
        t_max_mar = 0
        t_opt_retail = 0
        for j in np.arange(t_min_ret[i], t_max_ret[i], 0.01):
            if t_max_mar < j * (t_units[i] + t_units[i] * (t_elast_coef[i] * (j / t_retail[i] - 1))):
                t_max_mar = j * (t_units[i] + t_units[i] * (t_elast_coef[i] * (j / t_retail[i] - 1)))
                t_opt_retail = j
        t_opt_retails.append(t_opt_retail)
        
    return np.array(t_opt_retails)

# calculates % break even based on cost, retail and % discount
def breakeven_ret(cost, retail, discount):
    'Calculates % break even based on cost, retail and % discount.'
    if type(cost) == list and type(retail) == list and type(discount) == list:
        t_list = [(retail[i] - cost[i]) / (retail[i] * (1 - discount[i]) - cost[i]) - 1 for i in range(len(cost))]
        return t_list
    else:
        t_var = (retail - cost) / (retail * (1 - discount) - cost) - 1
        return t_var

# calculates % break even based on % markup and % discount
def breakeven_mkup(markup, discount):
    'Calculates % break even based on % markup and % discount.'
    if type(markup) == list and type(discount) == list:
        t_list = [markup[i] / ((1 + markup[i]) * (1 - discount[i]) - 1) for i in range(len(markup))]  
        return t_list  
    else:
        t_var = markup / ((1 + markup) * (1 - discount) - 1)
        return t_var
    
# calculates % break even based on % margin and % discount
def breakeven_mrgn(margin, discount):
    'Calculates % break even based on % margin and % discount.'
    if type(margin) == list and type(discount) == list:
        t_list = [1 / (1 - discount[i] / margin[i]) - 1 for i in range(len(margin))] 
        return t_list  
    else:
        t_var = 1 / (1 - discount / margin) - 1
        return t_var

# creates and show retails distribution
def retail_distr(retail, precision=1):
    'Creates and show retails distribution.'
    t_retail = np.array(retail).flatten()
    t_min = t_retail.min()
    t_max = t_retail.max()
    
    plt.title('Retails Distribution.')
    plt.xlabel('retail price segment')
    plt.ylabel('nunmber of cases')
    plt.grid(True)
    t_xticks = [i for i in np.arange(t_min - (t_min % precision), t_max + precision, precision)]
    plt.xticks(t_xticks)
    plt.hist(t_retail, bins=t_xticks, rwidth=0.8)
    plt.show()

# creates and show price/units dependency scatter
def show_depend(retail, units):
    'Creates and show price/units dependency scatter.'
    plt.title('Retails/Units Dependency.')
    plt.xlabel('retail price')
    plt.ylabel('units sold')
    plt.grid(True)
    plt.scatter(retail, units)
    plt.show()

# smart rounding: number of decimals, ending digits
def smart_round(retail, temp='*.**', align='fair'):
    'Smart rounding: number of decimals, ending digits.'
    
    # counts number of digits in a number 
    def d_num(t_did):     
        t_d_n = 1       
        while t_did >= 10: 
            t_did = t_did / 10
            t_d_n = t_d_n + 1
        return t_d_n
    
    t_retail = np.array(retail)
    
    try:
        t_dot_ind = temp.index('.')
    except:
        t_dot_ind = -1
    
    t_case = 1
    if any(i.isdigit() for i in temp): t_case = 2
    if any(i == '(' or i == ')' for i in temp): t_case = 3
    
    if t_case == 1:
        
        if t_dot_ind != -1:
            t_dec = (len(temp) - 1) - t_dot_ind
        else:
            t_dec = 0
        
        t_retail = t_retail * (10 ** t_dec) + 0.5
        t_retail_int = t_retail.astype(int).copy()
        t_retail = t_retail_int.astype(float).copy()
        t_retail = t_retail / (10 ** t_dec)
        
        return t_retail
        
    elif t_case == 2:
        
        if t_dot_ind != -1:
            t_dec = (len(temp) - 1) - t_dot_ind
        else:
            t_dec = 0
            
        t_retail = t_retail * (10 ** t_dec) + 0.5
        t_retail_int = t_retail.astype(int).copy()
        
        d_temp = float(temp.replace('*','0')) * (10 ** t_dec)
        
        t_new_retail = np.array(0)
        
        for i in t_retail_int:
            
            t_low_bound = i - (i % 10 ** (d_num(d_temp))) - 10 ** d_num(d_temp) + d_temp
            if t_low_bound <= 0: t_low_bound = t_low_bound + 10 ** d_num(d_temp)
            t_upper_bound = i - (i % 10 ** (d_num(d_temp))) + d_temp
            
            if align == 'down': t_new_retail = np.append(t_new_retail, t_low_bound)                
            elif align == 'up': t_new_retail = np.append(t_new_retail, t_upper_bound)
            elif align == 'fair':
                
                if np.abs(i - t_low_bound) > np.abs(i - t_upper_bound): t_new_retail = np.append(t_new_retail, t_upper_bound) 
                else: t_new_retail = np.append(t_new_retail, t_low_bound)             
                     
        t_retail = t_new_retail[1:].astype(float).copy()
        t_retail = t_retail / (10 ** t_dec)
        
        return t_retail