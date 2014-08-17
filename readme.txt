- create barebone django project with 2 apps, articles and galleries
- create models for those apps and migrate them
- create a foreign key from one app to another
- make migrations
- migrate latest changes - FAILURE

# stack trace

~~~
Migrations for 'galleries':
  0002_galleryitem_article.py:
    - Add field article to galleryitem
(bugtest)[amar@galaxy bugtest]$ ./manage.py migrate
Operations to perform:
  Apply all migrations: articles, sessions, auth, contenttypes, galleries, admin
Running migrations:
  Applying galleries.0002_galleryitem_article...Traceback (most recent call last):
  File "/home/amar/.virtualenvs/bugtest/lib/python3.4/site-packages/django/apps/registry.py", line 148, in get_app_config
    return self.app_configs[app_label]
KeyError: 'articles'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/amar/.virtualenvs/bugtest/lib/python3.4/site-packages/django/db/migrations/state.py", line 79, in render
    model = self.apps.get_model(lookup_model[0], lookup_model[1])
  File "/home/amar/.virtualenvs/bugtest/lib/python3.4/site-packages/django/apps/registry.py", line 202, in get_model
    return self.get_app_config(app_label).get_model(model_name.lower())
  File "/home/amar/.virtualenvs/bugtest/lib/python3.4/site-packages/django/apps/registry.py", line 150, in get_app_config
    raise LookupError("No installed app with label '%s'." % app_label)
LookupError: No installed app with label 'articles'.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "./manage.py", line 10, in <module>
    execute_from_command_line(sys.argv)
  File "/home/amar/.virtualenvs/bugtest/lib/python3.4/site-packages/django/core/management/__init__.py", line 385, in execute_from_command_line
    utility.execute()
  File "/home/amar/.virtualenvs/bugtest/lib/python3.4/site-packages/django/core/management/__init__.py", line 377, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/home/amar/.virtualenvs/bugtest/lib/python3.4/site-packages/django/core/management/base.py", line 288, in run_from_argv
    self.execute(*args, **options.__dict__)
  File "/home/amar/.virtualenvs/bugtest/lib/python3.4/site-packages/django/core/management/base.py", line 337, in execute
    output = self.handle(*args, **options)
  File "/home/amar/.virtualenvs/bugtest/lib/python3.4/site-packages/django/core/management/commands/migrate.py", line 160, in handle
    executor.migrate(targets, plan, fake=options.get("fake", False))
  File "/home/amar/.virtualenvs/bugtest/lib/python3.4/site-packages/django/db/migrations/executor.py", line 63, in migrate
    self.apply_migration(migration, fake=fake)
  File "/home/amar/.virtualenvs/bugtest/lib/python3.4/site-packages/django/db/migrations/executor.py", line 91, in apply_migration
    if self.detect_soft_applied(migration):
  File "/home/amar/.virtualenvs/bugtest/lib/python3.4/site-packages/django/db/migrations/executor.py", line 135, in detect_soft_applied
    apps = project_state.render()
  File "/home/amar/.virtualenvs/bugtest/lib/python3.4/site-packages/django/db/migrations/state.py", line 89, in render
    model=lookup_model,
ValueError: Lookup failed for model referenced by field galleries.GalleryItem.article: articles.Article
~~~
