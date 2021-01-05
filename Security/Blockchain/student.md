
# Introduction
Ethereum is a blockchain protocol that introduced smart contracts into the blockchain world.
Smart Contracts are contracts but written by a developer using the Solidity programming language.
Once the smart contract has been written on the blockchain using a transaction it becomes immutable and cannot be further modified.

But as every IT program, Smart Contracts have flaws which can be use by hackers in order to hack a contract and change their behaviour. 

So today, using the website [Capture the Ether](https://capturetheether.com), we are going to introduce you to the hacking of Ethereum Smart Contracts.

# Setup
Before starting any of the following challenges, you need to set up a proper environment.
You can use the code editor of your choice, but we highly recommend using the online Remix Editor available [here](https://remix.ethereum.org).

It has all required features for smart contract development :
- A builtin Solidity compiler
- A local ethereum network with 10 accounts already funded with 100 Ether
- A syntax highlighter

In the `Solidity compiler` tab :
- Set the compiler version to `0.4.21`
- Select the `auto-compile` checkbox.

In the `Deploy & run transactions` :
- The environment refers to the ethereum network you're using.
  JavaScript VM means that the code will execute on a local network
  Injected Web3 will use metamask to connect to the real Ethereum network.
  
No worries, you will install metamask in the first challenge.

# Challenges
## Deploy a contract
For this exercise you have to solve  [this challenge](https://capturetheether.com/challenges/warmup/deploy/).

This will ensure that your Metamask account is properly configured and that you can send a transaction to the network.

No worries if the actions you make with the platform are slow, since you are working on a blockchain, all transactions are verified (yes, even on a test network), thus taking a bit of time (rarely more than a few minutes, but don’t hesitate to call a teacher if you have any doubt).

## Call me
[The following exercise](https://capturetheether.com/challenges/warmup/call-me/) expects you to interact with a deployed contract's function.

As you've read on the first challenge subject, whenever you click the ``Begin Challenge`` button the contract is deployed.
If you need to interact with one of the contract function, there is a corresponding tool in the Remix Editor.

Go to the ``Deploy & run transactions``. There is a field named `At Address` where you can paste your contract address.
This will load your contract ABI (abstract binary interface, used to know what your contract contains so that you can interact with it).

The contract functions and variables are now loaded in the Deployed Contracts field.

## Choose a nickname
[This challenge](https://capturetheether.com/challenges/warmup/nickname/)   is pretty similar to the previous one, but it lets you choose your Capture The Ether username.
## Guess the number
The real security begins !  [The following challenge](https://capturetheether.com/challenges/lotteries/guess-the-number/)  is a first example of a proper contract. Try to steal the ether contained in the contract.
## Guess the secret number
[This challenge](https://capturetheether.com/challenges/lotteries/guess-the-secret-number/)  will require you to write a small script, to, again, steal the ether contained in the contract.
## Assume ownership
[This challenge](https://capturetheether.com/challenges/miscellaneous/assume-ownership/) is a bit different from the previous challenges, but it's very simple. The person that write this contract made a terrible mistake that could be serious in real life. 
Your job is to find this mistake and to use it.
