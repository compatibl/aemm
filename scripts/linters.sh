#!/bin/bash

cd ..

echo ""
echo "Validate using flake8"
flake8 cl --config=.flake8
flake8 tests --config=.flake8

# Change back to the original directory
cd -
