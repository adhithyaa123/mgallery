from django.shortcuts import render,redirect

from django.contrib import messages

from django.views.generic import View

from myapp.forms import MovieForm

from myapp.models import Movies
# Create your views here.

class MovieCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=MovieForm()

        return render(request,"movie_create.html",{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)  

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Movies.objects.create(**data)

            messages.success(request,"movie hasbeen added")

            return redirect("movie_list")

        else:

            messages.error(request,"failed to added movie")

            return render(request,"movie_create.html",{"form":form_instance})


class MovieListView(View):

        def get(self,request,*args,**kwargs):            

            qs=Movies.objects.all()

            return render(request,"movie_list.html",{"movies":qs})


class MovieDetailsView(View):

        def get(self,request,*args,**kwargs): 

            id=kwargs.get("pk")

            qs=Movies.objects.get(id=id)

            return render(request,"movie_details.html",{"movie":qs})

class MovieDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Movies.objects.get(id=id).delete()

        messages.success(request,"movie remove")

        return redirect("movie_list")


class MovieUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        movie_obj=Movies.objects.get(id=id)

        movie_dictionary={
            "title":movie_obj.title,
            "genre":movie_obj.genre,
            "language":movie_obj.language,
            "year":movie_obj.year,
            "run_time":movie_obj.run_time,
            "director":movie_obj.director
        }

        form_instance=MovieForm(initial=movie_dictionary)

        return render(request,"movie_update.html",{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            id=kwargs.get("pk")

            Movies.objects.filter(id=id).update(**data)

            messages.success(request,"movie has been updated")

            return redirect("movie_list")

            

        else:

            messages.error(request,"failed updated")

            return render(request,"movie_update.html",{"form":form_instance})
    