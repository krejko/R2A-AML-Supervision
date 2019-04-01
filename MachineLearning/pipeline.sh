$tablas = () #aquí va la lista de tablas a evaluar

for i in ${tablas[@]}; do
	cat psql -U postgres -d database_name -c 'SELECT *  FROM $ ;'  |    
	    grep -Ev '^(<)' |
	    sed 's!http[s]\?://\S*!!g' |
	    sed 's/\./\.\n/g' |
	    sed 's/^ //g'  |
	    sed 's/ \{2,\}/ /g' |
	    sed *.py |
	    sed -e '/^$/d' |
	    grep '.\{30\}'
done

exit