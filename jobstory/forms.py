from django import forms
from .models import TaskHistory

TASK_HISTORY_FIELDS_CHOICES = [(field.name, field.verbose_name) for field in TaskHistory._meta.get_fields()]
BS_SELECT = forms.Select(attrs={
    'class': 'form-select',
})
BS_DATE_INPUT = forms.DateTimeInput(attrs={
    'type': 'datetime-local',
    'class': 'form-control',
})
BS_NUMBER_INPUT = forms.NumberInput(attrs={
    'class': 'form-control',
})


class SettingsForm(forms.Form):
    sort_field = forms.ChoiceField(label='Sort field', widget=BS_SELECT, choices=TASK_HISTORY_FIELDS_CHOICES)
    sort_direction = forms.ChoiceField(
        label='Sort direction',
        widget=BS_SELECT,
        choices=[('ASC', 'ASC'), ('DESC', 'DESC')])
    date_from = forms.DateTimeField(label="From date", widget=BS_DATE_INPUT, required=False)
    date_to = forms.DateTimeField(label='To date', widget=BS_DATE_INPUT, required=False)
    count_min = forms.IntegerField(label='Min count', widget=BS_NUMBER_INPUT, required=False, min_value=0)

    def as_bs_form(self):
        return self._html_output(
            normal_row='%(html_class_attr)s %(label)s %(field)s%(help_text)s',
            error_row='%s',
            row_ender='',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )