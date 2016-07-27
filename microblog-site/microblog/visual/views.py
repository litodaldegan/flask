from flask import (
	Blueprint, render_template, session
)

visual_blueprint = Blueprint('visual', __name__, static_folder='./static', template_folder='./templates')

@visual_blueprint.route('/energyJobs')
def energyJobs():
	if 'username' in session:
		return render_template('energyJobs.html',
								user=session['username'])

	return render_template('energyJobs.html')

@visual_blueprint.route('/energyJobsStacked')
def energyJobsStacked():
	if 'username' in session:
		return render_template('energyJobsStacked.html',
								user=session['username'])

	return render_template('energyJobsStacked.html')