from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages

from commissions.models import Commission, Job, JobApplication
from .forms import CommissionForm, JobApplicationForm, JobForm



@login_required
def commissions_list(request):
    all_commissions = Commission.objects.all()
    created_commissions = Commission.objects.filter(author=request.user.profile)
    user = request.user.profile
    user_applications = Commission.objects.filter(
            job__job_application__applicant=request.user.profile
        )
   
    
    ctx = {
        'all_commissions': all_commissions,
        'created_commissions': created_commissions,
        'user_applications': user_applications,
    }
    return render(request, 'commission/commissions_list.html', ctx)


@login_required
def commissions_detail(request, pk):
    commission_detail = Commission.objects.get(pk=pk)
    commission_jobs = commission_detail.job
    total_manpower_sum= commission_jobs.aggregate(Sum('manpower_required'))['manpower_required__sum'] or 0
    open_manpower = total_manpower_sum - commission_jobs.filter(job_application__status='Accepted').count()
    
    form = JobApplicationForm()
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = Job.objects.get(role=request.POST.get("job"))
            application.applicant = request.user.profile
            application.status = JobApplication.status_choices[0][1]
            form.save()
            return redirect(reverse('commissions:commissions_list'))
    
    ctx = {
        'commission_detail': commission_detail,
        'commission_jobs': commission_jobs.all,
        'total_manpower_sum': total_manpower_sum,
        'open_manpower': open_manpower,
        'form': form,
    }
    return render(request, 'commission/commissions_detail.html', ctx)

@login_required
def commissions_create(request):
    commission_form = CommissionForm()
    job_form = JobForm()
    if request.method == 'POST':
        commission_form = CommissionForm(request.POST)
        job_form = JobForm(request.POST)
        if commission_form.is_valid() and job_form.is_valid():
            commission = commission_form.save(commit=False)
            commission.author = request.user.profile
            commission.save()
            job = job_form.save(commit=False)
            job.commission = commission
            job.save()
            return redirect('commissions:commissions_list')
    
    ctx = {'commission_form': commission_form, 'job_form': job_form}
    return render(request, 'commission/commissions_add.html', ctx)

@login_required
def commissions_edit(request, pk):
    commission = Commission.objects.get(pk=pk)
    if commission.author != request.user.profile:

        messages.error(request, "You are not authorized to edit this commission.")
        return redirect('commissions:commission_detail', pk=pk)
    
    commission_form = CommissionForm(instance=commission)
    job_form = JobForm(instance=commission)
    if request.method == 'POST':
        commission_form = CommissionForm(request.POST, instance=commission)
        job_form = JobForm(request.POST, instance=commission)
        if commission_form.is_valid()and job_form.is_valid():
            job = job_form.save(commit=False)
            job.commission = commission
            job.save()
            if commission.job.filter(status='Open').count() == 0:
                commission.status = 'Full'
                commission.save()
            return redirect('commissions:commissions_detail', pk=pk)
    
    context = {'commission_form': commission_form,'job_form': job_form }
    return render(request, 'commission/commissions_edit.html', context)
