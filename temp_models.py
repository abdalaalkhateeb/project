# This is an auto-generated Django model module.

# You'll have to do the following manually to clean this up:

#   * Rearrange models' order

#   * Make sure each model has one field with primary_key=True

#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior

#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table

# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models





class AuthGroup(models.Model):

    name = models.CharField(unique=True, max_length=150)



    class Meta:

        managed = False

        db_table = 'auth_group'





class AuthGroupPermissions(models.Model):

    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)



    class Meta:

        managed = False

        db_table = 'auth_group_permissions'

        unique_together = (('group', 'permission'),)





class AuthPermission(models.Model):

    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)

    codename = models.CharField(max_length=100)

    name = models.CharField(max_length=255)



    class Meta:

        managed = False

        db_table = 'auth_permission'

        unique_together = (('content_type', 'codename'),)





class AuthUser(models.Model):

    password = models.CharField(max_length=128)

    last_login = models.DateTimeField(blank=True, null=True)

    is_superuser = models.BooleanField()

    username = models.CharField(unique=True, max_length=150)

    last_name = models.CharField(max_length=150)

    email = models.CharField(max_length=254)

    is_staff = models.BooleanField()

    is_active = models.BooleanField()

    date_joined = models.DateTimeField()

    first_name = models.CharField(max_length=150)



    class Meta:

        managed = False

        db_table = 'auth_user'





class AuthUserGroups(models.Model):

    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)



    class Meta:

        managed = False

        db_table = 'auth_user_groups'

        unique_together = (('user', 'group'),)





class AuthUserUserPermissions(models.Model):

    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)



    class Meta:

        managed = False

        db_table = 'auth_user_user_permissions'

        unique_together = (('user', 'permission'),)





class CoreAttraction(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField()

    location = models.CharField(max_length=100)

    entry_fee = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float



    class Meta:

        managed = False

        db_table = 'core_attraction'





class CoreHotel(models.Model):

    name = models.CharField(max_length=100)

    location = models.CharField(max_length=100)

    rating = models.FloatField()

    description = models.TextField()

    amenities = models.TextField()



    class Meta:

        managed = False

        db_table = 'core_hotel'





class CoreRestaurant(models.Model):

    name = models.CharField(max_length=100)

    location = models.CharField(max_length=100)

    cuisine = models.CharField(max_length=100)

    rating = models.FloatField()



    class Meta:

        managed = False

        db_table = 'core_restaurant'





class CoreReview(models.Model):

    entity_type = models.CharField(max_length=50)

    entity_id = models.IntegerField()

    rating = models.FloatField()

    comment = models.TextField()

    review_date = models.DateField()



    class Meta:

        managed = False

        db_table = 'core_review'





class CoreTour(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField()

    location = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    duration = models.IntegerField()



    class Meta:

        managed = False

        db_table = 'core_tour'





class DjangoAdminLog(models.Model):

    object_id = models.TextField(blank=True, null=True)

    object_repr = models.CharField(max_length=200)

    action_flag = models.PositiveSmallIntegerField()

    change_message = models.TextField()

    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)

    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    action_time = models.DateTimeField()



    class Meta:

        managed = False

        db_table = 'django_admin_log'





class DjangoContentType(models.Model):

    app_label = models.CharField(max_length=100)

    model = models.CharField(max_length=100)



    class Meta:

        managed = False

        db_table = 'django_content_type'

        unique_together = (('app_label', 'model'),)





class DjangoMigrations(models.Model):

    app = models.CharField(max_length=255)

    name = models.CharField(max_length=255)

    applied = models.DateTimeField()



    class Meta:

        managed = False

        db_table = 'django_migrations'





class DjangoSession(models.Model):

    session_key = models.CharField(primary_key=True, max_length=40)

    session_data = models.TextField()

    expire_date = models.DateTimeField()



    class Meta:

        managed = False

        db_table = 'django_session'





class HomeHerosection(models.Model):

    title = models.CharField(max_length=255)

    subtitle = models.CharField(max_length=255)

    description = models.TextField()

    background_image = models.CharField(max_length=100)



    class Meta:

        managed = False

        db_table = 'home_herosection'


