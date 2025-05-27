#!/bin/bash
num_test=3
question=012_red-painting
for (( i = 1 ; i <= ${num_test} ; i++ ))
do
    result=`cat test_${i}_0test.txt | python ${question}.py`
    answer=`cat test_${i}_1answ.txt`
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
