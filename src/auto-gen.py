import re

#define modifiers to search for
modifiers = {'onlyOwner': '    function echidna_check_onlyOwner() public returns (bool) {\n        return(owner != address(0x10000));\n    }\n\n'}

with open('../contracts/TestContract.sol', 'r') as file:
    source_code = file.read()

modifier_functions = []
for modifier in modifiers:
    pattern = re.compile(f'modifier {modifier}\(')
    matches = pattern.finditer(source_code)
    for match in matches:
        #get the start and end line numbers of the modifier function
        start_line = source_code[:match.start()].count('\n') + 1
        end_line = start_line + source_code[match.start():].count('}')
        test_case = modifiers.get(modifier)
        modifier_functions.append({'name': modifier, 'start_line': start_line, 'end_line': end_line, 'test_case': test_case})
    
for modifier_function in modifier_functions:
    with open('../contracts/TestContract.sol', 'r') as file:
        source_code = file.readlines()
    #insert test case after modifier
    source_code.insert(modifier_function['end_line'],
    modifier_function['test_case'])
    #create new solidity file with test cases
    with open('../contracts/TestContractWithTests.sol','w') as file:
        file.writelines(source_code)