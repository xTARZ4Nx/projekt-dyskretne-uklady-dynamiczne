# Dyskretne Uklady Dynamiczne - Projekt

Ten projekt zawiera implementacje i analize czterech zadan z zakresu dyskretnych ukladow dynamicznych.

## Autorzy
* Lukasz Sasin
* Mateusz Sobczak
* Kamil Styn

## Wymagania

Projekt wymaga Pythona 3 oraz bibliotek wymienionych w pliku `requirements.txt`.
* `numpy`
* `matplotlib`
* `scipy`

## Instalacja i uruchomienie

### 1. Przygotowanie srodowiska

Zaleca sie utworzenie wirtualnego srodowiska, aby uniknac konfliktow bibliotek.

**Windows:**
```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

**Linux / MacOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Uruchamianie zadan

Po aktywacji srodowiska, kazde zadanie mozna uruchomic bezposrednio:

**Zadanie 1: Model Populacji**
```bash
python zad1.py
```

**Zadanie 2: Model Krwinek (Lasoty)**
```bash
python zad2.py
```

**Zadanie 3: Odwzorowanie Logistyczne**
```bash
python zad3.py
```
*Generuje pliki: `bifurkacja.png`, `orbita.png`*

**Zadanie 4: Trojkat Sierpinskiego**
```bash
python zad4.py
```
*Generuje plik: `sierpinski.png`*
