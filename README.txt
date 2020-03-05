Simulación de  corrida  de  programas  en  un  sistema  operativo  de  tiempo  compartido  (el  procesador  se  comparte  por  una porción de tiempo entre cada programa que se desea correr). En la terminología de sistemas  operativos se llama “proceso” a un programa que se ejecuta.
El ciclo de vida de un proceso dentro del sistema operativo es:

New: el  proceso  llega  al  sistema  operativo  pero  debe  esperar  que  se  le  asigne  memoria  RAM. Si hay memoria disponible puede pasar al estado  de  ready, sino  permanece  haciendo  cola.

Ready:el proceso está listo  para correr pero debe esperar que lo atienda el CPU.

Running: el  CPU  atiende  al  proceso  por  un  tiempo  limitado,  suficiente  para  realizar  solamente  3  instrucciones. Al completarse el tiempo de atención el proceso es retirado del CPU y se  actualiza  el  contador  de  instrucciones  a  realizar.

