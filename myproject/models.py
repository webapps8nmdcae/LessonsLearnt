from myproject import db,app
from werkzeug.security import generate_password_hash,check_password_hash
from flask_security import UserMixin # , RoleMixin
import decimal
import flask.json
from datetime import datetime, timedelta
from sqlalchemy import text

def CreateSessionWebApps():
    sessionWebApps = db.create_scoped_session(options=dict(bind=db.get_engine(app, 'WebApps'), binds={}))
    return sessionWebApps

#
# class Role(db.Model):
#     __tablename__ = 'AspNetRoles'
#     __bind_key__ = 'WebApps'
#     id = db.Column(db.String(450), primary_key=True)
#     name = db.Column(db.String(450), unique=True)
#     NormalizedName=db.Column(db.String(450), unique=True)
#     Description = db.Column(db.String(500),primary_key=False)
#
#
# class UserRoles(db.Model):
#     __tablename__ = 'AspNetUserRoles'
#     __bind_key__ = 'WebApps'
#     id = db.Column(db.Integer(), primary_key=True)
#     UserId = db.Column(db.String(450), db.ForeignKey('AspNetUsers.id', ondelete='CASCADE'))
#     RoleId = db.Column(db.String(450), db.ForeignKey('AspNetRoles.id', ondelete='CASCADE'))
#
#
class User(db.Model):
    __tablename__ = "AspNetUsers"
    __bind_key__ = 'WebApps'
    __table_args__ = {u'schema': 'dbo'}
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(500), primary_key=False)
    email = db.Column(db.String(500), primary_key=False)
    PasswordHash = db.Column(db.String(500), primary_key=False)
    password = db.Column(db.String(500), primary_key=False)
    active = db.Column(db.Boolean)
    NameFirst = db.Column(db.String(500), primary_key=False)
    NameLast = db.Column(db.String(500), primary_key=False)
    EmployeeNumber = db.Column(db.String(500), primary_key=False)
    FunctionName = db.Column(db.String(500), primary_key=False)
    FullName = db.Column(db.String(500), primary_key=False)

    # json
    def json(self):
        return {'name': self.username}

    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'PasswordHash': self.PasswordHash,
            'active': self.active,
            'NameFirst': self.NameFirst,
            'NameLast': self.NameLast,
            # 'HR_EmployeeId': self.hrEmployee[0].Id,
            # 'EmployeeNumber': self.hrEmployee[0].EmployeeNumber.strip(),
            # 'FunctionName': self.FunctionName,
            'FullName': self.FullName,
            # 'ProjectIds': '-'.join([str(a.Id) for a in self.projectUsers]),
        }

class ProjectEmployerClassification(db.Model):
    __tablename__ = 'ProjectEmployerClassification'
    __bind_key__ = 'WebApps'
    __table_args__ = {u'schema': 'proj'}

    Id = db.Column(db.Integer(), primary_key=True)
    ProjectEmployerClassificationName = db.Column(db.String(50), primary_key=False, unique=True)

class Project(db.Model):
    __tablename__ = 'Project'
    __bind_key__ = 'WebApps'
    __table_args__ = {u'schema': 'proj'}
    
    Id = db.Column(db.Integer, primary_key=True)
    ProjectName = db.Column(db.String())
    ProjectNumber = db.Column(db.String())
    proj_ProjectEmployerClassificationId = db.Column(db.Integer)
    Relevance_LessonsLearnt = db.Column(db.Boolean)

class LLCategoryType(db.Model):
    __tablename__ = 'LLCategoryType'
    __bind_key__ = 'WebApps'
    __table_args__ = {u'schema': 'qhse'}

    Id = db.Column(db.Integer, primary_key=True)
    CategoryType = db.Column(db.String())

class LessonLearnCategory(db.Model):
    __tablename__ = 'LessonLearnCategory'
    __bind_key__ = 'WebApps'
    __table_args__ = {u'schema': 'qhse'}

    Id = db.Column(db.Integer, primary_key=True)
    Category = db.Column(db.String())
    qhse_LLCategoryTypeId = db.Column(db.Integer, db.ForeignKey('qhse.LLCategoryType.Id'))

    category_type = db.relationship("LLCategoryType")

class LessonLearnSubCategory(db.Model):
    __tablename__ = 'LessonLearnSubCategory'
    __bind_key__ = 'WebApps'
    __table_args__ = {u'schema': 'qhse'}

    Id = db.Column(db.Integer, primary_key=True)
    SubCategory = db.Column(db.String())
    qhse_LessonLearnCategoryId = db.Column(db.Integer, db.ForeignKey('qhse.LessonLearnCategory.Id'))
    ExpertiseId = db.Column(db.String(200))
    category = db.relationship("LessonLearnCategory")

