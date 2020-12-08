#!usr/bin/env bash

# Run from parent directory with 'sh tools/autolint.sh'

# ESLINT
for s in "scripts/*.jsx";
do
    echo "Linting $s"
    npx eslint $s --fix
done
echo "press any button to continue"
read -n 1 -s

# PYLINT
# Precede all lints with a reformat
# Game logic
for p in game/*.py;
do
    echo "Linting {$p}"
    python -m black $p
    python -m pylint $p
    echo "press any button to continue"
    read -n 1 -s
done
# Integration
for p in *.py;
do
    echo "Linting {$p}"
    python -m black $p
    python -m pylint $p
    echo "press any button to continue"
    read -n 1 -s
done

echo "All good!"