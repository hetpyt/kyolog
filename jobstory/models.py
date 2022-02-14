from django.db import models


class TaskHistory(models.Model):
    dev_name = models.CharField('Device', max_length=64)
    job_kind = models.CharField('Job kind', max_length=15)
    start_time = models.DateTimeField('Start time')
    end_time = models.DateTimeField('End time')
    job_number = models.PositiveIntegerField('Job number')
    job_name = models.CharField('Job name', max_length=64)
    job_result = models.CharField('Job result', max_length=15)
    job_result_detail = models.IntegerField('Job result detail')
    pages = models.PositiveSmallIntegerField('Pages')
    copies = models.PositiveSmallIntegerField('Copies', null=True)
    complete_pages = models.PositiveSmallIntegerField('Complete pages', null=True, db_column='complete_pages')
    complete_copies = models.PositiveSmallIntegerField('Complete copies', null=True, db_column='complete_copies')

    def __str__(self):
        return f'{self.dev_name} {self.job_kind} {self.start_time} {self.job_name}'

    class Meta:
        db_table = 'task_history'

