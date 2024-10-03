from django import forms

class MovieForm(forms.Form):

    title=forms.CharField()

    options=(
        ("fiction","fiction"),
        ("Action","Action"),
        ("comedey","comedy"),
        ("ghost","ghost")
    )

    genre=forms.ChoiceField(choices=options)

    language=forms.CharField()

    year=forms.CharField()

    run_time=forms.IntegerField()

    director=forms.CharField()


    def clean(self):

        cleaned_data=super().clean()

        run_time=cleaned_data.get("run_time")

        year=cleaned_data.get("year")

        if int(year)<1900:

            error_message="year>1990"

            self.add_error("year",error_message)


   
        if run_time > 210 or run_time < 60:

            error_miss="Run time should be greater than 210 and less than 60"

            self.add_error("run_time",error_miss)


        