def print_separator(text):
	"""
	print separator to console
	"""
    separator = "===================================================================================================="
    total_letters = len(text)
    start_text = int(len(separator) / 2) - int(total_letters / 2)
    end_text = start_text + total_letters
    full_separator = separator[:start_text - 1] + text + separator[end_text:]
    print(full_separator)
    
if __name__ == '__main__':
	print_separator("test")    
	print_separator("START LOG FILTERING")    
	print_separator("END LOG FILTERING")    
	print_separator("START LOG CONVERTER")    
	print_separator("END LOG CONVERTER")    
	print_separator("START LOG CLEANING")
	print_separator("END LOG CLEANING")
	print_separator("START LOG EXTRACTION")
	print_separator("END LOG EXTRACTION")
	print_separator("START LOG TRANSFORMATION")
	print_separator("END LOG TRANSFORMATION")