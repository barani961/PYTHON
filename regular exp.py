import re
text_search="AbC123$EfG456@HiJ789!KlM0#NoPqRs%TuVw&XyZ@12^34#56$78!90AbCdEfGhIjKlMnOpQrStUvWxYz1234@5678#90"
patter=re.compile(r'234')
matches=patter.finditer(text_search)
for match in matches:
    print(match)
print(text_search[83:86])
