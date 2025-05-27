#!/bin/bash
num_test=4
question=016_minimum-coins
for (( i = 1 ; i <= ${num_test} ; i++ ))
do
    result=`cat test_${question}_${i}.txt | python ${question}.py`
    answer=`cat ans_${question}_${i}.txt`
    if [ "${result}" = "${answer}" ];then
        echo "test ${i} OK"
    else
        echo "test ${i} NG"
        echo "---your result---"
        echo "${result}"
        echo "---answer---"
        echo "${answer}"
        exit 1
    fi
done
