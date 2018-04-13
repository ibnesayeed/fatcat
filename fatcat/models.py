
"""
states for identifiers:
- pre-live: points to a rev (during edit/accept period)
- live: points to a rev
- redirect: live, points to upstream rev, also points to redirect id
    => if live and redirect non-null, all other fields copied from redirect target
- deleted: live, but doesn't point to a rev

possible refactors:
- '_rev' instead of '_revision'
"""

from fatcat import db

# TODO: EntityMixin, EntityIdMixin

class WorkContrib(db.Model):
    __tablename__ = "work_contrib"
    work_rev= db.Column(db.ForeignKey('work_revision.id'), nullable=False, primary_key=True)
    creator_ident_id = db.Column(db.ForeignKey('creator_ident.id'), nullable=False, primary_key=True)
    type = db.Column(db.String, nullable=True)
    stub = db.Column(db.String, nullable=True)

    creator = db.relationship("CreatorIdent")
    work = db.relationship("WorkRevision")

class ReleaseContrib(db.Model):
    __tablename__ = "release_contrib"
    release_rev = db.Column(db.ForeignKey('release_revision.id'), nullable=False, primary_key=True)
    creator_ident_id = db.Column(db.ForeignKey('creator_ident.id'), nullable=False, primary_key=True)
    type = db.Column(db.String, nullable=True)
    stub = db.Column(db.String, nullable=True)

    creator = db.relationship("CreatorIdent")
    release = db.relationship("ReleaseRevision")

class ReleaseRef(db.Model):
    __tablename__ = "release_ref"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    release_rev = db.Column(db.ForeignKey('release_revision.id'), nullable=False)
    target_release_ident_id = db.Column(db.ForeignKey('release_ident.id'), nullable=True)
    index = db.Column(db.Integer, nullable=True)
    stub = db.Column(db.String, nullable=True)
    doi = db.Column(db.String, nullable=True)

    release = db.relationship("ReleaseRevision")
    target = db.relationship("ReleaseIdent")

class FileRelease(db.Model):
    __tablename__ = "file_release"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    file_rev= db.Column(db.ForeignKey('file_revision.id'), nullable=False)
    release_ident_id = db.Column(db.ForeignKey('release_ident.id'), nullable=False)

    release = db.relationship("ReleaseIdent")
    file = db.relationship("FileRevision")

class WorkIdent(db.Model):
    """
    If revision_id is null, this was deleted.
    If redirect_id is not null, this has been merged with the given id. In this
        case revision_id is a "cached" copy of the redirect's revision_id, as
        an optimization. If the merged work is "deleted", revision_id can be
        null and redirect_id not-null.
    """
    __tablename__ = 'work_ident'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    live = db.Column(db.Boolean, nullable=False, default=False)
    revision_id = db.Column(db.ForeignKey('work_revision.id'), nullable=True)
    redirect_id = db.Column(db.ForeignKey('work_ident.id'), nullable=True)
    revision = db.relationship("WorkRevision")

class WorkLog(db.Model):
    __tablename__ = 'work_log'
    # ID is a monotonic int here; important for ordering!
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    work_ident_id = db.Column(db.ForeignKey('work_ident.id'), nullable=False)
    #old_revision_id = db.Column(db.ForeignKey('work_revision.id'), nullable=True)
    #old_redirect_id = db.Column(db.ForeignKey('work_ident.id'), nullable=True)
    new_revision_id = db.Column(db.ForeignKey('work_revision.id'), nullable=True)
    new_redirect_id = db.Column(db.ForeignKey('work_ident.id'), nullable=True)
    # TODO: is this right?
    edit_id = db.Column(db.ForeignKey('edit.id'))

class WorkEdit(db.Model):
    __tablename__ = 'work_edit'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ident_id = db.Column(db.ForeignKey('work_ident.id'), nullable=True)
    revision_id = db.Column(db.ForeignKey('work_revision.id'), nullable=True)
    redirect_id = db.Column(db.ForeignKey('work_ident.id'), nullable=True)
    edit_group = db.Column(db.ForeignKey('edit_group.id'), nullable=True)
    editor = db.Column(db.ForeignKey('editor.id'), nullable=False)
    comment = db.Column(db.String, nullable=True)
    extra_json = db.Column(db.ForeignKey('extra_json.sha1'), nullable=True)

class WorkRevision(db.Model):
    __tablename__ = 'work_revision'
    id = db.Column(db.Integer, primary_key=True)
    edit_id = db.Column(db.ForeignKey('edit.id'))
    extra_json = db.Column(db.ForeignKey('extra_json.sha1'), nullable=True)

    title = db.Column(db.String)
    work_type = db.Column(db.String)
    primary_release_id = db.Column(db.ForeignKey('release_ident.id'), nullable=True)

    creators = db.relationship('WorkContrib', lazy='subquery',
        backref=db.backref('works', lazy=True))

class ReleaseIdent(db.Model):
    __tablename__ = 'release_ident'
    id = db.Column(db.Integer, primary_key=True)
    live = db.Column(db.Boolean, nullable=False, default=False)
    revision_id = db.Column(db.ForeignKey('release_revision.id'))
    redirect_id = db.Column(db.ForeignKey('release_ident.id'), nullable=True)
    revision = db.relationship("ReleaseRevision")

