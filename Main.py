from pyscript import document

def calculate_square(event):
    # 1. Grab the number from the HTML input box
    input_element = document.querySelector("#numberInput")
    number_value = input_element.value
    
    # 2. Check if the input is a valid number and square it
    try:
        number = float(number_value)
        result = number * number
        output_text = f"The square of {number} is {result}!"
    except ValueError:
        output_text = "Please enter a valid number."
    
    # 3. Send the final text back to the HTML screen
    output_element = document.querySelector("#output")
    output_element.innerText = output_text
