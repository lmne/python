""""
We schrijven een programma om de resultaten te verwerken van de finale van de wedstrijd "Slimste student ter wereld".
 Voor deze finale worden 10 meerkeuzevragen gesteld. De antwoorden van de deelnemers worden verwerkt m.b.v. een computer.
  Geef eerst de 10 juiste antwoorden via toetsenbord in (bv. "ABCBBCADBC"). De meerkeuzevragen hebben elk 4 keuzemogelijkheden,
   nl. A, B, C of D. Per deelnemer beschikken we over volgende gegevens: deelnemersnummer, geboortedatum,
    de 10 antwoorden van de deelnemer (A, B, C, D of E (E = vraag blanco gelaten)), de tijd in sec waarin de vragen werden beantwoord.
    De gegevens van 1 deelnemer worden in 1 keer via het toetsenbord ingegeven: bijv. "1234 14/05/1999 ABEBDCCDBC 7352".
    De invoer stopt als de waarde 0 wordt ingegeven.
De punten voor een deelnemer wordt als volgt berekend:
2 punten per juist antwoord
0 punten per vraag die de deelnemer heeft opengelaten
-1 punt per fout beantwoorde vraag. De deelnemers vertrekken vanaf 20 punten.
Er moet een lijst worden afgedrukt die er als volgt uitziet:

1. 1234  18 jaar  2u 12m  32 ptn
2. 3510  21 jaar  1u 56m  12 ptn
3. 3511  20 jaar  2u 02m  30 ptn
De lijst wordt afgedrukt in volgorde van ingave.

Bij het bepalen van de leeftijd, houdt men rekening met de verjaardagsdatum. Stel vandaag is het 10/10/2018, iemands geboortedatum is 22/11/2000 deze persoon is op dit moment dus 17 jaar oud. Gebruik een functie om de leeftijd te berekenen. De huidige datum wordt als gegeven ingegeven.

Gebruik een functie om de tijd in seconden om te zetten naar uren en minuten. Bij een restduur van 30 seconden of meer, wordt het aantal minuten naar boven afgerond.

Gebruik een functie om het resultaat per kandidaat te berekenen.
"""


