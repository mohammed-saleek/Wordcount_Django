from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def result(request):
    word_para = request.GET['para']
    wordlist = word_para.split()
    word_count = {}
    for word in wordlist:
        if word in word_count:
            count += 1
        else:
            count = 1
        
        word_count[word] = count
    word_counts = word_count.sorted()
    context = {'word_counts':word_counts}

    return render(request, 'result.html', context)
