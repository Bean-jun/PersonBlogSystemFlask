from flask import Blueprint

# 创建蓝图
home_blueprint = Blueprint('blog', __name__)

# 导入视图函数
from . import home, template, account

# 首页视图
home_blueprint.add_url_rule('/', view_func=home.IndexView.as_view(name='index'))
home_blueprint.add_url_rule('/profile/', view_func=home.ProfileView.as_view(name='profile'))

home_blueprint.add_url_rule('/list/<int:id>/', view_func=home.NoteListView.as_view(name='note_list'))

home_blueprint.add_url_rule('/detail/<int:id>/', view_func=home.DetailView.as_view(name='detail'))
home_blueprint.add_url_rule('/edit/', view_func=home.EditView.as_view(name='edit'))
home_blueprint.add_url_rule('/edit/delete/<int:id>/', view_func=home.DeleteNoteView.as_view(name='note_delete'))

home_blueprint.add_url_rule('/login/', view_func=account.LoginView.as_view(name='login'))
home_blueprint.add_url_rule('/oauth/', view_func=account.OauthView.as_view(name='oauth'))
home_blueprint.add_url_rule('/logout/', view_func=account.LogoutView.as_view(name='logout'))
home_blueprint.add_url_rule('/register/', view_func=account.RegisterView.as_view(name='register'))
home_blueprint.add_url_rule('/profile/userlogo/', view_func=account.ModifyLogo.as_view(name='userlogo'))
home_blueprint.add_url_rule('/profile/userpwd/', view_func=account.ModifyPassWdView.as_view(name='userpwd'))
home_blueprint.add_url_rule('/profile/addcategory/', view_func=account.AddCategory.as_view(name='addcategory'))
