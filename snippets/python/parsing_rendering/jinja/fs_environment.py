env = Environment(loader=FileSystemLoader(str(HOME.absolute())))
template = env.get_template(path)
result = template.render()
