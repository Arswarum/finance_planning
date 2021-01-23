from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
# from month.models import MonthField
# Create your models here.


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)  # Change to month
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    budget = models.IntegerField()

    # def __str__(self):
    #     return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def budget_left(self):
        expense_list = Expense.objects.filter(project=self)
        total_expense_amount = 0
        for expense in expense_list:
            total_expense_amount += expense.amount
        return int(self.budget - total_expense_amount)

    def total_transactions(self):
        expense_list = Expense.objects.filter(project=self)
        total_expense_amount = 0
        for expense in expense_list:
            total_expense_amount += expense.amount
        return f'{len(expense_list)} -  ${int(total_expense_amount)}'

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Category(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    # def __str__(self):
    #     return self.name


class Expense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-amount',)
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'

    # def __str__(self):
    #     return self.title
