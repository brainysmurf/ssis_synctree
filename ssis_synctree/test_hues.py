import hues
hues.success('plain method')
hues.info('again')
success = hues.huestr(' S ').white.bg_green.bold.colorized
error = hues.huestr(' W ').black.bg_yellow.bold.colorized
reverse = hues.huestr(' reverse ').black.bg_white.bold.colorized
print(success, 'fancy')
hues.log(error, 'warning')
print(reverse)
