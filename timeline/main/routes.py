from flask import render_template, request, Blueprint
from timeline.models import Event

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    events = Event.query.order_by(Event.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', events=events)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
