from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from repair.forms import RequestForm
from repair.models import Request
from django.contrib import messages


def is_superuser(user):
    return user.is_superuser


@login_required
def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.user = request.user
            if request.user.balance >= new_request.price:  # Проверка баланса
                new_request.save()
                request.user.balance -= new_request.price  # Списывание суммы с баланса
                request.user.save()
                messages.success(request, 'Заявка успешно создана.')
                return redirect('repair:user_requests')
            else:
                messages.error(request, 'Недостаточно средств на балансе для создания заявки.')
    else:
        form = RequestForm()
    return render(request, template_name='repairs/create_repair_request.html', context={'form': form})


@login_required
def pending_user_requests(request):
    requests = Request.objects.filter(user=request.user, status='В ожидании')
    return render(request, template_name='repairs/repair_request_list.html', context={'requests': requests})


@login_required
def processed_user_requests(request):
    requests = Request.objects.filter(user=request.user, status__in=['Выполнено','Отклонено'])
    return render(request, template_name='repairs/processed_request_list.html', context={'requests': requests})


@login_required
def edit_request(request, request_id):
    request_instance = get_object_or_404(Request, id=request_id, user=request.user)
    if request.method == 'POST' and request.POST.get('_method') == 'PUT':
        form = RequestForm(request.POST, request.FILES, instance=request_instance)
        if form.is_valid():
            form.save()
            return redirect('repair:user_requests')
    else:
        form = RequestForm(instance=request_instance)
    return render(
        request,
        template_name='repairs/edit_repair_request.html',
        context={'form': form, 'request_id': request_id}
    )


@login_required
@user_passes_test(is_superuser)
def admin_requests(request):
    requests = Request.objects.all()
    return render(request, template_name='repairs/admin_request_list.html', context={'requests': requests})


@user_passes_test(is_superuser)
def process_request(request, request_id):
    request_instance = get_object_or_404(Request, id=request_id)
    if request.user.is_superuser:
        if request.method == 'POST':
            if 'accept' in request.POST:
                request_instance.status = 'Выполнено'
            elif 'reject' in request.POST:
                request_instance.status = 'Отклонено'
            request_instance.save()
    return redirect('repair:admin_requests')


@login_required
def claim_request(request, request_id):
    request_instance = get_object_or_404(Request, id=request_id)
    if request.method == 'POST':
        request_instance.delete()
        return redirect('repair:processed_request_list')
    return render(request, template_name='repairs/processed_request_list.html', context={'request_id': request_id})


@login_required
def delete_request(request, request_id):
    request_instance = get_object_or_404(Request, id=request_id, user=request.user)
    if request.method == 'POST':
        request_instance.delete()
        return redirect('repair:user_requests')
    return render(request, template_name='repairs/repair_request_list.html', context={'request_id': request_id})
