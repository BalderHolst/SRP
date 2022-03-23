#!/bin/bash
echo "Watching..."


inotifywait -rm --exclude "aux|bib~|out|bcf|xml|toc|bbl|pdf|log|git\/" -e modify . | while read change; do
	echo "change detected in $change"
	echo "change detected in $change" >> watch.log
	pdflatex SRP.tex
done

