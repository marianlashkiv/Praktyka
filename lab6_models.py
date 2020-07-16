from lab6_printing_functions import print_models, show_completed_models

final_unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
final_completed_models = []
final_completed_models = print_models(final_unprinted_designs, final_completed_models)
show_completed_models(final_completed_models)
