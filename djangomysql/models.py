# coding=utf-8
from django.db import models

# Create your models here.


class TimePoint(models.Model):
    """
        start_time : 表示时间段的开始时间
        end_time   : 表示时间段的结束时间
        type       : 表示时间段内活动类型
        note       : 时间段活动注释
    """
    type = models.SmallIntegerField()
    note = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # 返回该时间段所花费的时间
    @property
    def spend_time(self):
        return self.end_time - self.start_time
