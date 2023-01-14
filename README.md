# echidna-auto-gen
POC script that parses solidity contracts and constructs echidna test cases based on properties in the smart contract.

Current POC script searches for modifiers, such as onlyOwner and then generates applicable test cases (e.g., checking that the owner has changed)
