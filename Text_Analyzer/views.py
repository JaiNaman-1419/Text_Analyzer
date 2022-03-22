from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def text_analyzer(request):
    text = request.POST.get('textArea', 'default')
    is_rm_punctuations = request.POST.get('removePunctuation', 'off')
    is_word_counter = request.POST.get('wordCount', 'off')
    is_upper_case = request.POST.get('upperCase', 'off')
    is_lower_case = request.POST.get('lowerCase', 'off')
    is_char_counter = request.POST.get('charCount', 'off')
    is_newline_remover = request.POST.get('newLineRemover', 'off')
    is_space_remover = request.POST.get('spaceRemover', 'off')

    operation = list()
    if is_rm_punctuations == 'on':
        operation.append({'Remove Punctuation' : remove_puctuation(text)})

    if is_word_counter == 'on':
        operation.append({'Word Count' : word_counter(text)})

    if is_upper_case == 'on':
        operation.append({'UPPER CASE' :convert_upper_case(text)})

    if is_lower_case == 'on':
        operation.append({'lower case':convert_lower_case(text)})

    if is_char_counter == 'on':
        operation.append({'Character Count' : char_counter(text)})

    if is_newline_remover == 'on':
        operation.append({'New Line Remover':new_line_remover(text)})

    if is_space_remover == 'on':
        operation.append({'Space Remover':space_remover(text)})

    if is_char_counter == 'off' and is_lower_case == 'off' and is_newline_remover == 'off' and is_rm_punctuations == 'off' and is_space_remover == 'off' and is_upper_case == 'off' and is_word_counter == 'off':
        operation = 'Not Selected!'

    if operation[0] == 'Not Selected!':
        text = None

    params = {'operation': operation}

    return render(request, 'analyzer.html', params)

def convert_upper_case(string:str):
    return string.upper()

def convert_lower_case(string:str):
    return string.lower()

def char_counter(string:str):
    return len(string)

def new_line_remover(string:str):
    string = string.replace('\r\n', ' ')
    string = ' '.join(string.split())
    return string

def space_remover(string:str):
    string = ''.join(string.split(' '))
    return string.strip()

def remove_puctuation(string:str):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    output = [char for char in string if char not in punctuations]
    output = ''.join(output)
    return output

def word_counter(text:str):
    text = text.split()
    count = 0
    for word in text:
        if word in '''!()-[]{};:'"\,<>./?@#$%^&*_~''':
            continue
        count += 1

    return count
