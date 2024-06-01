from django.urls import path
from repair.views import *
app_name = 'repair'

urlpatterns = [
    path('create_request/', create_request, name='create_request'),
    path('user_requests/', pending_user_requests, name='user_requests'),
    path('processed_request_list/', processed_user_requests, name='processed_request_list'),
    path('edit_request/<int:request_id>/', edit_request, name='edit_request'),
    path('admin_requests', admin_requests, name='admin_requests'),
    path('process_request/<int:request_id>/', process_request, name='process_request'),
    path('claim_request/<int:request_id>/', claim_request, name='claim_request'),
    path('delete_request/<int:request_id>/', delete_request, name='delete_request'),
]