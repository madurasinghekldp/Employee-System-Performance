from flask import Blueprint,request
from service.main_service import calculate_performance

main_bp = Blueprint('main_controller', __name__)

@main_bp.route('/calc', methods=['GET'])
def cal_performance():
    leave_count = request.args.get('leave_count', type=float)
    rejected_tasks = request.args.get('rejected_tasks', type=float)
    late_tasks = request.args.get('late_tasks', type=float)
    return calculate_performance(leave_count, rejected_tasks, late_tasks)