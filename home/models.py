# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Diccionario(models.Model):
    dic_key = models.AutoField(primary_key=True)
    dic_palabra = models.CharField(max_length=50, blank=True, null=True)
    dic_definicion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Diccionario'


class Lectura(models.Model):
    lec_key = models.FloatField()
    lec_fecha = models.CharField(max_length=255, blank=True, null=True)
    lec_am_libro = models.IntegerField(blank=True, null=True)
    lec_am_cap_start = models.IntegerField(blank=True, null=True)
    lec_am_cap_end = models.IntegerField(blank=True, null=True)
    lec_am_vers_start = models.IntegerField(blank=True, null=True)
    lec_am_vers_end = models.IntegerField(blank=True, null=True)
    lec_pm_libro = models.IntegerField(blank=True, null=True)
    lec_pm_cap_start = models.IntegerField(blank=True, null=True)
    lec_pm_cap_end = models.IntegerField(blank=True, null=True)
    lec_pm_vers_start = models.IntegerField(blank=True, null=True)
    lec_pm_vers_end = models.IntegerField(blank=True, null=True)
    lec_am_start = models.IntegerField(blank=True, null=True)
    lec_am_end = models.IntegerField(blank=True, null=True)
    lec_pm_start = models.IntegerField(blank=True, null=True)
    lec_pm_end = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Lectura'


class Usuarios(models.Model):
    user_key = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    user_password = models.TextField(blank=True, null=True)
    user_nombre = models.CharField(max_length=50, blank=True, null=True)
    user_apellido = models.CharField(max_length=50, blank=True, null=True)
    user_email = models.CharField(max_length=50, blank=True, null=True)
    user_fk_cia_key = models.IntegerField(blank=True, null=True)
    user_role = models.IntegerField(blank=True, null=True)
    user_address = models.CharField(max_length=50, blank=True, null=True)
    user_llave = models.TextField(blank=True, null=True)
    user_celular = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Usuarios'


class Anuncios(models.Model):
    an_key = models.AutoField(primary_key=True)
    an_title = models.CharField(max_length=50, blank=True, null=True)
    an_date = models.CharField(max_length=50, blank=True, null=True)
    an_remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'anuncios'
 
 

 

class Displayverso(models.Model):
    dv_key = models.AutoField(primary_key=True)
    dv_verso = models.IntegerField()
    dv_nro = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'displayVerso'


 
 

 
class EstudioVersos(models.Model):
    ve_key = models.AutoField(primary_key=True)
    ve_fk_e_id_key = models.IntegerField(blank=True, null=True)
    ve_fk_v_idversiculo = models.IntegerField(db_column='ve_fk_V_IdVersiculo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'estudio_versos'


class Eventos(models.Model):
    eve_key = models.AutoField(primary_key=True)
    eve_title = models.CharField(max_length=50, blank=True, null=True)
    eve_date = models.CharField(max_length=50, blank=True, null=True)
    eve_remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'eventos'


class Lcapitulos(models.Model):
    c_idcapitulo = models.IntegerField(db_column='C_IdCapitulo', primary_key=True)  # Field name made lowercase.
    c_capitulo_desc = models.IntegerField(db_column='C_Capitulo_Desc', blank=True, null=True)  # Field name made lowercase.
    c_idlibro = models.ForeignKey('Llibros', models.DO_NOTHING, db_column='C_IdLibro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'lCapitulos'


class Lestudios(models.Model):
    e_id_key = models.AutoField(primary_key=True)
    e_estudio = models.CharField(max_length=200, blank=True, null=True)
    e_http = models.CharField(max_length=200, blank=True, null=True)
    e_fk_id_cat = models.IntegerField(blank=True, null=True)
    e_remarks = models.CharField(max_length=200, blank=True, null=True)
    e_short_url = models.CharField(max_length=10, blank=True, null=True)
    e_flag_activo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lEstudios'


class Llibros(models.Model):
    l_idlibro = models.IntegerField(db_column='L_IdLibro', primary_key=True)  # Field name made lowercase.
    l_libro_desc = models.CharField(db_column='L_Libro_Desc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    l_link = models.CharField(db_column='L_link', max_length=200, blank=True, null=True)  # Field name made lowercase.
    l_link2 = models.CharField(db_column='L_link2', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'lLibros'


class LpaCara(models.Model):
    ca_key = models.AutoField(primary_key=True)
    ca_fk_pa_key = models.IntegerField(blank=True, null=True)
    ca_verso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lPa_cara'


class LpaSello(models.Model):
    se_key = models.AutoField(primary_key=True)
    se_fk_pa_key = models.IntegerField(blank=True, null=True)
    se_verso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lPa_sello'


class Lparadojas(models.Model):
    pa_key = models.AutoField(primary_key=True)
    pa_titulo_cara = models.TextField(blank=True, null=True)
    pa_titulo_sello = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lParadojas'


class Ltema(models.Model):
    t_id_key = models.AutoField(db_column='T_id_key', primary_key=True)  # Field name made lowercase.
    t_titulo = models.CharField(db_column='T_titulo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    t_id_verso_start = models.IntegerField(db_column='T_id_verso_start', blank=True, null=True)  # Field name made lowercase.
    t_id_verso_end = models.IntegerField(db_column='T_id_verso_end', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'lTema'


class Lversiculos(models.Model):
    v_idversiculo = models.IntegerField(db_column='V_IdVersiculo', primary_key=True)  # Field name made lowercase.
    v_contenido = models.TextField(db_column='V_Contenido', blank=True, null=True)  # Field name made lowercase.
    v_idcapitulo = models.ForeignKey(Lcapitulos, models.DO_NOTHING, db_column='V_IdCapitulo', blank=True, null=True)  # Field name made lowercase.
    v_versiculo = models.IntegerField(db_column='V_versiculo', blank=True, null=True)  # Field name made lowercase.
    v_lbla = models.TextField(db_column='V_LBLA', blank=True, null=True)  # Field name made lowercase.
    v_nas = models.TextField(db_column='V_NAS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'lVersiculos'


class RndVersos(models.Model):
    rv_key = models.AutoField(primary_key=True)
    rv_fk_v_idversiculo = models.IntegerField(db_column='rv_fk_V_IdVersiculo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'rnd_Versos'
