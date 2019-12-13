print('Привет, как дела?')
answer = input()
if ('хорошо' in answer or 'отлично' in answer or 'прекрасно' in answer) and (('не' or '?') not in answer):
    print('Здорово, хорошего дня!')
elif ('плохо' in answer or 'ужасно' in answer) and (('не' or '?') not in answer):
    print('Очень жаль, но не расстраивайся')
else:
    print('Понятно.')