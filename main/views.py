from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import FormClub


@login_required()
def index(request):
    if request.method == "POST":
        form = FormClub(request.POST)
        if form.is_valid():
            run = True
            error = False
            response = []
            equivalent = []
            numbers = request.POST['number_vise']
            cotes1 = request.POST['cote_equipe_1'].split(",")
            cotes2 = request.POST['cote_equipe_2'].split(",")

            if len(cotes1) < 2 or len(cotes2) < 2:
                error = True
            else:

                for i in cotes1:
                    ii = float(i)
                    for y in cotes2:
                        yy = float(y)
                        p = yy * ii

                        if p == float(numbers):
                            response.append(
                                f"combinaison {i} X {y} \n soit {i} premiere combinaison et {y} deuxieme "
                            )
            if (error):
                context = {
                    "form": FormClub,
                    'error': 'verifier vos donnes'
                }
                return render(request, "main/index.html", context)
            else:
                context = {
                    "form": FormClub,
                    'cotes': response,
                    'run' : run
                }
                return render(request, "main/index.html", context)
        else:

            context = {
                "form": form,
                'error': 'une erreur est survenu'
            }
            return render(request, "main/index.html", context)

    else:

        context = {
            "form": FormClub(),
        }
        return render(request, "main/index.html", context)
