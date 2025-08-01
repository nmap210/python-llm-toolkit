from helper_functions import get_llm_response, print_llm_response

ice_cream_flavors = [
    "Vanilla",
    "Chocolate",
    "Strawberry",
    "Mint Chocolate Chip"
]

for flavor in ice_cream_flavors:
    prompt = f"""For the ice cream flavor listed below, 
provide a captivating description that could be used for promotional purposes.

Flavor: {flavor}
"""
    response = get_llm_response(prompt)
    print_llm_response(prompt, response)