class ReleaseRevision(db.Model):
    __tablename__ = 'release_revision'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    edit_id = db.Column(db.ForeignKey('edit.id'))
    extra_json = db.Column(db.ForeignKey('extra_json.sha1'), nullable=True)

    work_ident_id = db.ForeignKey('work_ident.id')
    container_ident_id = db.Column(db.ForeignKey('container_ident.id'), nullable=True)
    title = db.Column(db.String, nullable=False)
    license = db.Column(db.String, nullable=True)   # TODO: oa status foreign key
    release_type = db.Column(db.String)             # TODO: foreign key
    date = db.Column(db.String, nullable=True)      # TODO: datetime
    doi = db.Column(db.String, nullable=True)       # TODO: identifier table
    volume = db.Column(db.String, nullable=True)
    pages = db.Column(db.String, nullable=True)
    issue = db.Column(db.String, nullable=True)

    #work = db.relationship("WorkIdent", lazy='subquery')
    container = db.relationship("ContainerIdent", lazy='subquery')
    creators = db.relationship('ReleaseContrib', lazy='subquery')
    refs = db.relationship('ReleaseRef', lazy='subquery')

class CreatorIdent(db.Model):
    __tablename__ = 'creator_ident'
    id = db.Column(db.Integer, primary_key=True)
    live = db.Column(db.Boolean, nullable=False, default=False)
    revision_id = db.Column(db.ForeignKey('creator_revision.id'))
    redirect_id = db.Column(db.ForeignKey('creator_ident.id'), nullable=True)
    revision = db.relationship("CreatorRevision")

class CreatorRevision(db.Model):
    __tablename__ = 'creator_revision'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    edit_id = db.Column(db.ForeignKey('edit.id'))
    extra_json = db.Column(db.ForeignKey('extra_json.sha1'), nullable=True)
    #creator_ids = db.relationship("CreatorIdent", backref="revision", lazy=False)

    name = db.Column(db.String)
    sortname = db.Column(db.String)
    orcid = db.Column(db.String)            # TODO: identifier table

class ContainerIdent(db.Model):
    __tablename__ = 'container_ident'
    id = db.Column(db.Integer, primary_key=True)
    live = db.Column(db.Boolean, nullable=False, default=False)
    revision_id = db.Column(db.ForeignKey('container_revision.id'))
    redirect_id = db.Column(db.ForeignKey('container_ident.id'), nullable=True)
    revision = db.relationship("ContainerRevision")

class ContainerRevision(db.Model):
    __tablename__ = 'container_revision'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    edit_id = db.Column(db.ForeignKey('edit.id'))
    extra_json = db.Column(db.ForeignKey('extra_json.sha1'), nullable=True)

    name = db.Column(db.String)
    #XXX: container_ident_id = db.Column(db.ForeignKey('container_ident.id'))
    publisher = db.Column(db.String)        # TODO: foreign key
    sortname = db.Column(db.String)
    issn = db.Column(db.String)             # TODO: identifier table

class FileIdent(db.Model):
    __tablename__ = 'file_ident'
    id = db.Column(db.Integer, primary_key=True)
    live = db.Column(db.Boolean, nullable=False, default=False)
    revision_id = db.Column('revision', db.ForeignKey('file_revision.id'))
    redirect_id = db.Column(db.ForeignKey('file_ident.id'), nullable=True)
    revision = db.relationship("FileRevision")

class FileRevision(db.Model):
    __tablename__ = 'file_revision'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    edit_id = db.Column(db.ForeignKey('edit.id'))
    extra_json = db.Column(db.ForeignKey('extra_json.sha1'), nullable=True)

    size = db.Column(db.Integer)
    sha1 = db.Column(db.Integer)            # TODO: hash table... only or in addition?
    url = db.Column(db.Integer)             # TODO: URL table

    releases = db.relationship('FileRelease', lazy='subquery')

class Edit(db.Model):
    __tablename__ = 'edit'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    edit_group = db.Column(db.ForeignKey('edit_group.id'), nullable=True)
    editor = db.Column(db.ForeignKey('editor.id'), nullable=False)
    comment = db.Column(db.String, nullable=True)
    extra_json = db.Column(db.ForeignKey('extra_json.sha1'), nullable=True)
    # WARNING: polymorphic. Represents the ident that should end up pointing to
    # this revision.
    entity_ident = db.Column(db.Integer, nullable=True)
    entity_rev = db.Column(db.Integer, nullable=True)
    entity_redirect = db.Column(db.Integer, nullable=True)

class EditGroup(db.Model):
    __tablename__ = 'edit_group'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    editor = db.Column(db.ForeignKey('editor.id'))
    description = db.Column(db.String)

class Editor(db.Model):
    __tablename__ = 'editor'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)

class ChangelogEntry(db.Model):
    # XXX: remove this?
    __tablename__= 'changelog'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    edit_id = db.Column(db.ForeignKey('edit.id'))
    timestamp = db.Column(db.Integer)

class ExtraJson(db.Model):
    __tablename__ = 'extra_json'
    sha1 = db.Column(db.String, primary_key=True)
    json = db.Column(db.String)
