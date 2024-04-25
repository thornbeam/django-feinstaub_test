from django.db import models
from django.conf import settings
import os
class bme280(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    pressure = models.FloatField(null=True, blank=True)
#
    altitude = models.FloatField(null=True, blank=True)
#
    pressure_sealevel = models.FloatField(null=True, blank=True)
#
    temperature = models.FloatField(null=True, blank=True)
#
    humidity = models.FloatField(null=True, blank=True)
class bmp180(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    pressure = models.FloatField(null=True, blank=True)
#
    altitude = models.FloatField(null=True, blank=True)
#
    pressure_sealevel = models.FloatField(null=True, blank=True)
#
    temperature = models.FloatField(null=True, blank=True)
class bmp280(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    pressure = models.FloatField(null=True, blank=True)
#
    altitude = models.FloatField(null=True, blank=True)
#
    pressure_sealevel = models.FloatField(null=True, blank=True)
#
    temperature = models.FloatField(null=True, blank=True)
class dht22(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    temperature = models.FloatField(null=True, blank=True)
#
    humidity = models.FloatField(null=True, blank=True)
class ds18b20(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    temperature = models.FloatField(null=True, blank=True)
class hpm(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    P1 = models.FloatField(null=True, blank=True)
#
    P2 = models.FloatField(null=True, blank=True)
class htu21d(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    temperature = models.FloatField(null=True, blank=True)
#
    humidity = models.FloatField(null=True, blank=True)
class laerm(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    noise_LAeq = models.FloatField(null=True, blank=True)
#
    noise_LA_min = models.FloatField(null=True, blank=True)
#
    noise_LA_max = models.FloatField(null=True, blank=True)
#
    noise_LA01 = models.FloatField(null=True, blank=True)
#
    noise_LA95 = models.FloatField(null=True, blank=True)
class nextpm(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    P1 = models.FloatField(null=True, blank=True)
#
    P2 = models.FloatField(null=True, blank=True)
#
    P0 = models.FloatField(null=True, blank=True)
#
    N1 = models.FloatField(null=True, blank=True)
#
    N25 = models.FloatField(null=True, blank=True)
#
    N10 = models.FloatField(null=True, blank=True)
class pms1003(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    P1 = models.FloatField(null=True, blank=True)
#
    P2 = models.FloatField(null=True, blank=True)
#
    P0 = models.FloatField(null=True, blank=True)
class pms3003(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    P1 = models.FloatField(null=True, blank=True)
#
    P2 = models.FloatField(null=True, blank=True)
#
    P0 = models.FloatField(null=True, blank=True)
class pms5003(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    P1 = models.FloatField(null=True, blank=True)
#
    P2 = models.FloatField(null=True, blank=True)
#
    P0 = models.FloatField(null=True, blank=True)
class pms6003(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    P1 = models.FloatField(null=True, blank=True)
#
    P2 = models.FloatField(null=True, blank=True)
#
    P0 = models.FloatField(null=True, blank=True)
class pms7003(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    P1 = models.FloatField(null=True, blank=True)
#
    P2 = models.FloatField(null=True, blank=True)
#
    P0 = models.FloatField(null=True, blank=True)
class ppd42ns(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    P1 = models.FloatField(null=True, blank=True)
#
    durP1 = models.FloatField(null=True, blank=True)
#
    ratioP1 = models.FloatField(null=True, blank=True)
#
    P2 = models.FloatField(null=True, blank=True)
#
    durP2 = models.FloatField(null=True, blank=True)
#
    ratioP2 = models.FloatField(null=True, blank=True)
class radiation_sbm19(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    counts_per_minute = models.FloatField(null=True, blank=True)
#
    hv_pulses = models.FloatField(null=True, blank=True)
#
    tube = models.FloatField(null=True, blank=True)
#
    counts = models.FloatField(null=True, blank=True)
#
    sample_time_ms = models.FloatField(null=True, blank=True)
class radiation_sbm20(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    counts_per_minute = models.FloatField(null=True, blank=True)
#
    hv_pulses = models.FloatField(null=True, blank=True)
#
    tube = models.FloatField(null=True, blank=True)
#
    counts = models.FloatField(null=True, blank=True)
#
    sample_time_ms = models.FloatField(null=True, blank=True)
class radiation_si22g(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    counts_per_minute = models.FloatField(null=True, blank=True)
#
    hv_pulses = models.FloatField(null=True, blank=True)
#
    tube = models.FloatField(null=True, blank=True)
#
    counts = models.FloatField(null=True, blank=True)
#
    sample_time_ms = models.FloatField(null=True, blank=True)
class scd30(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    temperature = models.FloatField(null=True, blank=True)
#
    humidity = models.FloatField(null=True, blank=True)
#
    co2_ppm = models.FloatField(null=True, blank=True)
class sds011(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    P1 = models.FloatField(null=True, blank=True)
#
    durP1 = models.FloatField(null=True, blank=True)
#
    ratioP1 = models.FloatField(null=True, blank=True)
#
    P2 = models.FloatField(null=True, blank=True)
#
    durP2 = models.FloatField(null=True, blank=True)
#
    ratioP2 = models.FloatField(null=True, blank=True)
class sht11(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    temperature = models.FloatField(null=True, blank=True)
#
    humidity = models.FloatField(null=True, blank=True)
class sht15(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    temperature = models.FloatField(null=True, blank=True)
#
    humidity = models.FloatField(null=True, blank=True)
class sht30(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    temperature = models.FloatField(null=True, blank=True)
#
    humidity = models.FloatField(null=True, blank=True)
class sht31(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    temperature = models.FloatField(null=True, blank=True)
#
    humidity = models.FloatField(null=True, blank=True)
class sht35(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    temperature = models.FloatField(null=True, blank=True)
#
    humidity = models.FloatField(null=True, blank=True)
class sht85(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    temperature = models.FloatField(null=True, blank=True)
#
    humidity = models.FloatField(null=True, blank=True)
class sps30(models.Model):
#
    sensor_id = models.IntegerField(null=True, blank=True)
#
    sensor_type = models.CharField(max_length=255, blank=True)
#
    location = models.IntegerField(null=True, blank=True)
#
    lat = models.FloatField(null=True, blank=True)
#
    lon = models.FloatField(null=True, blank=True)
#
    timestamp = models.DateTimeField(null=True, blank=True)
#
    P1 = models.FloatField(null=True, blank=True)
#
    P4 = models.FloatField(null=True, blank=True)
#
    P2 = models.FloatField(null=True, blank=True)
#
    P0 = models.FloatField(null=True, blank=True)
#
    N10 = models.FloatField(null=True, blank=True)
#
    N4 = models.FloatField(null=True, blank=True)
#
    N25 = models.FloatField(null=True, blank=True)
#
    N1 = models.FloatField(null=True, blank=True)
#
    N05 = models.FloatField(null=True, blank=True)
#
    TS = models.FloatField(null=True, blank=True)
