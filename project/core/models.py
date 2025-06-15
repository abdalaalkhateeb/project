# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Attraction(models.Model):
    attraction_id = models.AutoField(db_column='Attraction_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hours_of_operation = models.CharField(db_column='Hours_Of_Operation', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                           null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Attraction'
        app_label = 'attractions'


class Booking(models.Model):
    booking_id = models.AutoField(db_column='Booking_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='User_ID', blank=True, null=True,db_constraint=False)  # Field name made lowercase.
    entity_id = models.IntegerField(db_column='Entity_ID', blank=True, null=True)  # Field name made lowercase.
    booking_type = models.CharField(db_column='Booking_Type', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    booking_date = models.DateField(db_column='Booking_Date', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    total_cost = models.DecimalField(db_column='Total_Cost', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Booking'
        app_label = 'booking'

class Chatbot(models.Model):
    chatbot_id = models.AutoField(db_column='Chatbot_ID', primary_key=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    availability = models.BooleanField(db_column='Availability', blank=True, null=True)  # Field name made lowercase.
    ai_model_type = models.CharField(db_column='AI_Model_Type', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    last_training_date = models.DateField(db_column='Last_Training_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Chatbot'


class Hotel(models.Model):
    hotel_id = models.AutoField(db_column='Hotel_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rating = models.DecimalField(db_column='Rating', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    price_range = models.CharField(db_column='Price_Range', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    contact_info = models.CharField(db_column='Contact_Info', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    available_rooms = models.IntegerField(db_column='Available_Rooms', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hotel'
        app_label = 'rooms'


class Notification(models.Model):
    notification_id = models.AutoField(db_column='Notification_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='User_ID', blank=True, null=True,db_constraint=False)  # Field name made lowercase.
    message = models.TextField(db_column='Message', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    notification_type = models.CharField(db_column='Notification_Type', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sent_date = models.DateField(db_column='Sent_Date', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Notification'


class Payment(models.Model):
    payment_id = models.AutoField(db_column='Payment_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='User_ID', blank=True, null=True,db_constraint=False)  # Field name made lowercase.
    booking = models.ForeignKey(Booking, models.DO_NOTHING, db_column='Booking_ID', blank=True, null=True)  # Field name made lowercase.
    payment_date = models.DateField(db_column='Payment_Date', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    payment_method = models.CharField(db_column='Payment_Method', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payment'
        app_label = 'booking'

class Recommendation(models.Model):
    recommendation_id = models.AutoField(db_column='Recommendation_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='User_ID', blank=True, null=True,db_constraint=False)  # Field name made lowercase.
    entity_id = models.IntegerField(db_column='Entity_ID', blank=True, null=True)  # Field name made lowercase.
    recommendation_type = models.CharField(db_column='Recommendation_Type', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recommendation'


class Restaurant(models.Model):
    restaurant_id = models.AutoField(db_column='Restaurant_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cuisine_type = models.CharField(db_column='Cuisine_Type', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rating = models.DecimalField(db_column='Rating', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    price_range = models.CharField(db_column='Price_Range', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    contact_info = models.CharField(db_column='Contact_Info', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    availability = models.BooleanField(db_column='Availability', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Restaurant'
        app_label = 'restaurant'


class Review(models.Model):
    review_id = models.AutoField(db_column='Review_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='User_ID', blank=True, null=True,db_constraint=False)  # Field name made lowercase.
    entity_id = models.IntegerField(db_column='Entity_ID', blank=True, null=True)  # Field name made lowercase.
    entity_type = models.CharField(db_column='Entity_Type', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    review_date = models.DateField(db_column='Review_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Review'


class Room(models.Model):
    room_id = models.AutoField(db_column='Room_ID', primary_key=True)  # Field name made lowercase.
    hotel = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='Hotel_ID', blank=True, null=True)  # Field name made lowercase.
    room_type = models.CharField(db_column='Room_Type', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    price_per_night = models.DecimalField(db_column='Price_Per_Night', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    availability = models.BooleanField(db_column='Availability', blank=True, null=True)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    @property
    def id(self):
        return self.room_id

    class Meta:
        managed = False
        db_table = 'Room'
        app_label = 'rooms'


class Tour(models.Model):
    tour_id = models.AutoField(db_column='Tour_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='Duration', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    available_spots = models.IntegerField(db_column='Available_Spots', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tour'


class TravelInfo(models.Model):
    info_id = models.AutoField(db_column='Info_ID', primary_key=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    transportation_options = models.TextField(db_column='Transportation_Options', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    travel_costs = models.TextField(db_column='Travel_Costs', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    travel_tips = models.TextField(db_column='Travel_Tips', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Travel_Info'


class User(models.Model):
    user_id = models.AutoField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    preferences = models.TextField(db_column='Preferences', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    @property
    def id(self):
        return self.user_id

    class Meta:
        managed = False
        db_table = 'User'
        app_label = 'accounts'


class Weather(models.Model):
    weather_id = models.AutoField(db_column='Weather_ID', primary_key=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    temperature = models.FloatField(db_column='Temperature', blank=True, null=True)  # Field name made lowercase.
    conditions = models.CharField(db_column='Conditions', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Weather'
