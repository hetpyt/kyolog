import re
from datetime import datetime, timedelta
from django.shortcuts import render
from django.db.models import Q
from django.core.exceptions import FieldDoesNotExist
from .models import TaskHistory
from .forms import SettingsForm


DEF_SORT_FIELD = 'id'
DEF_SORT_DIR = 'DESC'


def str_to_date(d):
    m = re.match(r'^(\d{4})-(\d{1,2})-(\d{1,2})(.{1}(\d{1,2}):(\d{1,2}):(\d{1,2}))*$', d)
    if m is None:
        raise ValueError
    g = m.groups()
    try:
        if g[3] is None:
            return datetime(int(g[0]), int(g[1]), int(g[2]))
        else:
            return datetime(int(g[0]), int(g[1]), int(g[2]), int(g[4]), int(g[5]), int(g[6]))
    except Exception:
        raise ValueError


def index(request):
    sort_direction, sort_field = DEF_SORT_DIR, DEF_SORT_FIELD
    date_from, date_to, count_min, limit = None, None, None, None
    initials = {}
    filters = []

    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            sort_field = form.cleaned_data['sort_field']
            if sort_field not in [f.name for f in TaskHistory._meta.get_fields()]:
                sort_field = DEF_SORT_FIELD
            date_from = form.cleaned_data['date_from']
            date_to = form.cleaned_data['date_to']
            sort_direction = form.cleaned_data['sort_direction']
            count_min = form.cleaned_data['count_min']

    else:
        # по умолчанию показывать задания за последний день
        now = datetime.now()
        date_from = datetime(now.year, now.month, now.day)

    initials['sort_field'] = sort_field
    initials['sort_direction'] = sort_direction

    # apply filters & sort
    if count_min is not None:
        initials['count_min'] = count_min
        filters.append(Q(pages__gte=count_min) | Q(copies__gte=count_min))
    if date_from:
        initials['date_from'] = date_from.strftime('%Y-%m-%dT%H:%M')
        filters.append(Q(start_time__gte=date_from))
    if date_to:
        initials['date_to'] = date_to.strftime('%Y-%m-%dT%H:%M')
        filters.append(Q(start_time__lte=date_to))
    sort_dir = '-' if sort_direction == "DESC" else ''
    qs = TaskHistory.objects.filter(*filters).order_by(sort_dir + sort_field)

    context = {
        'request': request,
        'form': SettingsForm(initial=initials),
        'task_list': qs,
        'meta': TaskHistory._meta,
        'sort_field': sort_field,
        'sort_dir': sort_dir,
    }
    return render(request, 'jobstory/index.html', context)



def form_test(request):
    form = SettingsForm()
    return render(request, 'jobstory/settings_form.html', {'form': form})
