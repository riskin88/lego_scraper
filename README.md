# Stručný návod
Oba skripty vyžadují Python3, spouští se klasicky z terminálu `python3 nazev_skriptu`.

## `set_details_scraper.py`
Vybírá náhodné sety a stahuje jejich data.

V hlavičce jsou definované názvy vstupních a výstupních souborů:
- `set_number_filename` - obsahuje úplně všechna čísla setů, ze kterých skript vybírá náhodná čísla setů; ve výchozí podobě je nastaven na hodnotu `set_numbers.txt`
- `output_table_filename` - data jednotlivých setů jsou ukládaná do souboru ve formátu `csv`, který by měl normálně otevřít jako tabulka v Excelu. Pokud je soubor prázdný nebo neexistuje, bude automaticky vytvořen a bude nadepsané záhlaví tabulky. Jinak jsou při každém dalším spuštění programu připisovány záznamy o setech do nových řádků. Ve výchozí podobě je nastaven na hodnotu `lego_sets.csv`

### Použití 
Zatím je skript nastavený tak, aby rovnou po spuštění bez argumentů stáhl data o všech setech. Aby to vždycky netrvalo zbytečně dlouho, je toto možné stránkovat. Program volitelně bere 2 argumenty _offset_ a _limit_ (pokud je zadán pouze jeden, spustí se program jako bez argumentů). _offset_ určuje, kolik čísel setů od začátku ze vstupního seznamu se přeskočí, a _limit_ potom udává, kolik se má následně vybrat po sobě jdoucích čísel. Pokud tedy například chceme stáhnout data pro prvních 1000 setů, spuštění by v terminálu vypadalo takto: `python3 set_details_scraper.py 0 1000` (pro druhých 1000 se první argument nahradí 1000, atd.).

V kódu jsou připravené funkce i na generování náhodných čísel setů.

## `set_numbers_scraper.py`
Stahuje čísla všech setů. Tenhle skript v podstatě není potřeba spouštět, pokud už je jednou soubor se všemi čísly setů dostupný  - samotný běh skriptu trvá několik minut. Pokud je potřeba postahovat všechna čísla znovu, stačí ho spustit bez jakýchkoliv argumentů - jen je v  tom případě vhodné se přesvědčit, že je výstupní soubor prázdný nebo neexistuje.

V hlavičce je definovaný název výstupního souboru:
- `output_file` - obyčejný textový soubor, do kterého se na každý řádek zapisuje jedno číslo setu. Čísla se postupně připisují, takže pokud už soubor existuje, nedojde k přepsání stávajících dat. Ve výchozí podobě je nastaven na hodnotu `set_numbers.txt`

