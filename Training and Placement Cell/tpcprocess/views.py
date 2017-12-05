from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, logout, login
from .forms import UserForm, StudentForm, CompanyForm, EligiForm
from .models import Student, Company, EligiCriteria, CandidateList


def register_stu(request, key):
    form1 = UserForm(request.POST or None)
    print key
    if key == '0':
        form2 = StudentForm(request.POST or None)
    else:
        form2 = CompanyForm(request.POST or None)
    if form1.is_valid() and form2.is_valid():
        user = form1.save(commit=False)
        username = form1.cleaned_data['username']
        password = form1.cleaned_data['password1']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if key == '0':
                    stu = Student()
                    stu.user = request.user
                    stu.name = form2.cleaned_data['name']
                    stu.u_id = form2.cleaned_data['u_id']
                    stu.branch = form2.cleaned_data['branch']
                    stu.cgpa = form2.cleaned_data['cgpa']
                    stu.live_kt = form2.cleaned_data['live_kt']
                    stu.dead_kt = form2.cleaned_data['dead_kt']
                    stu.profile = form2.cleaned_data['profile']
                    stu.passing_year = form2.cleaned_data['passing_year']
                    stu.save()
                    companies = EligiCriteria.objects.all()
                    box_size = companies.count() * 60 + 300
                    context = {'companies': companies,
                               'box_size': box_size}
                    return render(request, 'tpcprocess/comp_list.html', context)
                else:
                    com = Company()
                    com.user = request.user
                    com.name = form2.cleaned_data['name']
                    com.location = form2.cleaned_data['location']
                    com.c_id = form2.cleaned_data['c_id']
                    com.save()
                    return render(request, 'tpcprocess/eligi_form.html')
    context = {'form1': form1, 'form2': form2}
    return render(request, 'tpcprocess/register_stu.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if Student.objects.filter(user=user).count() == 1:
                    companies = EligiCriteria.objects.all()
                    box_size = companies.count()*60 + 300
                    context = {'companies': companies,
                               'box_size': box_size}
                    return render(request, 'tpcprocess/comp_list.html', context)

                elif Company.objects.filter(user=user).count() == 1:
                    comp = get_object_or_404(Company, user=request.user)
                    count = comp.eligicriteria_set.count()
                    if count:
                        comp = get_object_or_404(EligiCriteria, company=comp)
                    context = {'filled': count, 'comp': comp}
                    return render(request, 'tpcprocess/eligi_form.html', context)
    return render(request, 'tpcprocess/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'tpcprocess/login.html', context)


def submit_eligi(request):
    if request.method == "POST":
        a = EligiCriteria()
        comp = get_object_or_404(Company, user=request.user)
        a.company = comp
        a.description = request.POST['description']
        a.min_cgpa = request.POST['cgpa']
        a.tech_skills = request.POST['techskill']
        if request.POST['ktoptions'] == 'False':
            a.live_kt_allowed = False
        else:
            a.live_kt_allowed = True
        if request.POST['bloptions'] == 'False':
            a.backlog_allowed = False
        else:
            a.backlog_allowed = True
        a.save()
        count = 1
        comp = get_object_or_404(EligiCriteria, company=comp)
        context = {'filled': count, 'comp': comp}
        return render(request, 'tpcprocess/eligi_form.html', context)
    else:
        comp = get_object_or_404(Company, user=request.user)
        count = comp.eligicriteria_set.count()
        if count:
            comp = get_object_or_404(EligiCriteria, company=comp)
        context = {'filled': count, 'comp': comp}
        return render(request, 'tpcprocess/eligi_form.html', context)


def comp_list(request):
    companies = EligiCriteria.objects.all()
    box_size = companies.count() * 60 + 300
    context = {'companies': companies,
               'box_size': box_size}
    return render(request, 'tpcprocess/comp_list.html', context)


def apply(request, company_id):
    a = get_object_or_404(EligiCriteria, pk=company_id)
    comp = a.company
    stu = get_object_or_404(Student, user=request.user)
    temp = CandidateList.objects.filter(company=comp, student=stu).count()
    if temp == 0:
        a = CandidateList()
        a.company = comp
        a.student = stu
        a.save()
    return comp_list(request)


def candi_list(request):
    company = get_object_or_404(Company, user=request.user)
    candidates = CandidateList.objects.filter(company=company)
    context = {'candidates': candidates}
    return render(request, 'tpcprocess/candi_list.html', context)


def filter_candi(request):
    if request.method == "POST":
        temp = request.POST.getlist('filterlist')
        for r in temp:
            a = get_object_or_404(CandidateList, pk=r)
            if a.is_selected:
                a.is_selected = False
            else:
                a.is_selected = True
            a.save()
    candidates = CandidateList.objects.filter(is_selected=True)
    context = {'candidates': candidates}
    return render(request, 'tpcprocess/filter_candi.html', context)


