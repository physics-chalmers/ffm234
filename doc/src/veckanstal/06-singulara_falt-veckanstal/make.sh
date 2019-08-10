#!/bin/sh
set -x

function system {
  "$@"
  if [ $? -ne 0 ]; then
    echo "make.sh: unsuccessful command $@"
    echo "abort!"
    exit 1
  fi
}

if [ $# -eq 0 ]; then
echo 'bash make.sh slides1|slides2'
exit 1
fi

name=$1
rm -f *.tar.gz

opt=
opt="--encoding=utf-8"

rm -f *.aux


#--html=${name}-reveal
#--system doconce format html $name --pygments_html_style=perldoc --keep_pygments_html_bg --html_links_in_new_window --html_output=$html $opt
#--system doconce slides_html $html reveal --html_slide_theme=beige

# Plain HTML documentsls

#--html=${name}-solarized
#--system doconce format html $name --pygments_html_style=perldoc --html_style=solarized3 --html_links_in_new_window --html_output=$html $opt
#--system doconce slides_html $html doconce --nav_button=text method=hrule

html=${name}
system doconce format html $name --pygments_html_style=default --html_style=bloodish --html_links_in_new_window --html_output=$html $opt
system doconce split_html $html.html
# Remove top navigation in all parts
doconce subst -s '<!-- begin top navigation.+?end top navigation -->' '' ${name}-plain.html ._${name}*.html

# Bootstrap style
html=${name}-bs
system doconce format html $name --html_style=bootstrap --pygments_html_style=default --html_admon=bootstrap_panel --html_output=$html $opt
system doconce split_html $html.html --pagination --nav_button=bottom




# Ordinary plain LaTeX document
system doconce format pdflatex $name --minted_latex_style=trac --latex_admon=paragraph $opt
system doconce ptex2tex $name envir=minted
# Add special packages
doconce subst "% Add user's preamble" "\g<1>\n\\usepackage{simplewick}" $name.tex
doconce replace 'section{' 'section*{' $name.tex
pdflatex -shell-escape $name
pdflatex -shell-escape $name

mv -f $name.pdf ${name}-print.pdf
cp $name.tex ${name}-plain-print.tex

# IPython notebook
system doconce format ipynb $name $opt

# Publish
dest=../../pub
if [ ! -d $dest/$name ]; then
mkdir $dest/$name
mkdir $dest/$name/pdf
mkdir $dest/$name/html
mkdir $dest/$name/ipynb
fi
cp ${name}*.pdf $dest/$name/pdf
cp -r ${name}*.html ._${name}*.html reveal.js $dest/$name/html

# Figures: cannot just copy link, need to physically copy the files
if [ -d fig-${name} ]; then
if [ ! -d $dest/$name/html/fig-$name ]; then
mkdir $dest/$name/html/fig-$name
fi
cp -r fig-${name}/* $dest/$name/html/fig-$name
fi

cp ${name}.ipynb $dest/$name/ipynb
ipynb_tarfile=ipynb-${name}-src.tar.gz
if [ ! -f ${ipynb_tarfile} ]; then
cat > README.txt <<EOF
This IPython notebook ${name}.ipynb does not require any additional
programs.
EOF
tar czf ${ipynb_tarfile} README.txt
fi
cp ${ipynb_tarfile} $dest/$name/ipynb

