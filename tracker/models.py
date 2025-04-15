from django.db import models

class MonthlyPerformance(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()

    revenue_target = models.FloatField()
    revenue_sales = models.FloatField()
    revenue_ratio = models.FloatField()

    cost_cost = models.FloatField()
    cost_goods = models.FloatField()
    cost_outsourcing = models.FloatField()

    sgna = models.FloatField()

    op_target = models.FloatField()
    op_operating_profit = models.FloatField()
    op_ratio = models.FloatField()
    op_margin = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
