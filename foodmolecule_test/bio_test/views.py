from django.shortcuts import render
from django.http import HttpResponse

def bio_test(request):
    if request.method == "POST":
        x = request.POST.get('input')

        if x == "Molecule":
            response_text = (
                "Food Molecules:\n"
                "1. Starch\n"
                "2. Glucose\n"
                "3. Calories\n"
                "4. Lipid(fat)\n"
                "5. Protein"
            )
        elif x == "Test":
            response_text = (
                "Tests:\n"
                "1. Biuret solution\n"
                "2. Benedict's reagent\n"
                "3. Ethanol\n"
                "4. Iodine solution\n"
                "5. Burning"
            )
        else:
            response_text = "Invalid input. Please choose 'Molecule' or 'Test'."
    else:
        response_text = ""

    return render(request, 'bio_test.html', {'response': response_text})
