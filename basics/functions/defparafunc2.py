#another example of default parameters in functions

def profile(name='Narendra Modi', work='politician'):
    print('Profile: \n Name = {} \n Occupation = {}'.format(name, work))

profile('Anirudha','student')
profile()
profile(name='Sharad Pawar')
profile(work='Prime Minister')
