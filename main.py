from decimal import Decimal, getcontext

class Book:
    def __init__(self, sentence):
        self.encoding = {
            ' ': '000',
            'A': '001',
            'B': '002',
            'C': '003',
            'D': '004',
            'E': '005',
            'F': '006',
            'G': '007',
            'H': '008',
            'I': '009',
            'J': '010',
            'K': '011',
            'L': '012',
            'M': '013',
            'N': '014',
            'O': '015',
            'P': '016',
            'Q': '017',
            'R': '018',
            'S': '019',
            'T': '020',
            'U': '021',
            'V': '022',
            'W': '023',
            'X': '024',
            'Y': '025',
            'Z': '026',
            '.': '027',
            ',': '028',
            '?': '029',
            '!': '030',
            ':': '031',
            ';': '032',
            '-': '033',
            '(': '034',
            ')': '035',
            '\'': '036',
        }
        self.sentence = sentence

    def encode_sentence(self):
        encoded = ''.join(self.encoding.get(letter.upper(), '') for letter in self.sentence)
        decimal = '0.' + encoded
        return decimal

    def find_divisors(self, decimal):
        # Code to prevent rounding
        getcontext().prec = len(decimal)
        decimal_value = Decimal(decimal)
        
        # convert into fraction object
        fraction = Decimal(decimal_value).as_integer_ratio()
        numerator, denominator = fraction[0], fraction[1]

        # calculate new encoded
        new_encoded = Decimal(numerator) / Decimal(denominator)
        return numerator, denominator, new_encoded
        
    def decode_decimal(self, decimal):
        reverse_encoding = {value: key for key, value in self.encoding.items()}

        decimal_str = str(decimal)[2:]  # Remove '0.'
        decoded = ''
        i = 0
        while i < len(decimal_str):
            if decimal_str[i:i+3].startswith('\\'): # properly detect apostrophes 
                encoded_value = decimal_str[i+1:i+4]
                i += 4
            else:
                encoded_value = decimal_str[i:i+3]
                i += 3
            decoded += reverse_encoding.get(encoded_value, '')

            # Fix capitalization issues
            decoded_sentences = decoded.split('. ')
            capitalized_sentences = [sentence.capitalize() for sentence in decoded_sentences]
            final_decoded = '. '.join(capitalized_sentences)

        return final_decoded
        
def run(sentence):
    literature = Book(sentence)
    decimal = literature.encode_sentence()
    numerator, denominator, new_encoded = literature.find_divisors(decimal)
    decoded = literature.decode_decimal(new_encoded)

    report = f"""
    \033[35m=======================\033[0m


    \033[35mENCODED BOOKS:\033[0m

    \033[36m\tSentence: {sentence}\033[0m

    \033[32m\tEncoded: {decimal}\033[0m

    \033[33m\tFraction: {numerator}/{denominator}:\033[0m 

    \033[34m\tDecoded: {new_encoded} => {decoded}\033[0m

    \033[35m=======================\033[0m
    """

    print(report)

    run_again = input("Would you like to run the program again? (Y/N) ")
    if (run_again == "Y"):
        sentence = input("What sentence would you like to encode? ")
        run(sentence)
    else:
        print("Shutting off!")

sentence = input("What sentence would you like to encode? ")
run(sentence)