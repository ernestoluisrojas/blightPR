from django.db import models
from django.contrib.auth.models import User
#from django.template.defaultfilters import slugify



class AbndSite(models.Model):
	catastro = models.CharField(max_length=128)
	lat = models.CharField(max_length=128, blank=True)
	lng = models.CharField(max_length=128, blank=True)
	dueno = models.CharField(max_length=128, blank=True)
	calle = models.CharField(max_length=128, blank=True)
	numero = models.CharField(max_length=128, blank=True)
	comunidad = models.CharField(max_length=128, blank=True)
	cabida = models.CharField(max_length=128, blank=True)
	tenencia = models.CharField(max_length=128, blank=True)
	tipo = models.CharField(max_length=128, blank=True)
	calificacion = models.CharField(max_length=128, blank=True)
	descripcion = models.CharField(max_length=128, blank=True)
	inundabilidad = models.CharField(max_length=128, blank=True)
	comentarios = models.TextField(blank=True)

	#TODO: anadir Upload picture Field
	picture = models.ImageField(upload_to='properties_images/', null='True', 
		blank=True, max_length=512, default='/static/media/properties_images/default.png')

	#Valorizacion
	v_estructura = models.CharField(max_length=128, blank=True)
	v_solar = models.CharField(max_length=128, blank=True)
	v_total = models.CharField(max_length=128, blank=True)

	def __unicode__(self):
		return self.catastro


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username

