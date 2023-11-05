from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Service, User
from website import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    all_services = Service.query.join(User).all()
    return render_template("home.html", user=current_user, services=all_services)


@views.route('/postService', methods=['GET', 'POST'])
@login_required
def post_service():
    if request.method == 'POST':
        service_name = request.form.get('service_name')
        service_detail = request.form.get('service_detail')
        service_price = float(request.form.get('service_price'))

        if len(service_name) not in range(3, 51):
            flash('Service name must have between 3 and 50 characters.', category='error')
        elif len(service_detail) not in range(1, 5001):  # => de modificat
            flash('Service detail must have between 30 and 5000 characters.', category='error')
        elif 0 > service_price > 999999.99:
            flash('Price must be between 0 and 999999.99.', category='error')
        else:
            new_service = Service(service_name=service_name, service_detail=service_detail, service_price=service_price,
                                  user_id=current_user.id)
            db.session.add(new_service)
            db.session.commit()
            flash('Service added.', category='success')
    return render_template("postService.html", user=current_user)


@views.route('/delete-service', methods=['POST'])
def delete_service():
    service = json.loads(request.data)
    serviceId = service['serviceId']
    service = Service.query.get(serviceId)
    if service:
        if service.user_id == current_user.id:
            db.session.delete(service)
            db.session.commit()

    return jsonify({})








