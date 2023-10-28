from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    last_logged_in = models.DateTimeField()


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()


class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class AdPopup(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    time_to_send = models.DateTimeField()


class PopupGroup(models.Model):
    popup = models.ForeignKey(AdPopup, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


# The following are for targeted popups flow


class Action(models.Model):
    id = models.AutoField(primary_key=True)
    action_type = models.CharField(max_length=255)


class TargetedPopup(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    action = models.ForeignKey(Action, on_delete=models.CASCADE)


class TargetedPopupAnswer(models.Model):
    popup = models.ForeignKey(TargetedPopup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_answer_text = models.TextField()
    user_rating_stars = models.PositiveIntegerField()
