Il dataset presente nella cartella /data/raw/, a cui è stata rimossa la prima colonna che presenta gli indici, contiene informazioni sulle case.
È composto da 414 osservazioni, non mancanti, tutte numeriche, dove le colonne indicano: x1 la data di avvenuta transazione, x2 l'età della casa, 
x3 la distanza dal supermercato più vicino, x4 il numero di convenience store, x5 la latitudine e x6 la longitudine. y indica il prezzo ed è usata 
come variabile dipendente.

Il modello utilizzato è una regressione lineare in cui vengono usate tutte le 6 variabili x come indipendenti e la y come dipendente, dividendo il dataset 
in train e test.

Per utilizzare l'applicazione scrivere nel terminal 'streamlit run UI.py', a questo punto sarà necessario selezionare quali variabili si hanno a disposizione, e, 
dopo aver premuto 'next', modificare i parametri, facendo attenzione a restare entro i limiti (si possono usare i segni +- come aiuto).
Infine premendo su 'predict' risulterà il prezzo previsto per la propria casa.
