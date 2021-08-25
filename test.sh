#!/bin/bash
python3 simulation.py tests/00_path.txt tests/00_item.txt tests/00_quest.txt < tests/00_input.txt > tests/00_actual.txt
DIFF=$(diff tests/00_expected.txt tests/00_actual.txt)
if [ "$DIFF" == "" ]
then
    echo "[Passed] test_00"
else
    echo "[Failed] test_00"
fi

python3 simulation.py tests/01_path.txt tests/01_item.txt tests/01_quest.txt < tests/01_input.txt > tests/01_actual.txt
DIFF=$(diff tests/01_expected.txt tests/01_actual.txt)
if [ "$DIFF" == "" ]
then
    echo "[Passed] test_01"
else
    echo "[Failed] test_01"
fi

python3 simulation.py tests/02_path.txt tests/02_item.txt tests/02_quest.txt < tests/02_input.txt > tests/02_actual.txt
DIFF=$(diff tests/02_expected.txt tests/02_actual.txt)
if [ "$DIFF" == "" ]
then
    echo "[Passed] test_02"
else
    echo "[Failed] test_02"
fi

python3 simulation.py tests/03_path.txt tests/03_item.txt tests/03_quest.txt < tests/03_input.txt > tests/03_actual.txt
DIFF=$(diff tests/03_expected.txt tests/03_actual.txt)
if [ "$DIFF" == "" ]
then
    echo "[Passed] test_03"
else
    echo "[Failed] test_03"
fi

python3 simulation.py tests/04_path.txt tests/04_item.txt tests/04_quest.txt < tests/04_input.txt > tests/04_actual.txt
DIFF=$(diff tests/04_expected.txt tests/04_actual.txt)
if [ "$DIFF" == "" ]
then
    echo "[Passed] test_04"
else
    echo "[Failed] test_04"
fi

python3 simulation.py tests/05_path.txt tests/05_item.txt tests/05_quest.txt < tests/05_input.txt > tests/05_actual.txt
DIFF=$(diff tests/05_expected.txt tests/05_actual.txt)
if [ "$DIFF" == "" ]
then
    echo "[Passed] test_05"
else
    echo "[Failed] test_05"
fi

python3 simulation.py tests/06_path.txt tests/06_item.txt tests/06_quest.txt < tests/06_input.txt > tests/06_actual.txt
DIFF=$(diff tests/06_expected.txt tests/06_actual.txt)
if [ "$DIFF" == "" ]
then
    echo "[Passed] test_06"
else
    echo "[Failed] test_06"
fi

python3 simulation.py tests/07_path.txt tests/07_item.txt tests/07_quest.txt < tests/07_input.txt > tests/07_actual.txt
DIFF=$(diff tests/07_expected.txt tests/07_actual.txt)
if [ "$DIFF" == "" ]
then
    echo "[Passed] test_07"
else
    echo "[Failed] test_07"
fi

python3 simulation.py tests/08_path.txt tests/08_item.txt tests/08_quest.txt < tests/08_input.txt > tests/08_actual.txt
DIFF=$(diff tests/08_expected.txt tests/08_actual.txt)
if [ "$DIFF" == "" ]
then
    echo "[Passed] test_08"
else
    echo "[Failed] test_08"
fi

python3 simulation.py tests/09_path.txt tests/09_item.txt tests/09_quest.txt < tests/09_input.txt > tests/09_actual.txt
DIFF=$(diff tests/09_expected.txt tests/09_actual.txt)
if [ "$DIFF" == "" ]
then
    echo "[Passed] test_09"
else
    echo "[Failed] test_09"
fi
