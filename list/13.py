# 13. Генерация строки в цикле
def build_definition_list(definitions):
    if not definitions:
        return ''
    parts = []
    for definition, description in definitions:
        parts.append(f'<dt>{definition}</dt><dd>{description}</dd>')
    return f'<dl>{''.join(parts)}</dl>'

definitions = [
  ['Блямба', 'Выпуклость, утолщение на поверхности чего-либо'],
  ['Бобр', 'Животное из отряда грызунов'],
]

print(build_definition_list(definitions))
# '<dl><dt>Блямба</dt><dd>Выпуклость, утолщение на поверхности чего-либо</dd><dt>Бобр</dt><dd>Животное из отряда грызунов</dd></dl>';