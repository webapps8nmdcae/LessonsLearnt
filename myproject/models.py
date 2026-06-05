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
    
    Id = db.Column(db.Integer, primary_key=True)
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
#
#     # relationships
#     roles = db.relationship('Role', secondary='AspNetUserRoles')
#     hrEmployee = db.relationship("Employee", back_populates="userX")
#     projectUsers = db.relationship('ProjectUser', back_populates="user")
#
#     # initializing user
#     def __init__(self, email, username, passwordInput):
#         self.username = username
#         self.email = email
#         self.PasswordHash = generate_password_hash(passwordInput)
#         # self.test= test
#
#     def check_password(self, passwordInput):
#         return self.check_password(self.password, passwordInput)
#
#     # print
#     def __repr__(self):
#         return f"Username is {self.username} user email is {self.email} password is {self.PasswordHash}"
#
#     # json
#     def json(self):
#         return {'name': self.username}
#
#     @property
#     def serialize(self):
#         return {
#             'id': self.id,
#             'username': self.username,
#             'email': self.email,
#             'PasswordHash': self.PasswordHash,
#             'active': self.active,
#             'NameFirst': self.NameFirst,
#             'NameLast': self.NameLast,
#             'HR_EmployeeId': self.hrEmployee[0].Id,
#             'EmployeeNumber': self.hrEmployee[0].EmployeeNumber.strip(),
#             'FunctionName': self.FunctionName,
#             'FullName': self.FullName,
#             # 'ProjectIds': '-'.join([str(a.Id) for a in self.projectUsers]),
#         }
#
#
# class AspNetUserProject(db.Model):
#     __tablename__ = "AspNetUserProject"
#     __bind_key__ = 'WebApps'
#     __table_args__ = {u'schema': 'dbo'}
#     Id = db.Column(db.Integer, primary_key=True)
#     AppId = db.Column(db.Integer, primary_key=False)
#     Proj_ProjectId = db.Column(db.Integer, primary_key=False)
#     DateStart = db.Column(db.Date(), primary_key=False)
#     DateFinish = db.Column(db.Date(), primary_key=False)
#     IsAdmin = db.Column(db.Boolean)
#     IsCostController = db.Column(db.Boolean)
#     IsFinance = db.Column(db.Boolean)
#     AspNetUserId = db.Column(db.String(), primary_key=False)
#
#
# #################################################################################################
# ################ MODELS TECHNICAL  ##############################################################
# #################################################################################################
# class Employee(db.Model):
#     __tablename__ = 'Employee'
#     __bind_key__ = 'WebApps'
#     __table_args__ = {u'schema': 'hr'}
#     Id = db.Column(db.Integer(), primary_key=True)
#     EmployeeName = db.Column(db.String(), unique=False)
#     EmployeeNumber = db.Column(db.String(450), unique=False)
#     EmployeeEmail = db.Column(db.String(50), unique=False)
#     gen_CompanyId = db.Column(db.Integer(), db.ForeignKey('gen.Company.Id', ondelete='CASCADE'))
#     EmployeeTelephone = db.Column(db.String(50), unique=False)
#     dev_AspNetUsersId = db.Column(db.String(450), db.ForeignKey('AspNetUsers.id', ondelete='CASCADE'))
#     tech_EquipmentStatusId = db.Column(db.Integer())
#     hr_StandardFunctionId = db.Column(db.Integer())
#     ContractualHours = db.Column(db.Float())
#     hr_ContractualDaysId = db.Column(db.Integer())
#     IsActive = db.Column(db.Boolean)
#
#     Remarks = db.Column(db.String())
#     EID = db.Column(db.String())
#     IsManpower = db.Column(db.Boolean)
#     AppId = db.Column(db.Integer())
#     CreatedBy = db.Column(db.String())
#     CreatedOn = db.Column(db.DateTime())
#     UpdatedBy = db.Column(db.String())
#     UpdatedOn = db.Column(db.DateTime())
#
#     # relationships
#     projectUsers = db.relationship("ProjectUser", back_populates="employee")
#     projectUserActivity = db.relationship("ProjectUserActivity", back_populates="employee")
#     userX = db.relationship("User", back_populates="hrEmployee")
#     company = db.relationship("Company", back_populates="employee")
#
#     @property
#     def serialize(self):
#         return {
#             'Id': self.Id,
#             'EmployeeName': self.EmployeeName,
#             'EmployeeNumber': self.EmployeeNumber,
#             'EmployeeEmail': self.EmployeeEmail,
#             'gen_CompanyId': self.gen_CompanyId,
#             'EmployeeTelephone': self.EmployeeTelephone,
#             'dev_AspNetUsersId': self.dev_AspNetUsersId,
#             'tech_EquipmentStatusId': self.tech_EquipmentStatusId,
#             'hr_StandardFunctionId': self.hr_StandardFunctionId,
#         }
#
#
# class EmployeeStatus(db.Model):
#     __tablename__ = 'EmployeeStatus'
#     __bind_key__ = 'WebApps'
#     __table_args__ = {u'schema': 'hr'}
#     Id = db.Column(db.Integer(), primary_key=True)
#     EmployeeStatusName = db.Column(db.String(), unique=False)
#     IsChargeable = db.Column(db.Boolean)
#     projectUserHistory = db.relationship("ProjectUserHistory", back_populates="employeeStatus")
#

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