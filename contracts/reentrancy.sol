// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Bank {

    mapping(address => uint) balances;

    function withdraw() public {

        uint amount = balances[msg.sender];

        (bool success,) =
            msg.sender.call{value: amount}("");

        require(success);

        balances[msg.sender] = 0;
    }
}