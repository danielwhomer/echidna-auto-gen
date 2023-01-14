pragma solidity ^0.8.0;

contract TestContract {
    address owner = 0x10000;
    bool flipped = false;

    modifier onlyOwner(){
        require(msg.sender == owner);
        _;
    }
    
    function changeOwner(address _a) public {
        owner = _a;
    }

    function test() onlyOwner public {
        flipped = true;
    }
}