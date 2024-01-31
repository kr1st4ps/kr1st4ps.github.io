#!/bin/bash

echo "Starting git commit process"
git add *
git commit -m "Made changes"
git push
echo "Done"