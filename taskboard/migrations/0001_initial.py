# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Client'
        db.create_table('taskboard_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('taskboard', ['Client'])

        # Adding model 'Project'
        db.create_table('taskboard_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['taskboard.Client'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('taskboard', ['Project'])

        # Adding model 'Team'
        db.create_table('taskboard_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('taskboard', ['Team'])

        # Adding M2M table for field members on 'Team'
        db.create_table('taskboard_team_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm['taskboard.team'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('taskboard_team_members', ['team_id', 'user_id'])

        # Adding model 'Task'
        db.create_table('taskboard_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['taskboard.Project'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['taskboard.Team'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('effort', self.gf('django.db.models.fields.IntegerField')()),
            ('completed', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('blocked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('icebox', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('taskboard', ['Task'])

        # Adding model 'TeamStrengthAdjustment'
        db.create_table('taskboard_teamstrengthadjustment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['taskboard.Team'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('taskboard', ['TeamStrengthAdjustment'])


    def backwards(self, orm):
        
        # Deleting model 'Client'
        db.delete_table('taskboard_client')

        # Deleting model 'Project'
        db.delete_table('taskboard_project')

        # Deleting model 'Team'
        db.delete_table('taskboard_team')

        # Removing M2M table for field members on 'Team'
        db.delete_table('taskboard_team_members')

        # Deleting model 'Task'
        db.delete_table('taskboard_task')

        # Deleting model 'TeamStrengthAdjustment'
        db.delete_table('taskboard_teamstrengthadjustment')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'taskboard.client': {
            'Meta': {'ordering': "['name']", 'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'taskboard.project': {
            'Meta': {'ordering': "['client', 'name']", 'object_name': 'Project'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['taskboard.Client']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'taskboard.task': {
            'Meta': {'ordering': "['-completed', 'priority']", 'object_name': 'Task'},
            'blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'completed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'effort': ('django.db.models.fields.IntegerField', [], {}),
            'icebox': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['taskboard.Project']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['taskboard.Team']"})
        },
        'taskboard.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'taskboard.teamstrengthadjustment': {
            'Meta': {'object_name': 'TeamStrengthAdjustment'},
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['taskboard.Team']"})
        }
    }

    complete_apps = ['taskboard']
