from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User
from .import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'] )
def home():
    return render_template("home.html")


@views.route('/browse', methods = ['GET', 'POST'])
@login_required
def browse():
    return render_template('dashboard.html', user=current_user)