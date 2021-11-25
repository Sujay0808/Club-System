from django.db import models

# Create your models here.
class Club(models.Model):
    member_PRN = models.IntegerField(primary_key=True)
    club_name = models.CharField(max_length=20)
    member_name = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.club_name}'

class Workshop(models.Model):
    workshop_id = models.IntegerField(primary_key=True)
    workshop_name = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    venue = models.CharField(max_length=20)
    resource_person = models.CharField(max_length=20)
    total_seat = models.IntegerField()
    registration_fee = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.workshop_name}'

class Carnival(models.Model):
    game_id = models.CharField(primary_key=True, max_length=20)
    game_name = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    venue = models.CharField(max_length=20)
    participation_fee = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.game_name}'

class Participant(models.Model):
    candidate_PRN = models.CharField(max_length=20, primary_key=True)
    candidate_name = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    department_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.candidate_name}'

class Guest_Lecture(models.Model):
    lecture_id = models.CharField(max_length=20, primary_key=True)
    resource_person = models.CharField(max_length=20)
    topic_name = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    venue = models.CharField(max_length=20)
    time = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.topic_name}'

class Attend(models.Model):
    member_PRN = models.ForeignKey(Club, on_delete=models.CASCADE)
    workshop_id = models.ForeignKey(Workshop, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.member_PRN} attends {self.workshop_id}'

class Coordinate(models.Model):
    member_PRN = models.ForeignKey(Club, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Carnival, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.member_PRN} coordinates {self.game_id}'

class Arrange(models.Model):
    member_PRN = models.ForeignKey(Club, on_delete=models.CASCADE)
    lecture_id = models.ForeignKey(Guest_Lecture, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.member_PRN} arranges {self.lecture_id}'

class Participation1(models.Model):
    workshop_id = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    candidate_PRN = models.ForeignKey(Participant, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.candidate_PRN} participates in workshop {self.workshop_id}'

class Participation2(models.Model):
    game_id = models.ForeignKey(Carnival, on_delete=models.CASCADE)
    candidate_PRN = models.ForeignKey(Participant, on_delete=models.CASCADE)
    is_winner = models.BooleanField(default=False)
    price = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.candidate_PRN} participates in carnival {self.game_id}'

class Participation3(models.Model):
    candidate_PRN = models.ForeignKey(Participant, on_delete=models.CASCADE)
    lecture_id = models.ForeignKey(Guest_Lecture, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.candidate_PRN} participates in lecture {self.lecture_id}'