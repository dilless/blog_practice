"""

@Author  : dilless
@Time    : 2018/7/18 23:54
@File    : urls.py
"""
from django.urls import path

from course.views import AboutView, CourseListView, ManageCourseListView, CreateCourseView, DeleteCourseView, \
    CreateLessonView, ListLessonsView, DetailLessonView, StudentListLessonView

app_name = 'course'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('course-list/', CourseListView.as_view(), name='course_list'),
    path('manage-course/', ManageCourseListView.as_view(), name='manage_course'),
    path('create-course/', CreateCourseView.as_view(), name='create_course'),
    path('delete-course/<int:pk>/', DeleteCourseView.as_view(), name='delete_course'),
    path('create-lesson/', CreateLessonView.as_view(), name='create_lesson'),
    path('list-lessons/<int:course_id>/', ListLessonsView.as_view(), name='list_lessons'),
    path('detail-lesson/<int:lesson_id>/', DetailLessonView.as_view(), name='detail_lesson'),
    path('lessons-list/<int:course_id>/', StudentListLessonView.as_view(), name='lessons_list'),
]
