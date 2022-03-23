import argparse

def find_goodies_with_least_difference(no_of_employees, inp_goodies_prices, output_file):
    if no_of_employees < 2:
        print('Need atleast 2 emoloyees to solve the goodies dilemma')
        return
    price_values = list(inp_goodies_prices.keys())
    price_values.sort()

    # Go through each and find the difference and get the best value
    price_first_index = 0
    price_diff = price_values[no_of_employees - 1] - price_values[0]
    curr_price_first_index = 1
    for x in range(price_first_index + no_of_employees, len(inp_goodies_prices)):
        loop_price_diff = price_values[x] - price_values[curr_price_first_index]
        if price_diff > loop_price_diff:
            price_diff = loop_price_diff
            price_first_index = curr_price_first_index
        curr_price_first_index += 1

    # Save it to the file
    with open(output_file, "w") as f:
        f.write('The goodies selected for distribution are:\n\n')
        for x in range(price_first_index, price_first_index+no_of_employees):
            f.write("{}\n".format(inp_goodies_prices[price_values[x]]))
        f.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is {}".format(price_diff))

if __name__ == "__main__":
    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("-i", "--input", help="Input data file path", required=True)
    parser.add_argument("-o", "--output", help="Output data file path")

    # Read arguments from command line
    args = parser.parse_args()
    output_file =  'output.txt'
    if args.output :
        output_file = args.output
    # Read input from file
    inp_goodies_prices = {}
    with open(args.input, 'r') as f:
        no_of_employees = int(f.readline())
        while True:
            line = f.readline()
            if not line:
                break
            line_split_arr = line.split(':')
            inp_goodies_prices[int(line_split_arr[1].strip())] =  line.strip()
    find_goodies_with_least_difference(no_of_employees, inp_goodies_prices, output_file)

