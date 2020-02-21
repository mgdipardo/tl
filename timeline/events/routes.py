from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from timeline import db
from timeline.models import Event
from timeline.events.forms import EventForm

events = Blueprint('events', __name__)


@events.route("/event/new", methods=['GET', 'POST'])
@login_required
def new_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(title=form.title.data, event_date=form.event_date.data,
                      content=form.content.data, source=form.source.data, author=current_user)
        db.session.add(event)
        db.session.commit()
        flash('Your event has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_event.html', title='New Event',
                           form=form, legend='New Event')


@events.route("/event/<int:event_id>")
def event(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template('event.html', title=event.title, event=event)


@events.route("/event/<int:event_id>/update", methods=['GET', 'POST'])
@login_required
def update_event(event_id):
    event = Event.query.get_or_404(event_id)
    if event.author != current_user:
        abort(403)
    form = EventForm()
    if form.validate_on_submit():
        event.title = form.title.data
        event.event_date = form.event_date.data
        event.content = form.content.data
        event.source = form.source.data
        db.session.commit()
        flash('Your event has been updated!', 'success')
        return redirect(url_for('events.event', event_id=event.id))
    elif request.method == 'GET':
        form.title.data = event.title
        form.event_date.data = event.event_date
        form.content.data = event.content
        form.source.data = event.source
    return render_template('create_event.html', title='Update Event',
                           form=form, legend='Update Event')


@events.route("/event/<int:event_id>/delete", methods=['POST'])
@login_required
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    if event.author != current_user:
        abort(403)
    db.session.delete(event)
    db.session.commit()
    flash('Your event has been deleted!', 'success')
    return redirect(url_for('main.home'))
