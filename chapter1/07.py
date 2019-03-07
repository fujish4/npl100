from string import Template
 
def format_string(x, y, z):
    return '{}時の{}は{}'.format(x, y, z)
 
def format_string_template(x, y, z):
    t = Template('$hour時の$targetは$value')
    return t.substitute(hour=x, target=y, value=z)
 
print(format_string(12, '気温', 22.4))
print(format_string_template(18, '湿度', 60.4))