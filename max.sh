#!/bin/bash

echo "first number: "
read num1
echo "second number: "
read num2

if (( num1 > num2 )); 
    then 
    echo "$num1"
    elif (( num2 > num1 ));
    then
    echo "$num2"
    else
    echo "$num1 = $num2"
    fi
