# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        pass
        #db.create_unique('auth_user', ['email'])
        #db.alter_column(
            #'auth_user',
            #'username',
            #models.CharField(max_length=200)
        #)

    def backwards(self, orm):
        raise RuntimeError("Cannot reverse this migration")

    models = {

    }

    complete_apps = ['commons']