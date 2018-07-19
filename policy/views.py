from django.http import HttpResponse
from django.shortcuts import render
from policy.forms import PolicyForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from policy.forms import PolicyForm
from django.shortcuts import render
class index(TemplateView):
      template_name = 'policy/index.html'
class details(TemplateView):
      template_name = 'policy/details.html'
      def get(self,request):
          form=PolicyForm()
          return render(request,self.template_name,{'form':form})

      def post(self,request):
          form = PolicyForm(request.POST)
          if form.is_valid():
              gender=form.cleaned_data['gender']
              fname=form.cleaned_data['fname']
              lname=form.cleaned_data['lname']
              email=form.cleaned_data['email']
              age=form.cleaned_data['age']
              tobacco=form.cleaned_data['tobacco']
              city=form.cleaned_data['city']
              state=form.cleaned_data['state']

              name=fname+lname
              args={'form':form,'name':name,'gender':gender,'email':email,'age':age,'tobacco':tobacco,'city':city,'state':state}
              return render(request,self.template_name,args)


