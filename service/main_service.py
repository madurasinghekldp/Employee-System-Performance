import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def calculate_performance(leave, rejected, late):
    # Define fuzzy input variables
    leave_count = ctrl.Antecedent(np.arange(0, 11, 0.5), 'leave_count')
    rejected_tasks = ctrl.Antecedent(np.arange(0, 11, 1), 'rejected_tasks')
    late_tasks = ctrl.Antecedent(np.arange(0, 11, 1), 'late_tasks')

    # Define fuzzy output variable
    performance = ctrl.Consequent(np.arange(0, 11, 1), 'performance')

    # Auto-membership functions
    leave_count['low'] = fuzz.trimf(leave_count.universe, [0, 0, 4])
    leave_count['average'] = fuzz.trimf(leave_count.universe, [2, 5, 8])
    leave_count['high'] = fuzz.trimf(leave_count.universe, [6, 10, 10])

    rejected_tasks['low'] = fuzz.trimf(rejected_tasks.universe, [0, 0, 4])
    rejected_tasks['average'] = fuzz.trimf(rejected_tasks.universe, [2, 5, 8])
    rejected_tasks['high'] = fuzz.trimf(rejected_tasks.universe, [6, 10, 10])

    late_tasks['low'] = fuzz.trimf(late_tasks.universe, [0, 0, 4])
    late_tasks['average'] = fuzz.trimf(late_tasks.universe, [2, 5, 8])
    late_tasks['high'] = fuzz.trimf(late_tasks.universe, [6, 10, 10])

    performance['low'] = fuzz.trimf(performance.universe, [0, 0, 4])
    performance['average'] = fuzz.trimf(performance.universe, [2, 5, 8])
    performance['high'] = fuzz.trimf(performance.universe, [6, 10, 10])

    rules = [
    ctrl.Rule(leave_count['low'] & rejected_tasks['low'] & late_tasks['low'], performance['high']),
    ctrl.Rule(leave_count['low'] & rejected_tasks['low'] & late_tasks['average'], performance['average']),
    ctrl.Rule(leave_count['low'] & rejected_tasks['low'] & late_tasks['high'], performance['average']),
    ctrl.Rule(leave_count['low'] & rejected_tasks['average'] & late_tasks['low'], performance['high']),
    ctrl.Rule(leave_count['low'] & rejected_tasks['average'] & late_tasks['average'], performance['average']),
    ctrl.Rule(leave_count['low'] & rejected_tasks['average'] & late_tasks['high'], performance['low']),
    ctrl.Rule(leave_count['low'] & rejected_tasks['high'] & late_tasks['low'], performance['average']),
    ctrl.Rule(leave_count['low'] & rejected_tasks['high'] & late_tasks['average'], performance['average']),
    ctrl.Rule(leave_count['low'] & rejected_tasks['high'] & late_tasks['high'], performance['low']),
    ctrl.Rule(leave_count['average'] & rejected_tasks['low'] & late_tasks['low'], performance['high']),
    ctrl.Rule(leave_count['average'] & rejected_tasks['low'] & late_tasks['average'], performance['average']),
    ctrl.Rule(leave_count['average'] & rejected_tasks['low'] & late_tasks['high'], performance['low']),
    ctrl.Rule(leave_count['average'] & rejected_tasks['average'] & late_tasks['low'], performance['average']),
    ctrl.Rule(leave_count['average'] & rejected_tasks['average'] & late_tasks['average'], performance['average']),
    ctrl.Rule(leave_count['average'] & rejected_tasks['average'] & late_tasks['high'], performance['low']),
    ctrl.Rule(leave_count['average'] & rejected_tasks['high'] & late_tasks['low'], performance['average']),
    ctrl.Rule(leave_count['average'] & rejected_tasks['high'] & late_tasks['average'], performance['low']),
    ctrl.Rule(leave_count['average'] & rejected_tasks['high'] & late_tasks['high'], performance['low']),
    ctrl.Rule(leave_count['high'] & rejected_tasks['low'] & late_tasks['low'], performance['average']),
    ctrl.Rule(leave_count['high'] & rejected_tasks['low'] & late_tasks['average'], performance['low']),
    ctrl.Rule(leave_count['high'] & rejected_tasks['low'] & late_tasks['high'], performance['low']),
    ctrl.Rule(leave_count['high'] & rejected_tasks['average'] & late_tasks['low'], performance['average']),
    ctrl.Rule(leave_count['high'] & rejected_tasks['average'] & late_tasks['average'], performance['low']),
    ctrl.Rule(leave_count['high'] & rejected_tasks['average'] & late_tasks['high'], performance['low']),
    ctrl.Rule(leave_count['high'] & rejected_tasks['high'] & late_tasks['low'], performance['low']),
    ctrl.Rule(leave_count['high'] & rejected_tasks['high'] & late_tasks['average'], performance['low']),
    ctrl.Rule(leave_count['high'] & rejected_tasks['high'] & late_tasks['high'], performance['low'])
    ]

    # Create control system
    performance_ctrl = ctrl.ControlSystem(rules)
    performance_calc = ctrl.ControlSystemSimulation(performance_ctrl)

    # Input values
    performance_calc.input['leave_count'] = leave
    performance_calc.input['rejected_tasks'] = rejected
    performance_calc.input['late_tasks'] = late

    # Calculate output
    performance_calc.compute()
    performance_out = performance_calc.output['performance']
    performance_mf = performance.terms

    low_mf = performance_mf['low'].mf
    average_mf = performance_mf['average'].mf
    high_mf = performance_mf['high'].mf
    
    low_value = fuzz.interp_membership(performance.universe, low_mf, performance_out)
    avg_value = fuzz.interp_membership(performance.universe, average_mf, performance_out)
    high_value = fuzz.interp_membership(performance.universe, high_mf, performance_out)


    print(f"Predicted Performance: {performance_out}")
    return {'performance':performance_out,'low_value':low_value,'avg_value':avg_value,'high_value':high_value}
