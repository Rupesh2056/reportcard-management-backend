from .user import urlpatterns as user_url_patterns
from .student import urlpatterns as student_url_patterns
from .course import urlpatterns as course_url_patterns
from .report import urlpatterns as report_url_patterns

urlpatterns = []
urlpatterns += student_url_patterns
urlpatterns += user_url_patterns
urlpatterns += course_url_patterns
urlpatterns += report_url_patterns