class LessonLearnForm(db.Model):
    __tablename__ = 'LessonLearnForm'
    __bind_key__ = 'WebApps'
    __table_args__ = {u'schema': 'qhse'}
    
    Id = db.Column(db.Integer, primary_key=True)
    proj_ProjectId = db.Column(db.Integer)
    Date = db.Column(db.DateTime)
    qhse_LLCategoryId = db.Column(db.Integer)
    Title = db.Column(db.String)
    Background = db.Column(db.String)
    Implication = db.Column(db.String)
    LessonLearnt = db.Column(db.String)
    qshe_LLApprovalOrderId = db.Column(db.Integer)
    ActionStatus = db.Column(db.Integer)
    RequesterId = db.Column(db.Integer)
    IsProject = db.Column(db.Boolean)
    qhse_LLDepartmentId = db.Column(db.Integer)
    proj_ProjectEmployerClassificationId = db.Column(db.Integer)
    ImpactOnProcedure = db.Column(db.Boolean)
    TenderStage = db.Column(db.Boolean)
    ConstructabilityView = db.Column(db.Boolean)
    CloseOutAction = db.Column(db.String)
    IsArchived = db.Column(db.Integer)
    AttachmentPath = db.Column(db.String)
    CreatedBy = db.Column(db.String)
    CreatedOn = db.Column(db.DateTime)
    UpdatedBy = db.Column(db.String)
    UpdatedOn = db.Column(db.DateTime)

class LessonLearnFormDocuments(db.Model):
    __tablename__ = 'LessonLearnFormDocuments'
    __bind_key__ = 'WebApps'
    __table_args__ = {u'schema': 'qhse'}
    
    Id = db.Column(db.Integer, primary_key=True)
    qhse_LLFormId = db.Column(db.Integer, db.ForeignKey('qhse.LessonLearnForm.Id'))
    AttachmentPath = db.Column(db.String)

class LessonLearnLApprovalData(db.Model):
    __tablename__ = 'LessonLearnLApprovalData'
    __bind_key__ = 'WebApps'
    __table_args__ = {u'schema': 'qhse'}
    
    Id = db.Column(db.Integer, primary_key=True)
    LLFormId = db.Column(db.Integer, db.ForeignKey('qhse.LessonLearnForm.Id'))
    qhse_LLApprovalOrderId = db.Column(db.Integer)
    qhse_LLDepartmentId = db.Column(db.Integer)
    hr_EmployeeId = db.Column(db.Integer)
    Comments = db.Column(db.String)
    qshe_LLApprovalStatusId = db.Column(db.Integer)
    CreatedBy = db.Column(db.String)
    CreatedOn = db.Column(db.DateTime)
    UpdatedBy = db.Column(db.String)
    UpdatedOn = db.Column(db.DateTime)
    qhse_LessonLearnPriorityLevelId = db.Column(db.Integer)
    qhse_LessonLearnPrimaryBusinessImpactId = db.Column(db.Integer)

class LessonLearnFormCategory(db.Model):
    __tablename__ = 'LessonLearnFormCategory'
    __bind_key__ = 'WebApps'
    __table_args__ = {u'schema': 'qhse'}

    Id = db.Column(db.Integer, primary_key=True)
    qhse_LessonLearnFormId = db.Column(db.Integer,db.ForeignKey('qhse.LessonLearnForm.Id'))
    qhse_LLCategoryTypeId = db.Column(db.Integer)
    qhse_LLCategoryId = db.Column(db.Integer)
    qhse_LLSubCategoryId = db.Column(db.Integer)
    CreatedBy = db.Column(db.String)
    CreatedOn = db.Column(db.DateTime)
    UpdatedBy = db.Column(db.String)
    UpdatedOn = db.Column(db.DateTime)

class LessonLearnPriorityLevel(db.Model):
    __tablename__ = 'LessonLearnPriorityLevel'
    __bind_key__ = 'WebApps'
    __table_args__ = {u'schema': 'qhse'}

    Id = db.Column(db.Integer, primary_key=True)
    PriorityLevel = db.Column(db.String(50))

class LessonLearnPrimaryBusinessImpact(db.Model):
    __tablename__ = 'LessonLearnPrimaryBusinessImpact'
    __bind_key__ = 'WebApps'
    __table_args__ = {u'schema': 'qhse'}

    Id = db.Column(db.Integer, primary_key=True)
    PrimaryBusinessImpact = db.Column(db.String(50))

class LessonLearnFormExpertise(db.Model):
    __tablename__ = 'LessonLearnFormExpertise'
    __bind_key__ = 'WebApps'
    __table_args__ = {u'schema': 'qhse'}

    Id = db.Column(db.Integer, primary_key=True)
    ExpertiseId = db.Column(db.String())
    qhse_LessonLearnFormId = db.Column(
        db.Integer,
        db.ForeignKey('qhse.LessonLearnForm.Id')
    )

    CreatedBy = db.Column(db.String(200))
    CreatedOn = db.Column(db.DateTime)

    UpdatedBy = db.Column(db.String)  # VARCHAR(MAX)
    UpdatedOn = db.Column(db.DateTime)