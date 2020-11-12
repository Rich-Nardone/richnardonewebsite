#!bin/bash

# Run from parent directory with 'sh tools/test_all_python.sh'

echo "Finding coverage..."
coverage run -m --source=. unittest tests/*.py && coverage html
for p in tests/*.py;
do
    echo "Running $p"
    python $p
done
