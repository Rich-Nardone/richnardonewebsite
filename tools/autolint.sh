#!usr/bin/env bash

# Run from parent directory with 'sh tools/autolint.sh'

# ESLINT
for s in scripts/*.jsx;
do
    echo "Linting $s"
    npx eslint $s --fix
    echo "press any button to continue"
    read -n 1 -s
done

# PYLINT
# Precede all lints with a reformat
for p in *.py;
do
    echo "Linting {$p}"
    black $p
    pylint $p
    echo "press any button to continue"
    read -n 1 -s
done

echo "All good!"