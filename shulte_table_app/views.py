from django.shortcuts import render
from .forms import ShulteTableForm
import random

def shulte_table(request):
    if request.method == 'POST':
        form = ShulteTableForm(request.POST)
        if form.is_valid():
            size = form.cleaned_data['size']
            table_data = generate_shulte_table(size)
            return render(request, 'shulte_table.html', {'form': form, 'table_data': table_data})
    else:
        form = ShulteTableForm()

    return render(request, 'shulte_table.html', {'form': form})

def generate_shulte_table(size):
    # Create a list of numbers from 1 to size^2
    numbers = list(range(1, size*size + 1))

    # Shuffle the list randomly
    random.shuffle(numbers)

    # Reshape the list into a 2D array to represent the table
    table_data = [numbers[i:i+size] for i in range(0, len(numbers), size)]

    return table_data
