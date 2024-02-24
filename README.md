# Stručný návod
Oba skripty vyžadují Python3, spouští se klasicky z terminálu `python3 nazev_skriptu`.

## `set_details_scraper.py`
Vybírá náhodné sety a stahuje jejich data.

V hlavičce jsou definované názvy vstupních a výstupních souborů:
- `set_number_filename` - obsahuje úplně všechna čísla setů, ze kterých skript vybírá náhodná čísla setů; ve výchozí podobě je nastaven na hodnotu `set_numbers.txt`
- `output_table_filename` - data jednotlivých setů jsou ukládaná do souboru ve formátu `csv`, který by měl normálně otevřít jako tabulka v Excelu. Pokud je soubor prázdný nebo neexistuje, bude automaticky vytvořen a bude nadepsané záhlaví tabulky. Jinak jsou při každém dalším spuštění programu připisovány záznamy o setech do nových řádků. Ve výchozí podobě je nastaven na hodnotu `lego_sets.csv`

### Použití 
Zatím je skript nastavený tak, aby rovnou po spuštění vygeneroval náhodná čísla setů a pro tyto sety stáhl a uložil data. Požadovaný počet těchto setů lze zadat jako argument při spuštění programu, tedy například pro 50 požadovaných setů náhodných setů ke stažení by spuštění v terminálu vypadalo takto: `python3 set_details_scraper.py 50` . Při vynechání argumentu se stáhne vždy jen jeden náhodný set.

## `set_numbers_scraper.py`
Stahuje čísla všech setů. Tenhle skript v podstatě není potřeba spouštět, pokud už je jednou soubor se všemi čísly setů dostupný  - samotný běh skriptu trvá několik minut. Pokud je potřeba postahovat všechna čísla znovu, stačí ho spustit bez jakýchkoliv argumentů - jen je v  tom případě vhodné se přesvědčit, že je výstupní soubor prázdný nebo neexistuje.

V hlavičce je definovaný název výstupního souboru:
- `output_file` - obyčejný textový soubor, do kterého se na každý řádek zapisuje jedno číslo setu. Čísla se postupně připisují, takže pokud už soubor existuje, nedojde k přepsání stávajících dat. Ve výchozí podobě je nastaven na hodnotu `set_numbers.txt`

